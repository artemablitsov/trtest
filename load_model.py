import joblib
import os

import sklearn

def load_model(name:str) -> object:
    """loads a guaranteed existing model from a directory. """

    models_dir = os.path.join(".", "binary")

    try:
        with open(os.path.join(models_dir, name), 'rb') as fo:
            model = joblib.load(fo)
    except Exception as e:
        #TODO: add logging
        print("I'm fall because of", e)

    return model
