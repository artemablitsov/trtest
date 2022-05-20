import ast
import pandas as pd
import numpy as np


def make_df(input_data) -> object:
    """
    Convert string format "{{'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}" to Pandas dataframe
    test str {{'time_delta': [0], 'segment': [0], 'order_time_delta': [0], 'distance':  [0], 'std_time_by_segment': [0], 'days_to_next_repair': [0], 'years_to_expiration':  [0], 'log_time_delta': [0]}
    """

    col_type = {'time_delta':           np.int16,
                'segment':              np.int32,
                'order_time_delta':     np.float16,
                'distance':             np.float16,
                'std_time_by_segment':  np.float16,
                'days_to_next_repair':  np.float16,
                'years_to_expiration':  np.float16,
                'log_time_delta':       np.float16,
                }
    try:
        df = pd.DataFrame.from_dict(ast.literal_eval(input_data))

        for col in df.columns:
            df[col] = df[col].astype(col_type[col])
    except IOError as e:
        print("I couldn't understand input data", e)

    return df
