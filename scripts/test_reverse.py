import json_scorer as jscore
import os


def test_reverse_scoring(simple_data):
    # unpack simple_data
    surv_data, input_path, solutions = simple_data
    sol_cols = list(solutions.columns)
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data)

    for index, row in output_data.iterrows():
        for name in sol_cols:
            assert row[name] == solutions.loc[index][name]
