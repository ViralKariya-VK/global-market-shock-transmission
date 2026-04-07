import numpy as np
import matplotlib.pyplot as plt

def plot_irf_relationship(
    vecm_fit,
    impulse: str,
    response: str,
    steps: int = 20,
    tolerance: float = 0.01
):
    """
    IRF plot focused on stabilization (new equilibrium)
    """

    irf = vecm_fit.irf(steps)

    variables = vecm_fit.names
    impulse_idx = variables.index(impulse)
    response_idx = variables.index(response)

    irf_values = irf.irfs[:, response_idx, impulse_idx]
    t = np.arange(len(irf_values))

    # -------- Find stabilization point --------
    stable_day = None
    for i in range(2, len(irf_values)):
        if abs(irf_values[i] - irf_values[i-1]) < tolerance:
            stable_day = i
            break

    # -------- Plot --------
    plt.figure(figsize=(12, 6))
    plt.plot(t, irf_values, linewidth=3)

    # Zero baseline
    plt.axhline(0, linestyle='--')

    # Initial impact
    plt.scatter(1, irf_values[1], s=80)
    plt.text(1, irf_values[1],
             f' Initial Impact\n{irf_values[1]:.3f}',
             fontsize=10)

    # Stabilization marker
    if stable_day:
        plt.axvline(stable_day, linestyle='--')
        plt.text(stable_day, max(irf_values)*0.8,
                 f'Stabilizes ≈ Day {stable_day}',
                 fontsize=11)

    plt.title(f"Shock Transmission & Stabilization: {impulse} → {response}",
              fontsize=15, fontweight='bold')

    plt.xlabel("Days after Shock")
    plt.ylabel("System Response")

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()