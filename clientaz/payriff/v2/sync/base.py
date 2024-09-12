from typing import Any

from clientaz.base import RequestType, SyncApiRequest
from clientaz.payriff import PAYRIFF_LOGGER_NAME, PAYRIFF_MERCHANT_ID, PAYRIFF_SECRET_KEY


class PayriffV2Request(SyncApiRequest[RequestType]):
    """Payriff sorğular üçün baza class (v2)"""

    def __init__(self):
        super().__init__('Payriff', PAYRIFF_LOGGER_NAME)

        self.base_url = 'https://api.payriff.com/api/v2/'
        self.headers['Authorization'] = PAYRIFF_SECRET_KEY
        self.body_data: dict = {}

    def __call__(self, *args: Any, **kwds: Any):
        if self.body_data:
            self.body = {'body': self.body_data, 'merchant': PAYRIFF_MERCHANT_ID}

        return super().__call__(*args, **kwds)
