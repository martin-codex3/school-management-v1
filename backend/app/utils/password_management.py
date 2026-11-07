from pwdlib import PasswordHash, exceptions

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    hashed_password = password_hash.hash(password)
    return hashed_password


# we will verify the password here
def verify_hashed_password(user_password: str, hashed_password: str) -> bool:
    try:
        return password_hash.verify(user_password, hashed_password)
    except exceptions.UnknownHashError as ex:
        raise ex.message
