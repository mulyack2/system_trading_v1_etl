import fredpy


class FredBroker:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        fredpy.api_key = api_key
        self.fredpy = fredpy

    class InterestRateBroker:
        us_bir = "DFF"
        us_dir = "IORB"
        us_lir = "DPRIME"

    class MonetaryBroker:
        us_m0 = "BOGMBASE"
        us_m1 = "WM1NS"
        us_m2 = "WM2NS"

    class EtcBroker:
        us_unemploy = "ICSA"
