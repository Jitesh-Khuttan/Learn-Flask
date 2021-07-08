user_mappings = {
}

def register_user(username, password):
    if username in user_mappings.keys():
        return f"{username} already registered."
    user_mappings[username] = {'username' : username, 'password' : password}
    return f"{username} registered."


def verify_user(username, password):
    if username in user_mappings.keys():
        return True if password == user_mappings[username]['password'] else False
    return False
