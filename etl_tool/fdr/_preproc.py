class FdrOhlcvPreproc:

    def __call__(self, df):
        _df = df.copy()
        _df.reset_index(inplace=True)
        _df.columns = [col.lower() for col in _df.columns]
        _df = _df.loc[:,["stock_code", "open", "high", "low", "close", "volume", "change", "date"]]
        return _df
