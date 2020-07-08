# Third-party library imports
import urllib.parse as encode

# Core Django imports
from django import template

register = template.Library()


@register.filter
def urlify(value):
    encode_url = encode.quote_plus(value)
    return encode_url

