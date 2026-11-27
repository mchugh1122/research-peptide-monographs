# Changelog

## 28 November 2026

- **Print stylesheet** added: monographs print as clean black-on-white sheets (nav, buttons and search hidden; boxes and tables bordered; page-break handling); a Print button on each monograph.
- **Monograph search:** the index search now also searches monograph text and references, showing a "Monograph matches" box with snippets.
- **Gap-fill:** BPC-157 dose table populated from the FDA briefing study conditions; EU/CA/AU regulatory rows made concrete; exenatide gained the EXSCEL DOI; AOD-9604 and LL-37 registry notes flagged for verification; MGF sequence note corrected — the 24-mer is the rat IGF-1Ec E-peptide, the human one is longer (UniProt P05019).

## 27 November 2026

- **3D ribbons:** the 3D view is now a ribbon (cartoon) style throughout — a locally generated ideal α-helix backbone ribbon for every entry with a sequence or residue trace (including cyclic peptides, with bridges noted as not shown); residue traces added for the sequence-less peptides (melanocortins, GHRPs, gonadorelin, dermorphin, CJC-1295, elamipretide, dihexa, PNC-27, FOXO4-DRI). The RDKit 3D (ETKDG) path was removed after finding the WebAssembly build only produces 2D coordinates.

## 27 November 2026

- **Class F–L evidence drafts (final batch):** thymosin alpha-1, Thymalin, ARA-290, LL-37, elamipretide, MOTS-c, humanin, Epitalon, FOXO4-DRI, dermorphin, PNC-27 and teriparatide populated with DOI-backed references, completing evidence drafts for all 49 monographs. MGF gained its two key references. MOTS-c and Epitalon include the July 2026 FDA PCAC committee votes.
- **Class E + J evidence drafts:** Semax, Selank, DSIP (emideltide), Cerebrolysin, Dihexa and P21 (neuropeptides) and gonadorelin, oxytocin and kisspeptin-10 (reproductive peptides) populated with DOI-backed, tiered references. DSIP/emideltide includes the July 2026 FDA PCAC evaluation and the 7–6 vote against 503A inclusion; Semax includes the 8–5 committee vote.

## 26 November 2026

- **Class C + D evidence drafts:** TB-500, thymosin beta-4, GHK-Cu and KPV (tissue repair) and bremelanotide, afamelanotide, setmelanotide and Melanotan II (melanocortins) populated with DOI-backed, tiered references; TB-500 cross-referenced to the July 2026 FDA PCAC briefing.

## 24 November 2026

- **Site retitled** to Pharmacopoeia Peptidorum (repo name unchanged).


- **3D viewer bug fixed:** the viewer is now recreated per entry, so navigating between monographs via links no longer leaves the 3D box empty; GHRP-2, GHRP-6 and hexarelin gained recorded SMILES with 2D and RDKit 3D views.
- **3D structures extended:** RDKit ETKDG generates atom-level 3D conformations from recorded SMILES for modified and cyclic peptides (semaglutide, liraglutide, tirzepatide, oxytocin, melanocortins, gonadorelin, thymosin α1, AOD-9604, ipamorelin, cagrilintide, elamipretide, dermorphin, PNC-27, dihexa, FOXO4-DRI, CJC-1295, TB-500, thymosin β4); backbone schematics now also shown for modified peptides with a "modifications not shown" label.
- **Licence:** site code MIT; monograph content CC BY-SA 4.0.
- **BPC-157 evidence pass:** pilot monograph now carries 3 DOI-backed animal/original papers, the FDA PCAC July 2026 briefing documents (characterisation gaps, immunogenicity, animal toxicity signals, 8–6 committee vote), and the WADA S0 listing; sequence verified against the FDA document (CAS 137525-51-0).
- **Class B evidence drafts:** tesamorelin, sermorelin, CJC-1295, ipamorelin, GHRP-2, GHRP-6, hexarelin, AOD-9604 and MGF/PEG-MGF populated with DOI-backed references.
- **Structure views extended:** recorded SMILES (PubChem) now render 2D structures for modified peptides (semaglutide, liraglutide, tirzepatide, tesamorelin, oxytocin, melanocortins, gonadorelin, thymosin α1, AOD-9604, ipamorelin); experimental PDB views added for oxytocin (2MGO) and LL-37 (2K6O); experimental-only 3D for cyclic peptides.
- **Sequence verification pass:** 22 sequences verified against PubChem/regulator records (formula match); corrections: AOD-9604 (Cys6–Cys14 disulfide, C-terminal acid), TB-500 and thymosin β4 (N-acetylated forms noted).
- **Changelog page** added to the site, fed by this file.
- **Community:** GitHub Discussions enabled; the site's Discussion page is a rules hub linking out to the board.
- **Structure and tooling:** repository restructured into a directory substructure (`peptides/`), with `build.py` compiling it into the single-file site. RDKit (WASM) atom-level 2D structures and 3Dmol schematic 3D views (ideal α-helix / β-strand) generated from the sequence field; classic pharmacopoeia light-only theme.
- **Registry populated:** 50 candidate peptides grouped by pharmacological class; skeletons for all single-sequence peptides.
- **Class A evidence drafts:** semaglutide, tirzepatide, liraglutide, exenatide, retatrutide, CagriSema, cagrilintide, survodutide, mazdutide and ecnoglutide monographs populated with DOI-backed, tiered references.

## Corrections

- None yet. Corrections to monograph claims will be recorded here with dates and the change made.
