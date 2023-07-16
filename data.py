import requests
import random
import datetime

base_url = "http://localhost:9999/admin"  # Replace with your API base URL

def create_station(name: str, lat: float, lng: float):
    payload = {
        "name": name,
        "lat": lat,
        "lng": lng
    }
    response = requests.post(f"{base_url}/stations", json=payload)
    return response.json()

def create_route(name: str):
    payload = {
        "name": name
    }
    response = requests.post(f"{base_url}/routes", json=payload)
    return response.json()

def create_route_station(route_id: int, station_id: int, order: int):
    payload = {
        "route_id": route_id,
        "station_id": station_id,
        "order": order
    }
    response = requests.post(f"{base_url}/route_stations", json=payload)
    return response.json()

def create_train(name: str, route_id: int, capacity: int):
    payload = {
        "name": name,
        "route_id": route_id,
        "capacity": capacity
    }
    response = requests.post(f"{base_url}/trains", json=payload)
    return response.json()

def create_ticket(train_id: int, departure_station_id: int, arrival_station_id: int, departure_time: str, arrival_time: str, price: float, sold: int, service_class: str):
    payload = {
        "train_id": train_id,
        "departure_station_id": departure_station_id,
        "arrival_station_id": arrival_station_id,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "price": price,
        "sold": sold,
        "service_class": service_class
    }
    print("running")
    response = requests.post(f"{base_url}/tickets", json=payload)
    return response.json()

def create_ticket_price(ticket_id: int, date: str, price: float):
    payload = {
        "ticket_id": ticket_id,
        "date": date,
        "price": price
    }
    response = requests.post(f"{base_url}/ticket_prices", json=payload)
    print(response.json())
    return response.json()

def data_to_create_station():
    # Create stations
    stations = [
        ("Moscow", 55.7558, 37.6173),
        ("St. Petersburg", 59.9343, 30.3351),
        ("Novosibirsk", 55.0084, 82.9357),
        ("Yekaterinburg", 56.8389, 60.6057),
        ("Kazan", 55.8304, 49.0661),
        ("Nizhny Novgorod", 56.2965, 43.9361),
        ("Chelyabinsk", 55.1644, 61.4368),
        ("Samara", 53.1959, 50.1001),
        ("Omsk", 54.9885, 73.3242),
        ("Rostov-on-Don", 47.2357, 39.7015),
        ("Ufa", 54.7388, 55.9721),
        ("Krasnoyarsk", 56.0153, 92.8932),
        ("Voronezh", 51.6755, 39.2089),
        ("Volgograd", 48.7080, 44.5133),
        ("Krasnodar", 45.0355, 38.9753),
        ("Saratov", 51.5331, 46.0342),
        ("Tyumen", 57.1613, 65.5250),
        ("Tolyatti", 53.5078, 49.4204),
        ("Izhevsk", 56.8526, 53.2049),
        ("Barnaul", 53.3548, 83.7697),
        ("Ulyanovsk", 54.3081, 48.3743),
        ("Irkutsk", 52.2869, 104.3050),
        ("Khabarovsk", 48.4802, 135.0718),
        ("Yaroslavl", 57.6261, 39.8845),
        ("Vladivostok", 43.1155, 131.8854),
        ("Makhachkala", 42.9849, 47.5047)
    ]
    for station in stations:
        create_station(*station)

def data_to_create_route():
    routes = [
        "Moscow - St. Petersburg",
        "Moscow - Novosibirsk",
        "Moscow - Yekaterinburg",
        "Moscow - Kazan",
        "Moscow - Nizhny Novgorod",
        "Moscow - Chelyabinsk",
        "Moscow - Samara",
        "Moscow - Omsk",
        "Moscow - Rostov-on-Don",
        "Moscow - Ufa",
        "Moscow - Krasnoyarsk",
        "Moscow - Voronezh",
        "Moscow - Volgograd",
        "Moscow - Krasnodar",
        "Moscow - Saratov",
        "Moscow - Tyumen",
        "Moscow - Tolyatti",
        "Moscow - Izhevsk",
        "Moscow - Barnaul",
        "Moscow - Ulyanovsk",
        "Moscow - Irkutsk",
        "Moscow - Khabarovsk",
        "Moscow - Yaroslavl",
        "Moscow - Vladivostok",
        "Moscow - Makhachkala"
    ]

    for route in routes:
        create_route(route)

def data_to_create_route_station():
    # use real ids from request
    stations = requests.get(f"{base_url}/stations").json()
    routes = requests.get(f"{base_url}/routes").json()

    # mix stations and routes to create route_stations
    for route in routes:
        route_id = route["id"]
        stations_ids = random.sample([station["id"] for station in stations], random.randint(2, 5))
        for i, station_id in enumerate(stations_ids):
            create_route_station(route_id, station_id, i)

def data_to_create_train():
    # use real ids from request
    routes = requests.get(f"{base_url}/routes").json()

    # mix routes and create trains
    for route in routes:
        route_id = route["id"]
        create_train(f"Train {route_id}", route_id, random.randint(100, 1000))

def data_to_create_ticket():
    # use real ids from request
    trains = requests.get(f"{base_url}/trains").json()
    stations = requests.get(f"{base_url}/stations").json()

    # mix trains and stations to create tickets
    for train in trains:
        train_id = train["id"]
        stations_ids = [station["id"] for station in stations]
        for i in range(len(stations_ids) - 1):
            departure_station_id = stations_ids[i]
            arrival_station_id = stations_ids[i + 1]
            departure_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arrival_time = (datetime.datetime.now() + datetime.timedelta(hours=random.randint(1, 24))).strftime("%Y-%m-%d %H:%M:%S")
            price = random.randint(1000, 5000)
            sold = random.randint(0, 100)
            service_class = random.choice(["economy", "business"])
            create_ticket(train_id, departure_station_id, arrival_station_id, departure_time, arrival_time, price, sold, service_class)

def data_to_create_ticket_price():
    # use real ids from request
    tickets = requests.get(f"{base_url}/tickets").json()

    # mix tickets and create ticket_prices
    for ticket in tickets:
        ticket_id = ticket["id"]
        price:float = float(random.randint(1000, 5000))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_ticket_price(ticket_id, date, price)

if __name__ == "__main__":
    data_to_create_station()
    data_to_create_route()
    data_to_create_route_station()
    data_to_create_train()
    data_to_create_ticket()
    data_to_create_ticket_price()