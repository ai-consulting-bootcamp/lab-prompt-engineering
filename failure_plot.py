"""Visualization helpers for the failure-analysis results."""

import matplotlib.pyplot as plt


def plot_failure_analysis(failure_df, ax=None, show=True):
    """Plot consistency and production-spec pass rates from ``failure_df``.

    Parameters
    ----------
    failure_df : pandas.DataFrame
        DataFrame containing ``Task``, ``Exact-Match Consistency (%)``, and
        ``Production Spec Pass Rate (%)`` columns.
    ax : matplotlib.axes.Axes, optional
        Existing axes to draw on. If omitted, new axes are created.
    show : bool, default=True
        Call ``plt.show()`` to render the graph inline in a notebook.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the graph.
    """
    required_columns = {
        "Task",
        "Exact-Match Consistency (%)",
        "Production Spec Pass Rate (%)",
    }
    missing_columns = required_columns.difference(failure_df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"failure_df is missing required column(s): {missing}")

    chart_df = failure_df.set_index("Task")[
        ["Exact-Match Consistency (%)", "Production Spec Pass Rate (%)"]
    ]

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 6))

    chart_df.plot(
        kind="bar",
        ax=ax,
        color=["#4C78A8", "#F58518"],
        edgecolor="white",
    )
    ax.set_title("Baseline Prompt Reliability Across 15 Runs")
    ax.set_xlabel("Task")
    ax.set_ylabel("Percentage")
    ax.set_ylim(0, 100)
    ax.legend(
        ["Exact-match consistency", "Production-spec pass rate"],
        loc="upper right",
    )
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.tick_params(axis="x", rotation=0)
    ax.figure.tight_layout()

    if show:
        plt.show()

    return ax

