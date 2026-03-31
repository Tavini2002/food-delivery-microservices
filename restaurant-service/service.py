from data_service import RestaurantMockDataService

class RestaurantService:
    def __init__(self):
        self.ds = RestaurantMockDataService()

    def get_all(self):
        return self.ds.get_all()

    def get_by_id(self, id):
        return self.ds.get_by_id(id)

    def create(self, data):
        return self.ds.create(data)

    def update(self, id, data):
        return self.ds.update(id, data)

    def delete(self, id):
        return self.ds.delete(id)