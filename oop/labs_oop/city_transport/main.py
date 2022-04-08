from classes import *


def clear_files():
    with open('flights.txt', 'w') as _: pass

if __name__ == '__main__':
    clear_files()

    # Лабораторная №1
    yellow_bus = Vehicle('Yellow bus')
    yellow_bus.characteristic = 'It is yellow and great.'
    print(yellow_bus)

    # Лабораторная №2 - test directory

    # Лабораторная №3
    red_motorcycle = Vehicle.add('Red motorcycle')
    red_motorcycle.characteristic = 'Old red motorcycle.'
    red_motorcycle.flight(5, 300)
    red_motorcycle.flight(4, 240)
    red_motorcycle.get_flights()
    PersistenceVehicle.serialize(red_motorcycle)
    print(PersistenceVehicle.deserialize())

    # Лабораторная №4 - уже реализовано в классах Driver и Service

    # Лабораторная #5
    try:
        # red_motorcycle.characteristic = 1001
        del red_motorcycle.characteristic
    except Exception as e:
        print(f'! Exception: {e}')

    # Лабораторная №6
    driver_data = {
        "surname": "Miloradov",
        "name": "Damian",
        "patronymic": "Leonidovich",
        "year_of_birth": 1991,
        "year_of_joining": 2007,
        "experience": 16,
        "post": "Bus driver",
        "sex": "male",
        "address": "Nekrasovskaya, bld. 53/А, appt. 33",
        "city": "Kaspipol",
        "phone_number": "+7(4232)57-70835"
    }
    driver = Driver(**driver_data)

    route_data = {
        "name": "Kaspipol — Alerzhinsk",
        "vehicle": yellow_bus,
        "driver": driver,
        "schedule": "Sat 12:05 \nSun 11:09",
    }
    route = Route(**route_data)

    route(10, 700)
    print(help(route))
