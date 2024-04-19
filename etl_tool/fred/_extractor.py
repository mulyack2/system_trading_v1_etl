from functools import wraps
from dateutil.relativedelta import relativedelta


def datetime2string(func):
    @wraps(func)
    def wrapper(self, date, *args, **kwargs):
        def _formatter(date):
            _date = date - relativedelta(day=1)
            formmated_date = _date.strftime("%Y-%m-%d")
            return formmated_date

        formmated_date = _formatter(date)
        return func(self, formmated_date, *args, **kwargs)

    return wrapper


class FredExtractor:
    def __init__(self, fred_broker) -> None:
        self.broker = fred_broker

    @datetime2string
    def extract_us_bir_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.InterestRateBroker.us_bir, end_date
        )
        return resp_obj.data

    @datetime2string
    def extract_us_dir_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.InterestRateBroker.us_dir, end_date
        )
        return resp_obj.data

    @datetime2string
    def extract_us_lir_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.InterestRateBroker.us_lir, end_date
        )
        return resp_obj.data

    @datetime2string
    def extract_us_m0_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.MonetaryBroker.us_m0, end_date
        )
        return resp_obj.data

    @datetime2string
    def extract_us_m1_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.MonetaryBroker.us_m1, end_date
        )
        return resp_obj.data

    @datetime2string
    def extract_us_m2_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.MonetaryBroker.us_m2, end_date
        )
        return resp_obj.data

    @datetime2string
    def extract_us_unemploy_df(self, end_date):
        resp_obj = self.broker.fredpy.series(
            self.broker.EtcBroker.us_unemploy, end_date
        )
        return resp_obj.data
