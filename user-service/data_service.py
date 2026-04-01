from models import User

users = []

def get_all_users():
    return users

def create_user(user: User):
    users.append(user)
    return user