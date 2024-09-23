"""Payriff üçün sorğular

Test kard məlumatları:

5239151747183468
11/24
292
"""

import os
from typing import Optional
from warnings import warn

from dotenv import load_dotenv

load_dotenv()

PAYRIFF_SECRET_KEY: str = os.getenv('PAYRIFF_SECRET_KEY', '')
PAYRIFF_MERCHANT_ID: str = os.getenv('PAYRIFF_MERCHANT_ID', '')

PAYRIFF_SUCCESS_REDIRECT_URL: Optional[str] = os.getenv('PAYRIFF_SUCCESS_REDIRECT_URL')
PAYRIFF_FAILED_REDIRECT_URL: Optional[str] = os.getenv('PAYRIFF_FAILED_REDIRECT_URL')
PAYRIFF_CANCELED_REDIRECT_URL: Optional[str] = os.getenv('PAYRIFF_CANCELED_REDIRECT_URL')

PAYRIFF_LOGGER_NAME: str = os.getenv('PAYRIFF_LOGGER_NAME', 'payriff')


if not PAYRIFF_SECRET_KEY or not PAYRIFF_MERCHANT_ID:
    warn('set PAYRIFF_SECRET_KEY/PAYRIFF_MERCHANT_ID env variables to use this library correctly')
