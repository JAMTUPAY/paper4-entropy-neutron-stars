#!/usr/bin/env bash
set -e
echo "[run_all] Regenerating plots from CSVs in ./data ..."
python code/plot_mr_from_csv.py
python code/plot_lambda_from_csv.py
echo "[run_all] Done. Figures in ./figures"
