from models.data_source import ambulances
from utils.crud import login, main_menu, options_menu, display_ambulance, add_ambulance, remove_ambulance, edit_ambulance, display_employees, add_employee, edit_employee, delete_employee
# from utils.emap import single_map

# print("Welcome to the AmulanceApp ")
# login()

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
    # elif choice == "3":
    #     choice_options = options_menu()
    #     if choice_options == "1":
    else:
        print("Opcja niedostępna.")

