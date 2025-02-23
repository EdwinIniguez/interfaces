from abc import ABC, abstractmethod

# Definición de la interfaz
class IPaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

# Implementaciones concretas
class CreditCardPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> None:
        print(f"Pago de {amount} realizado con Tarjeta de Crédito.")

class PayPalPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> None:
        print(f"Pago de {amount} realizado con PayPal.")

class BankTransferPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> None:
        print(f"Pago de {amount} realizado mediante Transferencia Bancaria.")

# Clase que usa la interfaz
class PaymentProcessor:
    def __init__(self, payment_method: IPaymentMethod):
        self.payment_method = payment_method

    def process(self, amount: float) -> None:
        self.payment_method.process_payment(amount)

# Prueba del sistema
if __name__ == "__main__":
    payment_method = CreditCardPayment()
    processor = PaymentProcessor(payment_method)
    processor.process(100.0)

    payment_method = PayPalPayment()
    processor = PaymentProcessor(payment_method)
    processor.process(200.0)