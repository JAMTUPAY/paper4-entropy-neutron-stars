cat > README.md <<'EOF'
# Entropy-Constrained Neutron Stars: Universal QCD Bound Predicts \(M_{\max}\) & \(\Lambda_{1.4}\)

**DOIs:**  
- **Paper 1:** Universal Entropy–Mass Relation in QCD — [10.5281/zenodo.16743904](https://doi.org/10.5281/zenodo.16743904)  
- **Paper 2:** Entropy-Forbidden Exotic Hadrons — [10.5281/zenodo.16752674](https://doi.org/10.5281/zenodo.16752674)  
- **Paper 3:** Universal Entropy Threshold for QGP Formation — [10.5281/zenodo.16762323](https://doi.org/10.5281/zenodo.16762323)  

**License:** MIT (see `LICENSE`)

---

## Abstract

A single renormalization-group (RG) entropy ceiling in QCD,  
\[
|\Delta S_{\rm RG}| = 9.81\,k_B \ \text{per baryon},
\]  
acts as a hard cutoff on the dense-matter equation of state (EOS). Enforcing  
\( S_{\rm eff}(\rho) \le S_{\max} \) with  
\( S_{\max} \in \{8.0,\,9.81,\,12.0\}\,k_B \) generates Tolman–Oppenheimer–Volkoff (TOV) sequences that:  

- Reproduce observed \( \sim 2\,M_\odot \) pulsars.  
- Predict \(\Lambda_{1.4}\) inside the GW170817 90% credible interval.  
- Require **no empirical fitting or tunable astrophysical parameters** — \(S_{\max}\) is fixed from QCD theory (Papers 1–3).  

This repository contains **all data, code, figures, and LaTeX source** to reproduce the results, with a deterministic CSV → figure pipeline and full QA.

---

## Key Results

- **Parameter-free bridge** from QCD microphysics to neutron-star macrophysics.  
- \(M_{\max}\):  
  - 1.66 \(M_\odot\) @ \(S_{\max} = 8.0\,k_B\)  
  - 2.07 \(M_\odot\) @ \(S_{\max} = 9.81\,k_B\)  
  - 2.27 \(M_\odot\) @ \(S_{\max} = 12.0\,k_B\)  
- \(\Lambda_{1.4}\): 180–220, matching GW170817 bounds.  
- NICER radii compatible across all caps.  
- EOS remains causal: \(0 \le c_s^2/c^2 \le 1\).

---
```
## Repository Structure
paper4-entropy-neutron-stars/
├── code/
│   ├── plot_lambda_from_csv.py
│   └── plot_mr_from_csv.py
├── data/
│   ├── comprehensive_entropy_constrained_neutron_stars.csv
│   ├── mass_radius_results_08.00kB.csv
│   ├── mass_radius_results_09.81kB.csv
│   ├── mass_radius_results_12.00kB.csv
│   ├── lambda_vs_mass_08.00kB.csv
│   ├── lambda_vs_mass_09.81kB.csv
│   └── lambda_vs_mass_12.00kB.csv
├── figures/
│   ├── mass_radius_curve_08.00kB.png
│   ├── mass_radius_curve_09.81kB.png
│   ├── mass_radius_curve_12.00kB.png
│   ├── lambda_vs_mass_08.00kB.png
│   ├── lambda_vs_mass_09.81kB.png
│   ├── lambda_vs_mass_12.00kB.png
│   ├── appendix_fig_a1.png
│   ├── entropy_components.png
│   └── entropy_constraint_effect.png
├── paper/
│   ├── main.tex
│   └── Entropy_Constrained_Neutron_Stars_from_a_Universal_QCD_Bound.pdf
├── requirements.txt
├── run_all.sh
├── LICENSE
└── README.md

```
---

## Quick Start

### Rebuild all figures from CSVs
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
./run_all.sh

Compile the paper locally (TeX Live / MacTeX)
cd paper
pdflatex main
bibtex main
pdflatex main
pdflatex main

Use with Overleaf
Upload main.tex and the figures/ directory.

Data & QA

TOV CSVs:
rho_c_over_n0, M_solar, R_km, P_central, S_central_kB, cs2_over_c2, S_limit

Λ CSVs:
mass_solar, radius_km, k2, Lambda

QA Checks:
	•	All columns present.
	•	NaN count = 0.
	•	Physical ranges:
	•	(M\in[0.8,,2.5],M_\odot)
	•	(R\in[10,,16]) km
	•	(P_{\rm central} \sim 10^{34}–10^{37}) Pa
	•	(0 \le c_s^2/c^2 \le 1)
	•	(k_2 \in [0.03,,0.15])
	•	(\Lambda \in [10,,10^4]) for (M \in [1.0,,2.2],M_\odot)

All plots regenerate byte-for-byte from CSVs; no hidden data sources.

⸻

Core Discovery

Entropy ceiling as density cutoff:
[
S_{\rm eff}(\rho) \le S_{\max} \quad\Rightarrow\quad \rho_{\max} \ \text{fixes} \ M_{\max}, \ \Lambda_{1.4}.
]
One universal QCD constant governs neutron star observables without astrophysical tuning.

⸻
Citation
@article{tupay2025ns_entropy_bound,
  author = {Tupay, Johann Anton Michael},
  title  = {Entropy-Constrained Neutron Stars from a Universal QCD Bound},
  year   = {2025},
  month  = aug,
  publisher = {Zenodo},
  url    = {https://github.com/JAMTUPAY/paper4-entropy-neutron-stars}
}


Author


⸻

Author

Johann Anton Michael Tupay
London, United Kingdom
Contact: jamtupay@icloud.com
ORCID: 0009-0008-7661-8698

⸻

License

MIT License — see LICENSE.
EOF


