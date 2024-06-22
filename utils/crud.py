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

def options_map():
    print("Menu opcji map: ")
    print("1.Mapa wszystkich Oddziałów Pogotowia Ratunkowego")
    print("2.Mapa wszystkich pracowników Oddziałów Pogotowia Ratunkowego")
    print("3.Mapa wszystkich pacjentów Oddziałów Pogotowia Ratunkowego")
    print("4.Mapa pracowników wybranego Oddziału Pogotowia Ratunkowego")
    print("5.Mapa pacjentów wybranego Oddziału Pogotowia Ratunkowego")
    choice = input("Wybierz interesującą opcję: ")
    return choice

def display_ambulance(ambulances):
    for ambulance in ambulances:
        print("Oddział:", ambulance['name'])
        print("Adres:", ambulance['address'])
        print("Lokalizacja:", ambulance['location'])


def add_ambulance(ambulances):
    name_oddzialu = input("Podaj nazwę oddziału: ")
    address = input("Podaj adres oddziału: ")
    location = (input("Podaj miasto, w którym znajduje się oddział: "))
    ambulance = {"name": name_oddzialu, "address": address, "location": location}
    ambulances.append(ambulance)
    print("Oddział został dodany do listy.")


def remove_ambulance(ambulances):
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
            ambulance['location'] = input("Podaj nowe miasto, w którym znajduje się oddział (lub pozostaw puste, aby nie zmieniać): ") or \
                                   ambulance['location']
        print("Dane Oddziału zostały zaktualizowane.")
        return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")


def display_employees(ambulances):
    ambulance_name = input("Podaj nazwę oddziału (brak wyboru pokaże wszystko): ")
    for ambulance in ambulances:
        if ambulance['name'] != ambulance_name and ambulance_name != "":
            continue
        for employee in ambulance['employees']:
            print(f"{employee['name']} {employee['surname']} {employee['coordinates']}")


def add_employee(ambulances):
    name_ambulance = input("Podaj nazwę oddziału, do której chcesz dodać pracowników: ")
    for ambulance in ambulances:
        if ambulance['name'] == name_ambulance:
            name = input("Podaj imię nowego pracownika: ")
            surname = input("Podaj nazwisko nowego pracownika: ")
            latitude = float(input("Podaj szerokość geograficzną pracownika: "))
            longitude = float(input("Podaj długość geograficzną pracownika: "))
            ambulance['employees'].append({'name': name, 'surname': surname, 'coordinates': {'latitude': latitude, 'longitude':longitude}})
            print("Pracownik dodany pomyślnie!")

def edit_employee(ambulances):
    ambulance_name = input("Podaj nazwę oddziału, w którego chcesz edytować listę pracowników: ")
    for ambulance in ambulances:
        if ambulance['name'] == ambulance_name:
            print("Lista pracowników oddziału", ambulance_name, ":")
            for employee in ambulance['employees']:
                print(f"{employee['name']} {employee['surname']} {employee['coordinates']}")
            while True:
                edit_choice = input("Podaj imię i nazwisko pracownika, którego chcesz edytować (lub 'exit' aby zakończyć edycję): ")
                if edit_choice.lower() == 'exit':
                    break
                for employee in ambulance['employees']:
                    if f"{employee['name']} {employee['surname']}".lower() == edit_choice.lower():
                        print("Edycja pracownika", edit_choice)
                        employee['name'] = input("Podaj nowe imię: ")
                        employee['surname'] = input("Podaj nowe nazwisko: ")
                        new_latitude = float(input("Podaj nową szerokość geograficzną pracownika: "))
                        new_longitude = float(input("Podaj nową długość geograficzną pracownika: "))
                        coordinates = (new_latitude, new_longitude)
                        employee['coordinates'] ={'latitude': new_latitude, 'longitude': new_longitude}
                        print("Pracownik zedytowany pomyślnie!")
                        break
                else:
                    print("Pracownik o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")

