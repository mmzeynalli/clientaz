from integrify.base import AsyncApiRequest, RequestType
from integrify.payriff.v3.sync.base import PayriffV3Request as SyncPayriffV3Request


class PayriffV3Request(AsyncApiRequest[RequestType], SyncPayriffV3Request):  # type: ignore[misc]
    """Payriff async sorğular üçün baza class (v3)"""
