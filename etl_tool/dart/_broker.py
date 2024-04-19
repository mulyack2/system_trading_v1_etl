import os
import dart_fss


class DartFssBroker:
    """based on dart-fss"""

    def __init__(self, api_key) -> None:
        self.api_key = dart_fss.set_api_key(api_key)
        self.dart_fss = dart_fss


class DartApiBroker:
    """based on dart api"""

    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://opendart.fss.or.kr/api"

    def get_formed_url(self, theme):
        formed_url = os.path.join(self.base_url, theme)
        return formed_url
    
    def get_formed_params(self, **kwargs):
        params = {**kwargs}
        params['crtfc_key'] = self.api_key
        return params