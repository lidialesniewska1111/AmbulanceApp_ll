import folium


def map_ambulance(ambulances):
    map = folium.Map(location=[52.250821, 20.894949], zoom_start=12)
    for ambulance in ambulances:
        latitude = ambulance['coordinates']['latitude']
        longitude = ambulance['coordinates']['longitude']
        name = ambulance['name']
        folium.Marker(location=[latitude, longitude], popup=f"{name}").add_to(map)
    map.save('./Wszystkie Stacje Pogotowia Ratowniczego.html')
    print("Plik HTML został wygenerowany.")

def map_employees(ambulances):
    map = folium.Map(location=[52.240821, 20.895949], zoom_start=12)
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
    map = folium.Map(location=[52.2468, 20.9491], zoom_start=11)
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
    map = folium.Map(location=[52.240821, 20.895949], zoom_start=12)
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
    map = folium.Map(location=[52.240821, 20.895949], zoom_start=12)
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