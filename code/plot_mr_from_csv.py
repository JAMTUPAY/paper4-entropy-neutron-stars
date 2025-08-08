import pandas as pd, matplotlib.pyplot as plt, glob, os
plt.rcParams["font.family"]="serif"
colors = {"08.00":"#766CDB","09.81":"#DA847C","12.00":"#D9CC8B"}
for path in sorted(glob.glob("data/mass_radius_results_*.csv")):
    cap = os.path.basename(path).split("_")[3].replace("kB.csv","")
    df = pd.read_csv(path)
    fig, ax = plt.subplots(figsize=(9,6))
    ax.plot(df["R_km"], df["M_solar"], lw=3, color=colors.get(cap,"#333333"),
            label=f"S ≤ {cap} kB")
    ax.set_xlabel("Radius (km)"); ax.set_ylabel("Mass ($M_\\odot$)")
    ax.set_title(f"Mass–Radius (S ≤ {cap} kB)"); ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    out = f"figures/mass_radius_curve_{cap}kB.png"
    plt.tight_layout(); plt.savefig(out, dpi=300); plt.close()
    print("[OK]", out)
