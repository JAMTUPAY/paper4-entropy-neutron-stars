import pandas as pd, matplotlib.pyplot as plt, glob, os
from scipy.interpolate import interp1d
import numpy as np
plt.rcParams["font.family"]="serif"
colors = {"08.00":"#766CDB","09.81":"#DA847C","12.00":"#D9CC8B"}
fig, ax = plt.subplots(figsize=(12,9))
for path in sorted(glob.glob("data/lambda_vs_mass_*.csv")):
    cap = os.path.basename(path).split("_")[3].replace("kB.csv","")
    df = pd.read_csv(path).sort_values("mass_solar")
    ax.plot(df["mass_solar"], df["Lambda"], lw=3, label=f"S ≤ {cap} kB",
            color=colors.get(cap,"#333333"))
    if df["mass_solar"].min()<=1.4<=df["mass_solar"].max():
        f = interp1d(df["mass_solar"], df["Lambda"], bounds_error=False, fill_value="extrapolate")
        lam = float(f(1.4))
        ax.plot(1.4, lam, "o", ms=10, color=colors.get(cap,"#333333"), mec="white", mew=2)
ax.set_yscale("log"); ax.grid(True, which="both", alpha=0.3)
ax.set_xlabel("Mass ($M_\\odot$)"); ax.set_ylabel("Tidal Deformability $\\Lambda$")
ax.set_title("Tidal Deformability vs Mass (entropy caps)")
ax.legend()
plt.tight_layout(); plt.savefig("figures/appendix_fig_a1.png", dpi=300); plt.close()
print("[OK] figures/appendix_fig_a1.png")
