from dateutil.relativedelta import relativedelta
from functools import wraps


def monthly_extractor(func):
    """
    Ex) 2023-12-20 -> 202311
    """

    @wraps(func)
    def wrapper(self, start_date, end_date, *arg, **kwargs):
        def _monthly_formatter(date):
            _date = date - relativedelta(months=1)
            formmated_date = _date.strftime("%Y%m")
            return formmated_date

        formmated_start_date = _monthly_formatter(start_date)
        formmated_end_date = _monthly_formatter(end_date)
        return func(
            self, formmated_start_date, formmated_end_date, *arg, **kwargs
        )

    return wrapper


def daily_extractor(func):
    """
    Ex)2023-12-20 -> 20231219
    """

    @wraps(func)
    def wrapper(self, start_date, end_date, *arg, **kwargs):
        def _daily_formatter(date):
            _date = date - relativedelta(days=1)
            formmated_date = _date.strftime("%Y%m%d")
            return formmated_date

        formmated_start_date = _daily_formatter(start_date)
        formmated_end_date = _daily_formatter(end_date)
        return func(
            self, formmated_start_date, formmated_end_date, *arg, **kwargs
        )

    return wrapper


class EcosExtractor:
    def __init__(self, ecos_broker) -> None:
        self.broker = ecos_broker

    @monthly_extractor
    def extract_k_bir_df(self, start_date, end_date):
        """한국 기준금리"""
        params = self.broker.InterestRateBroker.k_bir
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    @monthly_extractor
    def extract_k_lir_df(self, start_date, end_date):
        """한국 대출금리"""
        params = self.broker.InterestRateBroker.k_lir
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    @monthly_extractor
    def extract_k_dir_df(self, start_date, end_date):
        """한국 예금금리"""
        params = self.broker.InterestRateBroker.k_dir
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    @monthly_extractor
    def extract_k_m0_df(self, start_date, end_date):
        """한국 본원통화"""
        params = self.broker.MonetaryBroker.k_m0
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    @monthly_extractor
    def extract_k_m1_df(self, start_date, end_date):
        """한국 협의통화"""
        params = self.broker.MonetaryBroker.k_m1
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    @monthly_extractor
    def extract_k_m2_df(self, start_date, end_date):
        """한국 광의통화"""
        params = self.broker.MonetaryBroker.k_m2
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    @monthly_extractor
    def extract_k_unemploy_df(self, start_date, end_date):
        """한국 실업수당건수"""
        params = self.broker.EtcBroker.k_unemploy
        params["검색시작일자"] = start_date
        params["검색종료일자"] = end_date
        data = self.__extract_with_params(params)
        return data

    def __extract_with_params(self, params):
        data = self.broker.ecos.get_statistic_search(**params)
        return data
