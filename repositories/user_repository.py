fake_database_profiles = {
    "Persephone657": {
        "FirstName": "Courtney",
        "LastName": "Marsh",
        "Password": "iLovechase123!"
    },
    "Snoodle": {
        "FirstName": "Chase",
        "LastName": "Struse",
        "Password": "iLoveCourtney8!"
    }
}


fake_database_user_profiles = {

}


def get_user(username):
    return fake_database_profiles[username]


def create_user_profile(username, first_name, last_name, current_password):
    if fake_database_profiles.get(username):
        return 500

    obj = {
        "FirstName": first_name,
        "LastName": last_name,
        "Password": current_password
    }
    fake_database_user_profiles[username] = obj
    return fake_database_user_profiles[username]


def change_password(username, new_password):
    fake_database_profiles[username]['Password'] = new_password
    return fake_database_profiles[username]

