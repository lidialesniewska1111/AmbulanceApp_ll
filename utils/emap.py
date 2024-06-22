import folium
import requests
from bs4 import BeautifulSoup

def map_ambulance(ambulances):
    lista_wspolrzednych = []
    map = folium.Map(location=[52, 21], zoom_start=6)
    for ambulance in ambulances:
        url: str = f'https://pl.wikipedia.org/wiki/{ambulance['location']}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = response_html.select('.latitude')[1].text.replace(",",".")
        longitude = response_html.select('.longitude')[1].text.replace(",",".")
        name = ambulance['name']
        folium.Marker(location=[latitude, longitude], popup=f"{name}").add_to(map)
    map.save('./Wszystkie Stacje Pogotowia Ratowniczego.html')
    print("Plik HTML został wygenerowany.")
def map_employees(ambulances):
    map = folium.Map(location=[52.00, 20.00], zoom_start=6)
    for ambulance in ambulances:
        for employee in ambulance['employees']:
            latitude = employee['coordinates']['latitude']
            longitude = employee['coordinates']['longitude']
            name = employee['name']
            surname = employee['surname']
            folium.Marker(location=[latitude, longitude], popup=f"{name} {surname}").add_to(map)
            map.save('./Wszyscy pracownicy Pogotowia Ratowniczego.html')
    print("Plik HTML został wygenerowany.")

def map_patients(ambulances):
    map = folium.Map(location=[52.2468, 20.9491], zoom_start=6)
    for ambulance in ambulances:
        for patient in ambulance['patients']:
            latitude = patient['coordinates']['latitude']
            longitude = patient['coordinates']['longitude']
            name = patient['name']
            surname = patient['surname']
            incident = patient['incident']
            folium.Marker(location=[latitude, longitude], popup=f"{name} {surname} {incident}").add_to(map)
            map.save('./Wszyscy pacjenci Pogotowia Ratowniczego.html')
    print("Plik HTML został wygenerowany.")

def map_employee_ambulance(ambulances):
    ambulance_name = input("Wpisz Oddział Pogotowia Ratowniczego: ")
    map = folium.Map(location=[52.240821, 20.895949], zoom_start=6)
    for ambulance in ambulances:
        if ambulance['name'] == ambulance_name:
            for employee in ambulance['employees']:
                latitude = employee['coordinates']['latitude']
                longitude = employee['coordinates']['longitude']
                name = employee['name']
                surname = employee['surname']
                folium.Marker(location=[latitude, longitude], popup=f"{name} {surname}").add_to(map)
                map.save('./Wszyscy pracownicy dla konkretnego oddziału Pogotowia Ratowniczego.html')
    print("Plik HTML został wygenerowany.")

def map_patient_ambulance(ambulances):
    ambulance_name = input("Wpisz Oddział Pogotowia Ratowniczego: ")
    map = folium.Map(location=[52.240821, 20.895949], zoom_start=6)
    for ambulance in ambulances:
        if ambulance['name'] == ambulance_name:
            for patient in ambulance['patients']:
                latitude = patient['coordinates']['latitude']
                longitude = patient['coordinates']['longitude']
                name = patient['name']
                surname = patient['surname']
                incident = patient['incident']
                folium.Marker(location=[latitude, longitude], popup=f"{name} {surname} {incident}").add_to(map)
                map.save('./Wszyscy pacjenci dla konkretnego oddziału Pogotowia Ratowniczego.html')
    print("Plik HTML został wygenerowany.")