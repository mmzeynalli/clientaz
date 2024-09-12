from clientaz.base import RequestType, SyncApiRequest
from clientaz.payriff import PAYRIFF_LOGGER_NAME, PAYRIFF_SECRET_KEY


class PayriffV3Request(SyncApiRequest[RequestType]):
    """Payriff sorğular üçün baza class (v3)"""

    def __init__(self):
        super().__init__('Payriff', PAYRIFF_LOGGER_NAME)

        self.base_url = 'https://api.payriff.com/api/v3/'
        self.headers['Authorization'] = PAYRIFF_SECRET_KEY
