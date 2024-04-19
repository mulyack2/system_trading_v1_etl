import pandas as pd
from tqdm import tqdm


class FdrExtractor:
    def __init__(self, fdr_broker) -> None:
        self.broker = fdr_broker

    def extract_krx_df(self):
        krx_df = self.broker.fdr.StockListing("KRX")
        return krx_df

    def extract_single_ohlcv_df(self, stock_code, start_date, end_date):
        single_ohlcv_df = self.broker.fdr.DataReader(
            symbol=stock_code, start=start_date, end=end_date
        )
        single_ohlcv_df["stock_code"] = stock_code
        return single_ohlcv_df

    def extract_multi_ohlcv_df(self, stock_codes, start_date, end_date):
        ohlcv_list = list()
        for stock_code in tqdm(stock_codes):
            try:
                single_ohlcv_df = self.extract_single_ohlcv_df(
                    stock_code, start_date, end_date
                )
                single_ohlcv_df["stock_code"] = stock_code
                ohlcv_list.append(single_ohlcv_df)
            except:
                print(stock_code)
        ohlcvs = pd.concat(ohlcv_list, axis=0)
        return ohlcvs
