from PublicDataReader import Ecos


class EcosBroker:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.ecos = Ecos(api_key)

    class InterestRateBroker:
        """금리 관련 파라미터 저장"""

        # 기준금리 (base_interest_rate)
        k_bir = {
            "통계표코드": "722Y001",
            "주기": "M",
            "통계항목코드1": "0101000",
        }

        # 대출금리 (loan_interest_rate)
        k_lir = {
            "통계표코드": "121Y006",
            "주기": "M",
            "통계항목코드1": "BECBLA01",
        }

        # 예금금리 (deposit_interest_rate)
        k_dir = {
            "통계표코드": "121Y002",
            "주기": "M",
            "통계항목코드1": "BEABAA1",
        }

    class MonetaryBroker:
        """통화량 관련 파라미터 저장"""

        # 본원 통화
        k_m0 = {
            "통계표코드": "102Y004",
            "주기": "M",
            "통계항목코드1": "ABA1",
        }

        # 협의 통화
        k_m1 = {
            "통계표코드": "101Y018",
            "주기": "M",
            "통계항목코드1": "BBLS00",
        }

        # 광의 통화
        k_m2 = {
            "통계표코드": "101Y003",
            "주기": "M",
            "통계항목코드1": "BBHS00",
        }

    class EtcBroker:
        k_unemploy = {
            "통계표코드": "901Y084",
            "주기": "M",
            "통계항목코드1": "167A",
            "통계항목코드2": "P",
        }
