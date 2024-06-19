def login():
    username = input("Wpisz login: ")
    password = input("Wpisz hasło: ")
    if username == "PPyt" and password == "PPyt":
        print("Zalogowano pomyślnie")
    else:
        print("Błędne hasło lub login. Spróbuj ponownie.")
        login()

def main_menu():
    print("0.Exit")
    print("1.Dostępne opcje dla Oddziałów Pogotowia Ratunkowego")
    print("2.Dostępne opcje dla pracowników Pogotowia Ratunkowego")
    print("3.Dostępne opcje dla pacjentów Pogotowia Ratunkowego")
    print("4.Generowanie map")
    choice = input("Wybierz interesującą opcję: ")
    return choice

def options_menu():
    print("Menu opcji: ")
    print("1.Lista")
    print("2.Dodawanie")
    print("3.Edycja")
    print("4.Usuwanie")
    choice = input("Wybierz interesującą opcję: ")
    return choice

def display_ambulance(ambulances):
    for ambulance in ambulances:
        print("Oddział:", ambulance['name'])
        print("Adres:", ambulance['address'])
        print("Współrzędne:", ambulance['coordinates'])


def add_ambulance(ambulances):
    name_oddzialu = input("Podaj nazwę oddziału: ")
    address = input("Podaj adres oddziału: ")
    latitude = float(input("Podaj szerokość geograficzną odziału: "))
    longitude = float(input("Podaj długość geograficzną oddziału: "))
    coordinates = (longitude, latitude)
    ambulance = {"name": name_oddzialu, "address": address, "coordinates": coordinates}
    ambulances.append(ambulance)
    print("Oddział został dodany do listy.")

def remove_ambulanse(ambulances):
    name = input("Podaj nazwę oddziału, który chcesz usunąć: ")
    for ambulance in ambulances:
        if ambulance['name'] == name:
            ambulances.remove(ambulance)
            print("Oddział został usunięty z listy.")
            return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")

def edit_ambulance(ambulances):
    name = input("Podaj nazwę oddziału, który chcesz edytować: ")
    for ambulance in ambulances:
        if ambulance['name'] == name:
            print("Edycja danych oddziału:")
            ambulance['name'] = input("Podaj nową nazwę oddziału (lub pozostaw puste, aby nie zmieniać): ") or \
                                 ambulance['name_oddzialu']
            ambulance['address'] = input("Podaj nowy adres oddziału (lub pozostaw puste, aby nie zmieniać): ") or \
                                    ambulance['address']
            latitude = input("Podaj nową szerokość geograficzną oddziału (lub pozostaw puste, aby nie zmieniać): ")
            if latitude:
                ambulance['coordinates']['latitude'] = float(latitude)
            longitude = input("Podaj nową długość geograficzną oddziału (lub pozostaw puste, aby nie zmieniać): ")
            if longitude:
                ambulance['coordinates']['longitude'] = float(longitude)
        print("Dane Oddziału zostały zaktualizowane.")
        return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")