import bcrypt


def hash_password(password: str) -> bytes:
    # Generate salt for complex password
    salt = bcrypt.gensalt()

    # Hashing password
    hashed = bcrypt.hashpw(password.encode("UTF-8"), salt)

    # retur password hashed
    return hashed


def check_password(hashed: bytes, password: str):
    # check if passowrd is correct when is hashed
    return bcrypt.checkpw(password.encode("UTF-8"), hashed)


def main() -> None:
    # Get the password of user input
    password = input("Insert password: ")

    hashed_password = hash_password(password)

    # Print hashed password
    print(f"Contraseña hasheada: {hashed_password.decode('UTF-8')}")

    # Basic passowrd check
    if check_password(hashed_password, password):
        print("Correct Password!")
    else:
        print("Incorrect Password!")


if __name__ == "__main__":
    main()
