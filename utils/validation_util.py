from repositories.user_repository import fake_database_profiles
from .custom_exceptions.user_exceptions import UserExceptions


def validate_username_exists_in_database(username):
    if not fake_database_profiles.get(username):
        raise UserExceptions(message="Username is not available")
    return True


def validate_username_length(username):
    if len(username) < 4:
        raise UserExceptions(message="Username needs to be a minimum of 4 characters")
    return True

