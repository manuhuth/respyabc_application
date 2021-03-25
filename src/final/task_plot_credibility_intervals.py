import pickle

import matplotlib.pyplot as plt
import pytask
from respyabc.evaluation import plot_credible_intervals

from src.config import BLD


specifications = (
    (
        BLD / "analysis" / f"run_{model_name}.pickle",
        BLD / "figures" / f"plot_{model_name}_credibility_intervals.png",
    )
    for model_name in ["delta_choice_frequencies", "delta_wage_moments"]
)


@pytask.mark.parametrize("depends_on, produces", specifications)
def task_plot_credibility_intervals(depends_on, produces):
    # Load locations after each round
    with open(depends_on, "rb") as f:
        history = pickle.load(f)

    plot_credible_intervals(
        history=history,
        parameter="delta_delta",
        interval_type="simulated",
        alpha=0.05,
        main_title="",
        y_label="delta",
    )
    plt.savefig(produces)
