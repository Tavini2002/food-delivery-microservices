from data_service import get_all_users, create_user

def fetch_users():
    return get_all_users()

def add_user(user):
    return create_user(user)