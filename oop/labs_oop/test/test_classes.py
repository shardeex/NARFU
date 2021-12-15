from city_transport import classes

import unittest

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

route_data = {
    "name": "Kaspipol — Alerzhinsk",
    "vehicle": classes.Vehicle(
        "Old yellow bus", operating_hours = 10, mileage = 500),
    "driver": classes.Driver(**driver_data),
    "schedule": "Sat 12:05 \nSun 11:09",
}

class TestRoute(unittest.TestCase):

    def setUp(self):
        self.route = classes.Route(**route_data)
    
    def test_drive_route(self):
        test_mileage = 800
        test_operating_hours = 15
        self.route.drive_route(5, 300)

        self.assertEqual(test_mileage, self.route.vehicle.mileage)
        self.assertEqual(test_operating_hours, self.route.vehicle.operating_hours)


if __name__ == '__main__':
    unittest.main()