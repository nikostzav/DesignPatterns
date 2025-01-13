
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement the process_payment method")


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.process_payment(amount)


if __name__ == "__main__":
  
    credit_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

  
    print("Credit Card Payment:")
    processor = PaymentProcessor(credit_payment)
    processor.make_payment(100)

 
    print("\nPayPal Payment:")
    processor = PaymentProcessor(paypal_payment)
    processor.make_payment(200)
