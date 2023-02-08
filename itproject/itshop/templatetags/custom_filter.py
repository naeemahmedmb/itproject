from django import template

register=template.Library()

@register.filter(name='currency')
def currency(num):
    return 'TAKA ' + str(num)


@register.filter(name='discount')
def discount(num):
    return 'Discount: ' + str(num) + '%'


@register.filter(name='price')
def price(num, num1):
    pr=num1- (num1*num/100)
    return 'Price: ' + str(pr) + 'Tk.'