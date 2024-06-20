from models.data_source import ambulances
from utils.crud import login, main_menu, options_menu, options_map, display_ambulance, add_ambulance, remove_ambulance, \
    edit_ambulance, display_employees, add_employee, edit_employee, delete_employee, display_patients, add_patient, edit_patient, delete_patient

from utils.emap import map_ambulance, map_employees, map_patients, map_employee_ambulance, map_patient_ambulance

print("Welcome to the AmulanceApp ")
login()

while True:
    choice = main_menu()
    if choice == "0":
        break
    if choice == "1":
        choice_options = options_menu()
        if choice_options == "1":
            display_ambulance(ambulances)
        if choice_options == "2":
            add_ambulance(ambulances)
        if choice_options == "3":
            edit_ambulance(ambulances)
        if choice_options == "4":
            remove_ambulance(ambulances)
    elif choice == "2":
        choice_options = options_menu()
        if choice_options == "1":
            display_employees(ambulances)
        if choice_options == "2":
            add_employee(ambulances)
        if choice_options == "3":
            edit_employee(ambulances)
        if choice_options == "4":
            delete_employee(ambulances)
    elif choice == "3":
        choice_options = options_menu()
        if choice_options == "1":
            display_patients(ambulances)
        if choice_options == "2":
            add_patient(ambulances)
        if choice_options == "3":
            edit_patient(ambulances)
        if choice_options == "4":
            delete_patient(ambulances)
    elif choice == "4":
        choice_options = options_map()
        if choice_options == "1":
            map_ambulance(ambulances)
        if choice_options == "2":
            map_employees(ambulances)
        if choice_options == "3":
            map_patients(ambulances)
        if choice_options == "4":
            map_employee_ambulance(ambulances)
        if choice_options == "5":
            map_patient_ambulance(ambulances)
    else:
        print("Opcja niedostępna.")
