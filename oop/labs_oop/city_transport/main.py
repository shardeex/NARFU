from classes import *


def clear_files():
    with open('flights.txt', 'w') as _: pass

def get_sample_route():
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
        "vehicle": Vehicle('White bus'),
        "driver": driver,
        "schedule": "Sat 12:05 \nSun 11:09",
    }
    return Route(**route_data)


if __name__ == '__main__':
    clear_files()

    try:
        run = int(input('Select LW [1..7]: '))
    except ValueError:
        print('You should input number to continue.')
        exit()

    match run: # python 3.10
        case 1:  # Лабораторная №1
            yellow_bus = Vehicle('Yellow bus')
            yellow_bus.characteristic = 'It is yellow and great.'
            print(yellow_bus)
        
        case 2:  # Лабораторная №2
            print('Check `test` directory.')
        
        case 3:  # Лабораторная №3
            red_motorcycle = Vehicle.add('Red motorcycle')
            red_motorcycle.characteristic = 'Old red motorcycle.'
            red_motorcycle.flight(5, 300)
            red_motorcycle.flight(4, 240)
            red_motorcycle.get_flights()
            PersistenceVehicle.serialize(red_motorcycle)
            print(PersistenceVehicle.deserialize())
        
        case 4:  # Лабораторная №4
            print('Already implemented in `Driver` & `Service` classes')

        case 5:  # Лабораторная #5
            try:
                blue_motorcycle = Vehicle.add('Blue motorcycle')
                blue_motorcycle.characteristic = 'New blue motorcycle.'
                del blue_motorcycle.characteristic
            except Exception as e:
                print(f'! Exception: {e}')

        case 6:  # Лабораторная №6
            route = get_sample_route()
            vehicle = route(10, 700)
            print(route.__doc__)
            vehicle.get_flights(silent=True)

        case 7:  # Лабораторная №7
            route = get_sample_route()
            vehicle = route.drive_with_logging(8, 800)
            vehicle.get_flights(silent=True)
        
        case 8:  # Лабораторная №8
            ...
