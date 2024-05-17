from repositories import user_repository
from utils.validation_util import validate_username_exists_in_database, validate_username_length


def get_user(username):
    validate_username_exists_in_database(username)

    return user_repository.get_user(username)


def create_user_profile(username, first_name, last_name, password):
    if not validate_username_exists_in_database(username):
        return None
    validate_username_length(username)
    return user_repository.create_user_profile(username, first_name, last_name, password)
