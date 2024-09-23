from integrify.payriff.schemas.types import PayriffMinimalResponse
from integrify.payriff.v2.asyncio.base import PayriffV2Request
from integrify.payriff.v2.sync.invoice import PayriffCreateInvoice as SyncPayriffCreateInvoice
from integrify.payriff.v2.sync.invoice import PayriffGetInvoice as SyncPayriffGetInvoice


class PayriffCreateInvoice(PayriffV2Request[PayriffMinimalResponse], SyncPayriffCreateInvoice):
    """"""


class PayriffGetInvoice(PayriffV2Request[PayriffMinimalResponse], SyncPayriffGetInvoice):
    """"""
