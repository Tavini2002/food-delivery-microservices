from models import MenuItem

class MenuMockDataService:
    def __init__(self):
        self.menu = [
            MenuItem(id=1, name="Burger", price=500, description="Chicken Burger", category="Fast Food", size="Medium"),
            MenuItem(id=2, name="Pizza", price=1200, description="Cheese Pizza", category="Fast Food", size="Large"),
            MenuItem(id=3, name="Fried Rice", price=800, description="Seafood fried rice", category="Main Course", size="Large"),
            MenuItem(id=4, name="Kottu", price=900, description="Chicken kottu", category="Main Course", size="Large"),
            MenuItem(id=5, name="French Fries", price=400, description="Crispy fries", category="Snacks", size="Medium"),
            MenuItem(id=6, name="Coke", price=150, description="Chilled Coca Cola", category="Beverage", size="Small"),
            MenuItem(id=7, name="Milkshake", price=350, description="Chocolate milkshake", category="Beverage", size="Medium"),
            MenuItem(id=8, name="Pasta", price=950, description="Creamy chicken pasta", category="Main Course", size="Large"),
            MenuItem(id=9, name="Sandwich", price=450, description="Club sandwich", category="Snacks", size="Medium"),
            MenuItem(id=10, name="Ice Cream", price=300, description="Vanilla ice cream", category="Dessert", size="Small"),
            MenuItem(id=11, name="Grilled Chicken", price=1100, description="Herb-marinated grilled chicken", category="Main Course", size="Large"),
    MenuItem(id=12, name="Veg Burger", price=400, description="Vegetarian burger with lettuce and tomato", category="Fast Food", size="Medium"),
    MenuItem(id=13, name="Chocolate Cake", price=500, description="Rich chocolate cake slice", category="Dessert", size="Small"),
    MenuItem(id=14, name="Pepsi", price=150, description="Chilled Pepsi can", category="Beverage", size="Small"),
    MenuItem(id=15, name="Chicken Nuggets", price=600, description="Crispy chicken nuggets with sauce", category="Snacks", size="Medium"),
    MenuItem(id=16, name="Veg Fried Rice", price=700, description="Fried rice with mixed vegetables", category="Main Course", size="Large"),
    MenuItem(id=17, name="Garlic Bread", price=350, description="Toasted garlic bread sticks", category="Snacks", size="Medium"),
    MenuItem(id=18, name="Lemonade", price=200, description="Fresh lemonade", category="Beverage", size="Medium"),
    MenuItem(id=19, name="Paneer Tikka", price=850, description="Spicy grilled paneer cubes", category="Main Course", size="Large"),
    MenuItem(id=20, name="Brownie", price=300, description="Chocolate brownie with nuts", category="Dessert", size="Small"),
    MenuItem(id=21, name="Fish & Chips", price=950, description="Fried fish with crispy fries", category="Main Course", size="Large"),
    MenuItem(id=22, name="Veg Pizza", price=1100, description="Pizza with mixed vegetables and cheese", category="Fast Food", size="Large"),
    MenuItem(id=23, name="Chicken Wings", price=650, description="Spicy grilled chicken wings", category="Snacks", size="Medium"),
    MenuItem(id=24, name="Iced Coffee", price=250, description="Cold coffee with milk and ice", category="Beverage", size="Medium"),
    MenuItem(id=25, name="Mango Shake", price=350, description="Fresh mango milkshake", category="Beverage", size="Medium"),
    MenuItem(id=26, name="Cheeseburger", price=550, description="Burger with cheese slice", category="Fast Food", size="Medium"),
    MenuItem(id=27, name="Veg Kottu", price=800, description="Kottu with mixed vegetables", category="Main Course", size="Large"),
    MenuItem(id=28, name="Tiramisu", price=400, description="Coffee-flavored Italian dessert", category="Dessert", size="Small"),
    MenuItem(id=29, name="Masala Fries", price=450, description="Spicy seasoned fries", category="Snacks", size="Medium"),
    MenuItem(id=30, name="Chocolate Brownie Sundae", price=500, description="Brownie with ice cream", category="Dessert", size="Small"),
    MenuItem(id=31, name="Prawn Curry", price=1200, description="Spicy prawn curry with rice", category="Main Course", size="Large"),
    MenuItem(id=32, name="Veg Sandwich", price=400, description="Fresh vegetable sandwich with sauces", category="Snacks", size="Medium"),
    MenuItem(id=33, name="Orange Juice", price=200, description="Freshly squeezed orange juice", category="Beverage", size="Medium"),
    MenuItem(id=34, name="Cheese Pasta", price=900, description="Pasta with creamy cheese sauce", category="Main Course", size="Large"),
    MenuItem(id=35, name="Chocolate Muffin", price=250, description="Soft chocolate muffin", category="Dessert", size="Small"),
    MenuItem(id=36, name="Hotdog", price=450, description="Classic hotdog with mustard and ketchup", category="Fast Food", size="Medium"),
    MenuItem(id=37, name="Chicken Biryani", price=1000, description="Spiced chicken biryani with raita", category="Main Course", size="Large"),
    MenuItem(id=38, name="Vanilla Latte", price=300, description="Espresso with steamed milk and vanilla syrup", category="Beverage", size="Medium"),
    MenuItem(id=39, name="Cheese Nachos", price=550, description="Nachos topped with melted cheese and salsa", category="Snacks", size="Medium"),
    MenuItem(id=40, name="Strawberry Ice Cream", price=300, description="Strawberry flavored ice cream", category="Dessert", size="Small"),
        ]
        self.next_id = 11
    
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