def delete_employee(ambulances):
    ambulance_name = input("Podaj nazwę oddziału, w którego chcesz usunąć pracowników: ")
    for ambulance in ambulances:
        if ambulance['name'] == ambulance_name:
            print("Lista pracowników w oddziału", ambulance_name, ":")
            for employee in ambulance['employees']:
                print(f"{employee['name']} {employee['surname']} {employee['coordinates']}")
            while True:
                edit_choice = input("Podaj imię i nazwisko pracownika, którego chcesz usunąć (lub 'exit' aby zakończyć edycję): ")
                if edit_choice.lower() == 'exit':
                    break
                for employee in ambulance['employees']:
                    if f"{employee['name']} {employee['surname']}".lower() == edit_choice.lower():
                        ambulance['employees'].remove(employee)
                        print("Pracownik zosatł usunięty")
                        break
                else:
                    print("Pracownik o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")

def display_patients(ambulances):
    ambulance_name = input("Podaj nazwę oddziału (brak wyboru pokaże wszystko): ")
    for ambulance in ambulances:
        if ambulance['name'] != ambulance_name and ambulance_name != "":
            continue
        for patient in ambulance['patients']:
            print(f"{patient['name']} {patient['surname']} {patient['incident']} {patient['coordinates']}")

def add_patient(ambulances):
    name_patient = input("Podaj nazwę oddziału, do której chcesz dodać pacjenta: ")
    for ambulance in ambulances:
        if ambulance['name'] == name_patient:
            name = input("Podaj imię nowego pacjenta: ")
            surname = input("Podaj nazwisko nowego pacjenta: ")
            incident = input("Podaj przyczynę zgłoszenia: ")
            latitude = float(input("Podaj szerokość geograficzną pacjenta: "))
            longitude = float(input("Podaj długość geograficzną pacjenta: "))
            coordinates = (latitude, longitude)
            ambulance['patients'].append({'name': name, 'surname': surname, 'incident': incident, 'coordinates': {'latitude': latitude, 'longitude':longitude}})
            print("Pacjent dodany pomyślnie!")

def edit_patient(ambulances):
    ambulance_name = input("Podaj nazwę oddziału, w którego chcesz edytować listę pacjentów: ")
    for ambulance in ambulances:
        if ambulance['name'] == ambulance_name:
            print("Lista pacjentów oddziału", ambulance_name, ":")
            for patient in ambulance['patients']:
                print(f"{patient['name']} {patient['surname']} {patient['incident']} {patient['coordinates']}")
            while True:
                edit_choice = input("Podaj imię i nazwisko pacjenta, którego chcesz edytować (lub 'exit' aby zakończyć edycję): ")
                if edit_choice.lower() == 'exit':
                    break
                for patient in ambulance['patients']:
                    if f"{patient['name']} {patient['surname']}".lower() == edit_choice.lower():
                        print("Edycja pacjenta: ", edit_choice)
                        patient['name'] = input("Podaj nowe imię: ")
                        patient['surname'] = input("Podaj nowe nazwisko: ")
                        patient['incident'] = input("Podaj nową przyczyne zgłoszenia: ")
                        new_latitude = float(input("Podaj nową szerokość geograficzną pracownika: "))
                        new_longitude = float(input("Podaj nową długość geograficzną pracownika: "))
                        coordinates = (new_latitude, new_longitude)
                        patient['coordinates'] ={'latitude': new_latitude, 'longitude': new_longitude}
                        print("Pacjent zedytowany pomyślnie!")
                        break
                else:
                    print("Pacjent o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")

def delete_patient(ambulances):
    ambulance_name = input("Podaj nazwę oddziału, w którego chcesz usunąć pacjenta: ")
    for ambulance in ambulances:
        if ambulance['name'] == ambulance_name:
            print("Lista pacjentów oddziału", ambulance_name, ":")
            for patient in ambulance['patients']:
                print(f"{patient['name']} {patient['surname']} {patient['incident']} {patient['coordinates']}")
            while True:
                edit_choice = input("Podaj imię i nazwisko pacjenta, którego chcesz usunąć (lub 'exit' aby zakończyć edycję): ")
                if edit_choice.lower() == 'exit':
                    break
                for patient in ambulance['patients']:
                    if f"{patient['name']} {patient['surname']}".lower() == edit_choice.lower():
                        ambulance['patients'].remove(patient)
                        print("Pacjent został usunięty")
                        break
                else:
                    print("Pacjent o podanym imieniu i nazwisku nie został znaleziony.")
            return
    print("Oddział o podanej nazwie nie został znaleziony w liście.")
