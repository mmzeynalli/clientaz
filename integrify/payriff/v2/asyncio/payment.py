from integrify.payriff.schemas.types import PayriffMinimalResponse
from integrify.payriff.v2.asyncio.base import PayriffV2Request
from integrify.payriff.v2.sync.payment import PayriffAutoPay as SyncPayriffAutoPay


class PayriffAutoPay(PayriffV2Request[PayriffMinimalResponse], SyncPayriffAutoPay):
    """"""
