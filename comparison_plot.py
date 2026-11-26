"""Visualization helper for the version comparison_df results table."""

import matplotlib.pyplot as plt


def plot_comparison(comparison_df, target_percentage=80, show=True):
    """Plot the v1/v2 comparison in ``comparison_df``.

    Expected columns are ``Task``, ``Version``, ``Runs``, ``Unique Outputs``,
    ``Exact-Match Consistency (%)``, and ``Spec Pass Rate (%)``.
    """
    required_columns = {
        "Task", "Version", "Runs", "Unique Outputs",
        "Exact-Match Consistency (%)", "Spec Pass Rate (%)",
    }
    missing_columns = required_columns.difference(comparison_df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"comparison_df is missing required column(s): {missing}")
    if comparison_df.empty:
        raise ValueError("comparison_df must contain at least one row")

    tasks = comparison_df["Task"].astype(str).unique().tolist()
    versions = comparison_df["Version"].astype(str).unique().tolist()
    total_runs = int(comparison_df["Runs"].max())
    positions = list(range(len(tasks)))
    version_width = 0.8 / max(len(versions), 1)

    def values_for(column, task, version):
        rows = comparison_df.loc[
            (comparison_df["Task"].astype(str) == task)
            & (comparison_df["Version"].astype(str) == version),
            column,
        ]
        return rows.iloc[0] if not rows.empty else 0

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    colors = ["#4C78A8", "#F58518", "#54A24B", "#B279A2"]
    rate_colors = ["#4C78A8", "#F58518", "#54A24B", "#B279A2"]

    # Left panel: unique outputs by task and prompt version.
    unique_bars = []
    for version_index, version in enumerate(versions):
        values = [values_for("Unique Outputs", task, version) for task in tasks]
        offset = (version_index - (len(versions) - 1) / 2) * version_width
        unique_bars.extend(ax1.bar(
            [x + offset for x in positions], values, version_width,
            label=version, color=colors[version_index % len(colors)],
        ))

    ax1.axhline(total_runs, color="#E45756", linestyle="--", linewidth=1.2,
                label=f"Total Runs ({total_runs})")
    ax1.set_title("Unique Outputs by Prompt Version")
    ax1.set_ylabel("Number of Unique Outputs")
    ax1.set_xticks(positions)
    ax1.set_xticklabels(tasks)
    ax1.set_ylim(0, max(total_runs * 1.35,
                        comparison_df["Unique Outputs"].max() * 1.35))
    ax1.tick_params(axis="x", labelrotation=0)
    ax1.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.18),
        ncol=min(len(versions) + 1, 3),
        fontsize=8,
        frameon=True,
        fancybox=True,
        framealpha=0.95,
        borderpad=0.6,
    )

    for bar in unique_bars:
        value = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            value + max(total_runs * 0.025, 0.25),
            f"{value:g}/{total_runs}",
            ha="center",
            va="bottom",
            fontsize=8,
            clip_on=False,
        )

    # Right panel: consistency and specification pass rates by version.
    consistency_bars = []
    spec_bars = []
    for version_index, version in enumerate(versions):
        exact_values = [values_for("Exact-Match Consistency (%)", task, version)
                        for task in tasks]
        spec_values = [values_for("Spec Pass Rate (%)", task, version)
                       for task in tasks]
        offset = (version_index - (len(versions) - 1) / 2) * version_width
        consistency_bars.extend(ax2.bar(
            [x + offset - version_width * 0.2 for x in positions],
            exact_values, version_width * 0.4, label=f"{version} consistency",
            color=rate_colors[(version_index * 2) % len(rate_colors)],
        ))
        spec_bars.extend(ax2.bar(
            [x + offset + version_width * 0.2 for x in positions],
            spec_values, version_width * 0.4, label=f"{version} spec pass rate",
            color=rate_colors[(version_index * 2 + 1) % len(rate_colors)],
        ))

    ax2.axhline(target_percentage, color="#54A24B", linestyle="--",
                linewidth=1.2, label=f"{target_percentage:g}% Target")
    ax2.set_title("Consistency & Spec Pass Rates")
    ax2.set_ylabel("Percentage (%)")
    ax2.set_xticks(positions)
    ax2.set_xticklabels(tasks)
    max_rate = max(
        comparison_df["Exact-Match Consistency (%)"].max(),
        comparison_df["Spec Pass Rate (%)"].max(),
        target_percentage,
    )
    ax2.set_ylim(0, max(110, max_rate + 12))
    ax2.tick_params(axis="x", labelrotation=0)
    ax2.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.18),
        ncol=2,
        fontsize=8,
        frameon=True,
        fancybox=True,
        framealpha=0.95,
        borderpad=0.6,
    )

    for bar in [*consistency_bars, *spec_bars]:
        value = bar.get_height()
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            value + 1,
            f"{value:.1f}%",
            ha="center",
            va="bottom",
            rotation=0,
            fontsize=6,
            clip_on=False,
        )

    fig.suptitle(
        f"TechFlow Solutions — {total_runs}-Run Prompt Version Comparison",
        fontsize=12, fontweight="bold", y=0.94,
    )
    # Keep the legends outside the axes while using a compact overall layout.
    fig.tight_layout(rect=[0.01, 0.02, 0.99, 0.90], pad=0.6, w_pad=1.4, h_pad=0.6)

    if show:
        plt.show()

    # Do not return the dataframe or any other displayable table object; this
    # keeps the notebook output limited to the single table already displayed
    # by the calling cell plus the chart.
    return None
