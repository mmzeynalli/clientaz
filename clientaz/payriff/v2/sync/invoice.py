from datetime import datetime
from decimal import Decimal
from typing import Optional

from clientaz.payriff.schemas.types import PayriffMinimalResponse
from clientaz.payriff.v2.sync.base import PayriffV2Request


class PayriffCreateInvoice(PayriffV2Request[PayriffMinimalResponse]):
    """"""

    def __init__(
        self,
        amount: Decimal,
        currency: str,
        expire_date: datetime | str,
        full_name: str,
        installment_period: int,
        installment_product_type: str,
        message: str,
        lang: Optional[str] = 'az',
        email: Optional[str] = None,
        phone: Optional[str] = None,
        send_sms: Optional[bool] = False,
        send_whatsapp: Optional[bool] = False,
        send_email: Optional[bool] = True,
        is_amount_dynamic: Optional[bool] = False,
        is_direct_pay: Optional[bool] = False,
        description: Optional[str] = None,
    ):
        """
        Args:
            amount: Invoice amount.
            currency: Invoice currency. e.g. AZN, USD, EUR.
            expire_date: Invoice expire date. This date should be in UTC.
            full_name: Customer full name.
            installment_period: Installment period.
            installment_product_type: Installment product type. e.g. credit_card.
            message: Invoice message.
            lang: Invoice language. e.g. az, en, ru. Default is az.
            email: Customer email. Used for sending invoice by email.
            phone: Customer phone. Used for sending invoice by SMS or WhatsApp.
            send_sms: Send invoice by SMS.
            send_whatsapp: Send invoice by WhatsApp.
            send_email: Send invoice by email.
            is_amount_dynamic: Is amount dynamic?
            is_direct_pay: Is direct pay?
            description: Invoice description.
        """
        super().__init__()

        self.path = 'invoices'
        self.verb = 'POST'

        if not phone and (send_sms or send_whatsapp):
            raise ValueError('Phone must be provided if send_sms or send_whatsapp is True')

        if not email and send_email:
            raise ValueError('Email must be provided if send_email is True')

        if isinstance(expire_date, datetime):
            expire_date = expire_date.isoformat()

        self.body_data.update(
            {
                'amount': amount,
                'currencyType': currency,
                'customMessage': message,
                'expireDate': expire_date,
                'fullName': full_name,
                'installmentPeriod': installment_period,
                'installmentProductType': installment_product_type,
                'languageType': lang,
                'sendSms': send_sms,
                'sendWhatsapp': send_whatsapp,
                'sendEmail': send_email,
                'amountDynamic': is_amount_dynamic,
                'directPay': is_direct_pay,
            }
        )

        if email:
            self.body_data['email'] = email

        if phone:
            self.body_data['phone'] = phone

        if description:
            self.body_data['description'] = description


class PayriffGetInvoice(PayriffV2Request[PayriffMinimalResponse]):
    def __init__(self, invoice_id: str):
        """
        Args:
            invoice_id: Invoice ID.
        """

        super().__init__()

        self.path = '/get-invoice'
        self.verb = 'POST'

        self.body_data['uuid'] = invoice_id
