# Peptide Monograph Repository

Independent, non-commercial reference on research peptides: evidence, safety and regulatory status. Pilot draft, unreviewed, not medical advice. No sales, ads or vendor links.

## Status

Draft v0.1. The registry lists 50 candidate peptides. The GLP-1/incretin class (10 peptides) has evidence drafts with DOI-backed references, BPC-157 has a pilot monograph, and the remaining entries have skeleton pages pending evidence. Every claim must be mapped to a DOI before a monograph can advance.

## Structure

The directory tree is the source of truth; `build.py` compiles it into the single-file site.

```
peptides/
  _index.json                      # registry: name, class, status, note
  <class>/<peptide>/               # one folder per monograph
    data.json                      # identity, sequence, status, structure notes
    monograph.md                   # narrative sections (markdown)
    references.json                # DOI + evidence tier + the claim it supports
template.html                      # site shell: layout, behaviour, generators
build.py                           # compiles peptides/ -> index.html (stdlib only)
index.html                         # generated single-file site (committed)
assets/                            # vendored 3Dmol.js and RDKit.js (WASM), BSD-3
```

## Building

```bash
python3 build.py
```

Requires only Python 3 (standard library). Open `index.html` directly, or serve it:

```bash
python3 -m http.server
```

## Features

- Searchable index of peptides grouped by pharmacological class and approval status
- Monographs with summary, mechanism, tiered evidence, indications and dose, safety, contraindications, side effects, product quality, regulatory and sport status, clinician notes, plain-language section and evidence gaps
- **DOI-first references:** every reference is a `https://doi.org/…` link carrying an evidence tier and the claim it supports
- **Structure views generated from the sequence field:** colour-coded residue strip, atom-level 2D structure drawn by RDKit (with formula and atom-count cross-check), and an interactive 3D schematic (ideal α-helix / β-strand) with optional experimental PDB structures
- Works offline; classic pharmacopoeia light-only styling

## Evidence standards

A Tier 0–5 rubric applies (see the Standards page on the site). Allowed sources: peer-reviewed literature, trial registries, regulators, pharmacopoeias, WADA, independent analytical studies, systematic reviews. Never used as evidence: vendor sites and press releases, forums, social media, unverified certificates of analysis.

## Community

Discussion is hosted on GitHub Discussions: <https://github.com/mchugh1122/research-peptide-monographs/discussions>

Community posts are anecdotal and never change monographs. No vendor names, links, discount codes or sourcing threads, including indirect forms. If you suspect an adverse reaction, report it to your national scheme (for example FDA MedWatch, MHRA Yellow Card or HPRA).

## Disclaimer

Pilot draft, unreviewed, and not medical advice. Nothing here is sold, advertised or linked to a vendor.

## Third-party libraries

3Dmol.js and RDKit.js are vendored unmodified under the BSD 3-Clause License; see `assets/3DMOL-LICENSE.txt`.
