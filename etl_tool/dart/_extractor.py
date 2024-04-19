import requests
import pandas as pd


class DartFssExtractor:
    def __init__(self, dart_fss_broker) -> None:
        self.broker = dart_fss_broker

    def extract_corp_df(self):
        corp_list = self.broker.dart_fss.get_corp_list()
        corp_df = pd.DataFrame([corp.info for corp in corp_list])
        return corp_df


class DartApiExtractor:
    def __init__(self, dart_api_broker) -> None:
        self.broker = dart_api_broker

    def extract_single_fundamental_df(self, corp_code, bsns_year, reprt_code):
        try:
            single_fundamental_df = self._extract_progress(
                "fnlttSinglAcnt.json", corp_code, bsns_year, reprt_code
            )
            return single_fundamental_df
        except:
            return None

    def extract_multi_fundamental_df(self, corp_codes, bsns_year, reprt_code):
        try:
            chunked_corp_codes = self.__get_chunked_list(corp_codes, 99)
            multi_fundamental_df = pd.concat(
                [
                    self._extract_progress(
                        "fnlttMultiAcnt.json",
                        ",".join(chunked_corp_code),
                        bsns_year,
                        reprt_code,
                    )
                    for chunked_corp_code in chunked_corp_codes
                ],
                axis=0,
            )
            return multi_fundamental_df
        except:
            return None

    def _extract_progress(self, theme, corp_code, bsns_year, reprt_code):
        url = self.broker.get_formed_url(theme)
        params = self.broker.get_formed_params(
            corp_code=corp_code, bsns_year=bsns_year, reprt_code=reprt_code
        )
        resp = self.__extract_data(url, params)
        resp_df = self.__resp2df(resp)
        return resp_df

    def __extract_data(self, url, params):
        resp = requests.get(url=url, params=params)
        return resp

    @staticmethod
    def __resp2df(resp):
        if resp.status_code == 200:
            return pd.DataFrame(resp.json()["list"])
        else:
            return {"error_code": resp.status_code}

    @staticmethod
    def __get_chunked_list(_list: list, n: int):
        return [_list[i : i + n] for i in range(0, len(_list), n)]
