from data_service import PaymentMockDataService

class PaymentService:
    def __init__(self):
        self.data = PaymentMockDataService()

    def get_all(self):
        return self.data.get_all()

    def get_by_id(self, id):
        return self.data.get_by_id(id)

    def create(self, payment):
        return self.data.add(payment)

    def update(self, id, payment):
        return self.data.update(id, payment)

    def delete(self, id):
        return self.data.delete(id)
