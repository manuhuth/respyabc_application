import pickle

import numpy as np
import pytask
import respy as rp
from respyabc.distances import compute_mean_squared_distance
from respyabc.models import compute_model
from respyabc.respyabc import respyabc

from src.config import BLD


@pytask.mark.produces(BLD / "analysis" / "run_delta_choice_frequencies.pickle")
def task_get_history_delta_choice_frequencies(produces):
    np.random.seed(123)
    params, options, data_stored = rp.get_example_model("kw_94_one")
    params.loc[("delta", "delta")]

    model_to_simulate = rp.get_simulate_func(params, options)
    parameter_true = {"delta_delta": 0.95}

    pseudo_observed_data = compute_model(
        parameter_true,
        model_to_simulate=model_to_simulate,
        parameter_for_simulation=params,
        options_for_simulation=options,
        descriptives="choice_frequencies",
    )

    population_size = 2
    max_nr_populations = 2
    minimum_epsilon = 0.05
    delta_prior_low = 0.9
    delta_prior_length = 0.09
    parameters_prior = {"delta_delta": [delta_prior_low, delta_prior_length]}

    history = respyabc(
        model=compute_model,
        parameters_prior=parameters_prior,
        data=pseudo_observed_data,
        distance_abc=compute_mean_squared_distance,
        descriptives="choice_frequencies",
        population_size_abc=population_size,
        max_nr_populations_abc=max_nr_populations,
        minimum_epsilon_abc=minimum_epsilon,
    )
    with open(produces, "wb") as out_file:
        pickle.dump(history, out_file)


# split up in 2 tasks since one run takes very long
@pytask.mark.produces(BLD / "analysis" / "run_delta_wage_moments.pickle")
def task_get_history_delta_wage_moments(produces):
    np.random.seed(123)
    params, options, data_stored = rp.get_example_model("kw_94_one")
    params.loc[("delta", "delta")]

    model_to_simulate = rp.get_simulate_func(params, options)
    parameter_true = {"delta_delta": 0.95}

    pseudo_observed_data = compute_model(
        parameter_true,
        model_to_simulate=model_to_simulate,
        parameter_for_simulation=params,
        options_for_simulation=options,
        descriptives="wage_moments",
    )

    population_size = 2
    max_nr_populations = 2
    minimum_epsilon = 0.05
    delta_prior_low = 0.9
    delta_prior_length = 0.09
    parameters_prior = {"delta_delta": [delta_prior_low, delta_prior_length]}

    history = respyabc(
        model=compute_model,
        parameters_prior=parameters_prior,
        data=pseudo_observed_data,
        distance_abc=compute_mean_squared_distance,
        descriptives="wage_moments",
        population_size_abc=population_size,
        max_nr_populations_abc=max_nr_populations,
        minimum_epsilon_abc=minimum_epsilon,
    )
    with open(produces, "wb") as out_file:
        pickle.dump(history, out_file)
