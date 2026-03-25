from models import Restaurant

class RestaurantMockDataService:
    def __init__(self):
        self.restaurants = []
        self.next_id = 1

    def get_all(self):
        return self.restaurants

    def get_by_id(self, id):
        return next((r for r in self.restaurants if r.id == id), None)

    def create(self, data):
        new = Restaurant(id=self.next_id, **data.dict())
        self.restaurants.append(new)
        self.next_id += 1
        return new

    def update(self, id, data):
        r = self.get_by_id(id)
        if r:
            for k, v in data.dict(exclude_unset=True).items():
                setattr(r, k, v)
            return r
        return None

    def delete(self, id):
        r = self.get_by_id(id)
        if r:
            self.restaurants.remove(r)
            return True
        return False