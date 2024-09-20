from clientaz.payriff.schemas.types import PayriffMinimalResponse
from clientaz.payriff.v2.asyncio.base import PayriffV2Request
from clientaz.payriff.v2.sync.payment import PayriffAutoPay as SyncPayriffAutoPay


class PayriffAutoPay(PayriffV2Request[PayriffMinimalResponse], SyncPayriffAutoPay):
    """"""
