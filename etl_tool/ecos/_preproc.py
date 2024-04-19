import pandas as pd


class EcosPreproc:
    @staticmethod
    def slice_columns(df):
        _df = df.loc[:, ["시점", "값"]]
        return _df

    @staticmethod
    def format_date(df, date_format):
        df["시점"] = pd.to_datetime(df["시점"], format=date_format)
        return df

    @staticmethod
    def add_arg(df, arg_name):
        df["arg_name"] = arg_name
        return df

    @staticmethod
    def rename_columns(df):
        df = df.rename(columns={"시점": "date", "값": "value"})
        return df

    def __call__(self, df, date_format, arg_name):
        _df = df.copy()
        _df = self.slice_columns(_df)
        _df = self.format_date(_df, date_format)
        _df = self.add_arg(_df, arg_name)
        _df = self.rename_columns(_df)
        _df.loc[:, ["arg_name", "date", "value"]]
        return _df
