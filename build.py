#!/usr/bin/env python3
"""Compile peptides/* directories into the single-file site index.html.

Usage:  python3 build.py

Source of truth lives in peptides/_index.json (registry) and one folder per
monographed peptide containing data.json, monograph.md and references.json.
The template (template.html) carries all layout and behaviour; this script
only injects the compiled data. No external dependencies.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
CODE = re.compile(r"`([^`]+)`")
H = re.compile(r"^(#{1,6})\s+(.*)$")
UL = re.compile(r"^(\s*)[-*]\s+(.*)$")
SPECIAL = re.compile(r"^(#{1,6}\s|\||\s*[-*]\s|\s*>)")


def inline(s):
    """Inline formatting: code, links, bold, italic. HTML-escapes the rest."""
    ph = []

    def _code(m):
        ph.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(ph) - 1}\x00"

    def _link(m):
        ph.append(
            f'<a href="{html.escape(m.group(2), quote=True)}" rel="noopener">'
            f"{html.escape(m.group(1))}</a>"
        )
        return f"\x00{len(ph) - 1}\x00"

    s = CODE.sub(_code, s)
    s = LINK.sub(_link, s)
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    for i, t in enumerate(ph):
        s = s.replace(f"\x00{i}\x00", t)
    return s


def table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    if len(cells) > 1 and all(re.fullmatch(r":?-{2,}:?", c) for c in cells[1]):
        cells = [cells[0]] + cells[2:]
    out = ["<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr>"]
    for r in cells[1:]:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    return '<div class="sc"><table>' + "".join(out) + "</table></div>"


def render_blocks(lines):
    out, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if not l.strip():
            i += 1
            continue
        m = H.match(l)
        if m:
            lvl = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{min(lvl, 6)}>{inline(m.group(2))}</h{min(lvl, 6)}>")
            i += 1
            continue
        if l.strip().startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            out.append(table(rows))
            continue
        if UL.match(l):
            items = []
            while i < n and UL.match(lines[i]):
                items.append(inline(UL.match(lines[i]).group(2)))
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
            continue
        buf = [l.strip()]
        i += 1
        while i < n and lines[i].strip() and not SPECIAL.match(lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")
    return "\n".join(out)


def sections(md):
    """Split markdown on ## headings; each becomes {t: title, h: html}."""
    parts, cur = [], None
    for line in md.split("\n"):
        m = re.match(r"^##\s+(.*)$", line.rstrip())
        if m:
            if cur:
                parts.append(cur)
            cur = {"t": m.group(1).strip(), "b": []}
        elif re.match(r"^#\s+", line) or cur is None:
            continue
        else:
            cur["b"].append(line)
    if cur:
        parts.append(cur)
    return [{"t": p["t"], "h": render_blocks(p["b"])} for p in parts]


def main():
    reg = json.loads((ROOT / "peptides" / "_index.json").read_text(encoding="utf-8"))
    monos = {}
    for dj in sorted((ROOT / "peptides").rglob("data.json")):
        folder = dj.parent
        data = json.loads((folder / "data.json").read_text(encoding="utf-8"))
        data["sections"] = sections((folder / "monograph.md").read_text(encoding="utf-8"))
        refs = folder / "references.json"
        data["refs"] = json.loads(refs.read_text(encoding="utf-8")) if refs.exists() else []
        monos[data["id"]] = data
    tpl = (ROOT / "template.html").read_text(encoding="utf-8")
    changelog_html = ""
    cl = ROOT / "CHANGELOG.md"
    if cl.exists():
        changelog_html = render_blocks(cl.read_text(encoding="utf-8").split("\n"))
    out = (
        tpl.replace("/*__REGISTRY__*/null", json.dumps(reg, ensure_ascii=False))
        .replace("/*__MONOS__*/null", json.dumps(monos, ensure_ascii=False))
        .replace("/*__CHANGELOG__*/null", json.dumps(changelog_html, ensure_ascii=False))
    )
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print(f"built index.html: {len(reg)} registry entries, {len(monos)} monograph(s)")


if __name__ == "__main__":
    main()
