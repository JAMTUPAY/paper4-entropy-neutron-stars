# Paper 4 — Entropy-Constrained Neutron Stars

## Repository Structure
code/     -> plotting scripts (CSV -> figures)  
data/     -> CSV outputs (mass–radius, tidal deformability)  
figures/  -> PNG figures (paper-ready)  
paper/    -> LaTeX (main.tex, refs.bib)  

## Rebuilding Figures
./run_all.sh

## Building the Paper (MacTeX/TeX Live)
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

## Notes
- All plots are generated **only** from the CSV data in `/data`.
- No hidden fits or extra parameters.
- CSVs can be regenerated from the TOV + tidal deformability solvers if needed.
