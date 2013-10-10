from datetime import datetime
from decimal import Decimal


TYPE_CODES = {
    'datetime': '_m\x01',
    'decimal': '_m\x02',
}


def msgxdec(has_datetime=True, has_decimal=False):
    def dec(obj):
        if has_datetime and TYPE_CODES['datetime'] in obj:
            return datetime(*obj['d'])
        elif has_decimal and TYPE_CODES['decimal'] in obj:
            return Decimal(obj['d'])
        return obj
    return dec


def msgxenc(has_datetime=True, has_decimal=False):
    def enc(obj):
        if has_datetime and isinstance(obj, datetime):
            return {TYPE_CODES['datetime']: True, 'd': (obj.year, obj.month, obj.day, obj.hour, obj.minute, obj.second, obj.microsecond,)}
        elif has_decimal and isinstance(obj, Decimal):
            return {TYPE_CODES['decimal']: True, 'd': tuple(obj.as_tuple())}
        return obj
    return enc
