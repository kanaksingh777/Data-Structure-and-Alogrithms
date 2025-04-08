#method overrding and method overloading
class PaymentMethod: 
    def __init__(self):
        pass
    def pay(self):
        pass
class CreditCard(PaymentMethod):
    def pay(self):
        print(f'paying with CreditCard')

class PayPal(PaymentMethod):
    def pay(self):
        print(f'paying with Paypal')

    # similarly for bitcoin

obj = [CreditCard(),PayPal()]
for i in obj:
    i.pay()