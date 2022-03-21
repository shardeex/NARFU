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
