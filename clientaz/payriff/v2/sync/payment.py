from decimal import Decimal
from typing import Optional

from clientaz.payriff.schemas.types import PayriffMinimalResponse
from clientaz.payriff.v2.sync.base import PayriffV2Request


class PayriffAutoPay(PayriffV2Request[PayriffMinimalResponse]):
    def __init__(
        self,
        amount: Decimal,
        card_id: str,
        order_id: str,
        session_id: str,
        description: Optional[str] = None,
    ):
        super().__init__()

        self.body_data.update(
            {
                'amount': amount,
                'cardUuid': card_id,
                'orderId': order_id,
                'sessionId': session_id,
            }
        )

        if description:
            self.body_data['description'] = description
