import pickle

import matplotlib.pyplot as plt
import pytask
from respyabc.evaluation import plot_kernel_density_posterior

from src.config import BLD


specifications = (
    (
        BLD / "analysis" / f"run_{model_name}.pickle",
        BLD / "figures" / f"plot_{model_name}_kernel_density.png",
    )
    for model_name in ["delta_choice_frequencies", "delta_wage_moments"]
)


@pytask.mark.parametrize("depends_on, produces", specifications)
def task_plot_kernel_density(depends_on, produces):
    # Load locations after each round
    with open(depends_on, "rb") as f:
        history = pickle.load(f)

    plot_kernel_density_posterior(
        history=history, parameter="delta_delta", xmin=0.9, xmax=0.99
    )
    plt.savefig(produces)
