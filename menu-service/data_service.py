from models import MenuItem

class MenuMockDataService:
    def __init__(self):
        self.menu = [
            MenuItem(id=1, name="Burger", price=500, description="Chicken Burger"),
            MenuItem(id=2, name="Pizza", price=1200, description="Cheese Pizza"),
        ]
        self.next_id = 3

    def get_all(self):
        return self.menu

    def get_by_id(self, item_id):
        return next((m for m in self.menu if m.id == item_id), None)

    def add(self, item):
        new_item = MenuItem(id=self.next_id, **item.dict())
        self.menu.append(new_item)
        self.next_id += 1
        return new_item

    def update(self, item_id, item):
        menu_item = self.get_by_id(item_id)
        if menu_item:
            for key, value in item.dict(exclude_unset=True).items():
                setattr(menu_item, key, value)
            return menu_item
        return None

    def delete(self, item_id):
        item = self.get_by_id(item_id)
        if item:
            self.menu.remove(item)
            return True
        return False