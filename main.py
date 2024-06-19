from models.data_source import ambulances
from utils.crud import login, main_menu, options_menu, display_ambulance, add_ambulance, remove_ambulanse, edit_ambulance
# from utils.emap import single_map

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
            remove_ambulanse(ambulances)

    else:
        print("Opcja niedostępna.")

