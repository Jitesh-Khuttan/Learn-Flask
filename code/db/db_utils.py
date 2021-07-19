
def validate_params_for_executemany(params):
    if params is None:
        raise Value("params can't be None when trying to do execute many.")

    if not isinstance(params, (list, tuple, set)):
        raise ValueError("Query params should be of type - tuple, list or a set of parameters.")
    params = [params] if isinstance(params, tuple) else list(params)
    return params
