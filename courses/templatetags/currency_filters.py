from django import template

register = template.Library()

@register.filter
def usd_to_inr(value):
    """Convert USD to INR (1 USD = 83 INR approximately)"""
    try:
        return round(float(value) * 83, 2)
    except:
        return value
