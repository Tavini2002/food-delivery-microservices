from models import Payment

class PaymentMockDataService:
    def __init__(self):
        self.payments = [
            Payment(id=1, amount=100.0, status="completed"),
            Payment(id=2, amount=250.5, status="pending"),
            Payment(id=3, amount=75.0, status="completed"),
            Payment(id=4, amount=500.0, status="pending"),
            Payment(id=5, amount=150.75, status="failed"),
        ]
        self.next_id = 6

    def get_all(self):
        return self.payments

    def get_by_id(self, id):
        for payment in self.payments:
            if payment.id == id:
                return payment
        return None

    def add(self, payment_data):
        new_payment = Payment(
            id=self.next_id,
            amount=payment_data.amount,
            status=payment_data.status
        )
        self.payments.append(new_payment)
        self.next_id += 1
        return new_payment

    def update(self, id, payment_data):
        payment = self.get_by_id(id)
        if not payment:
            return None
        
        if payment_data.amount is not None:
            payment.amount = payment_data.amount
        if payment_data.status is not None:
            payment.status = payment_data.status
        
        return payment

    def delete(self, id):
        for i, payment in enumerate(self.payments):
            if payment.id == id:
                self.payments.pop(i)
                return True
        return False
