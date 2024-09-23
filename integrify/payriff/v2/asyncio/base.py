from integrify.base import AsyncApiRequest, RequestType
from integrify.payriff.v2.sync.base import PayriffV2Request as SyncPayriffV2Request


class PayriffV2Request(AsyncApiRequest[RequestType], SyncPayriffV2Request):  # type: ignore[misc]
    """Payriff async sorğular üçün baza class (v2)"""
