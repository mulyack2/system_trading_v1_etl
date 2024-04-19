class FredPreproc:

    def __call__(self, df, arg_name):
        _df = df.copy()
        _df = _df.reset_index()
        _df["arg_name"] = arg_name
        _df = _df.loc[:, ["date", "value", "arg_name"]]
        return _df
