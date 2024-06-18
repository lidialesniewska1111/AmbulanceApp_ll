def login():
    username = input("Wpisz login: ")
    password = input("Wpisz hasło: ")
    if username == "PPyt" and password == "PPyt":
        print("Zalogowano pomyślnie")
    else:
        print("Błędne hasło lub login. Wpisz ponownie dane do logowania.")
        login()

