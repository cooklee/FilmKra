def check_length(password):
    return len(password) >= 7

def check_small(password):
    for x in password:
        if x.islower():
            return True
    return False

def check_secial_sign(password):
    sings = "!@#$%^&*()\""
    for x in password:
        if x in sings:
            return True
    return False


def check_password(password):
    return check_length(password) and check_small(password)
