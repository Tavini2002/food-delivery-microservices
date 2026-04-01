from models import Order

class OrderMockDataService:
    def __init__(self):
        self.orders = []
        self.next_id = 1

    def get_all(self):
        return self.orders

    def get_by_id(self, id):
        return next((o for o in self.orders if o.id == id), None)

    def create(self, data):
        new = Order(
            id=self.next_id,
            user_id=data.user_id,
            restaurant_id=data.restaurant_id,
            items=data.items,
            status="PENDING"
        )
        self.orders.append(new)
        self.next_id += 1
        return new

    def update(self, id, data):
        o = self.get_by_id(id)
        if o:
            for k, v in data.dict(exclude_unset=True).items():
                setattr(o, k, v)
            return o
        return None

    def delete(self, id):
        o = self.get_by_id(id)
        if o:
            self.orders.remove(o)
            return True
        return False