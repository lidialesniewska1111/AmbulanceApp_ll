from models.data_source import ambulances
from utils.crud import login
# from utils.emap import single_map

if __name__ == '__main__':
    while True:
        print("Welcome to the AmulanceApp  ")
        print("0. Exit ")
        print("1. Przejdź do systemu logowania ")
        menu_option = input("Wybierz opcję: ")
        if menu_option == "0":
            break
        if menu_option == "1":
            login()

