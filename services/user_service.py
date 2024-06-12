from repositories import user_repository
from utils.validation_util import validate_username_exists_in_database, validate_username_length


def get_user(username):
    validate_username_exists_in_database(username)

    return user_repository.get_user(username)


def create_user_profile(username, first_name, last_name, current_password):
    if not validate_username_exists_in_database(username):
        return None
    validate_username_length(username)
    return user_repository.create_user_profile(username, first_name, last_name, current_password)


def change_password(username, current_password, new_password):
    validate_username_exists_in_database(username)

    if new_password == current_password:
        return None

    return user_repository.change_password(username=username, new_password=new_password)

