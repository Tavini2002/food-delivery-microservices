from data_service import MenuMockDataService

class MenuService:
    def __init__(self):
        self.data = MenuMockDataService()

    def get_all(self):
        return self.data.get_all()

    def get_by_id(self, id):
        return self.data.get_by_id(id)

    def create(self, item):
        return self.data.add(item)

    def update(self, id, item):
        return self.data.update(id, item)

    def delete(self, id):
        return self.data.delete(id)