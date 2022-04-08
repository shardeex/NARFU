# Информационная система автопредприятия города. Основные сущности
# предметной области: автотранспорт, водители, маршруты, обслуживающий
# персонал, гаражное хозяйство. Сущность автотранспорт имеет следующие
# атрибуты: название транспорта (автобусы, такси, маршрутные такси, прочий
# легковой транспорт, грузовой транспорт и т.д.), кол-во наработки, пробег,
# колво ремонтов, характеристика. Сущность маршруты имеет следующие
# атрибуты: название маршрута, транспорт, водитель, график работы. Сущность
# водители имеет следующие атрибуты: фамилия, имя, отчество, год рождения,
# год поступления на работу, стаж, должность, пол, адрес, город, телефон.
# Сущность обслуживающий персонал имеет следующие атрибуты: должность
# (техники, сварщики, слесари, сборщики и др.), фамилия, имя, отчество, год
# рождения, год поступления на работу, стаж, пол, адрес, город, телефон.
# Сущность гаражное хозяйство имеет следующие атрибуты: название гаража,
# транспорт на ремонте, вид ремонта, дата поступления, дата выдачи после
# ремонта, результат ремонта, персонал, производящего ремонт.
from __future__ import annotations

import pickle
from datetime import datetime, date


_vehicle_id = 0


def _next_vehicle_id():
    global _vehicle_id
    _vehicle_id += 1
    return _vehicle_id


_person_id = 0


def _next_person_id():
    global _person_id
    _person_id += 1
    return _person_id


class Flight(object):
    def __init__(self, hours: int, mileage: int):
        self._date = datetime.today()
        self._hours = hours
        self._mileage = mileage

    def __del__(self):
        with open('flights.txt', 'a+') as f:
            f.write(f'{self._date}: {self._hours} hour(s) | {self._mileage} km\n')


class UndeleteableArgumentError(Exception):
    def __str__(self):
        return f'Undeleteable argument.'


class Vehicle():

    '''Base vehicle class.'''

    def __init__(
        self,
        name: str,
        operating_hours=0,
        mileage=0,
        number_of_repairs=0,
        characteristic='No characteristic yet.'
    ):
        self.name = name
        self._operating_hours = operating_hours
        self._mileage = mileage
        self._number_of_repairs = number_of_repairs
        self._characteristic = characteristic

        self.id = _next_vehicle_id()
        self.__flights = []

    def __str__(self):
        return (
            f'Vehicle "{self.name}" [ID: {self.id}], '
            f'{self._operating_hours} operatiing hours, '
            f'{self._mileage} mileage, '
            f'{self._number_of_repairs} number of repairs, '
            f'characteristic: "{self.characteristic}".'
        )

    def flight(self, hours: int, mileage: int):
        self._operating_hours += hours
        self._mileage += mileage
        self.__flights.append(Flight(hours, mileage))

    def get_flights(self):
        for i in range(len(self.__flights)):
            flight: Flight = self.__flights.pop(0)
            print(f'{flight._date}: {flight._hours} hours, {flight._mileage} km')

    @property
    def characteristic(self):
        return self._characteristic

    @characteristic.setter
    def characteristic(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Value "{value}" should be {str}, not {type(value)}')
        else:
            self._characteristic = value

    @characteristic.deleter
    def characteristic(self):
        raise UndeleteableArgumentError()

    @classmethod
    def add(cls, name: str):
        return cls(name)


class PersistenceVehicle(object):

    @staticmethod
    def serialize(vehicle: Vehicle):
        with open('vehicle.pkl', 'wb+') as f:
            pickle.dump(vehicle, f)

    @staticmethod
    def deserialize():
        with open('vehicle.pkl', 'rb') as f:
            vehicle = pickle.load(f)
        return vehicle


class LastDateError(Exception):

    def __init__(self, date):
        self.date = date
        self.today = date.today()

    def __str__(self):
        return f'Last working date cannot be from future (got {self.date}, today is {self.today})'


class LastWorkingDay():
    def __init__(self):
        self.max_date = date.today()
    def __get__(self, instance: Worker, cls):
        return instance._last_working_day
    def __set__(self, instance: Worker, value):
        if self.max_date < value:
            raise LastDateError(value)
        else:
            instance._last_working_day = value

class Worker():

    '''Base worker class.'''

    def __init__(
        self,
        surname: str,
        name: str,
        patronymic: str,
        year_of_birth: int,
        year_of_joining: int,
        experience: int,
        post: str,
        sex: str,
        address: str,
        city: str,
        phone_number: str
    ):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.year_of_birth = year_of_birth
        self.year_of_joining = year_of_joining
        self.experience = experience
        self.post = post
        self.sex = sex
        self.address = address
        self.city = city
        self.phone_number = phone_number

        self.last_working_day = LastWorkingDay()
        self._last_working_day = date.today()

        self.id = _next_person_id()

    @classmethod
    def recruit(cls, value):
        return cls(value)


class PersistenceWorker:

    @staticmethod
    def serialize(worker: Worker):
        with open('worker.pkl', 'wb+') as f:
            pickle.dump(worker, f)

    @staticmethod
    def deserialize():
        with open('worker.pkl', 'rb') as f:
            worker = pickle.load(f)
        return worker


class Driver(Worker):

    '''Driver worker class.'''

    job = 'driver'


class Service(Worker):

    '''Service worker class.'''

    job = 'service'

# по идее, для Driver и Service можно создать класс Worker и либо от него
# наследовать общий __init__(), либо просто добавить ещё один аргумент типа
# is_driver или что-то вроде этого. но по заданию это две сущности, потому так

# UPD: готово!

# UPD: лабораторная номер четыре, упс


class Route():

    '''Base route class.'''

    def __init__(
        self,
        name: str,
        vehicle: Vehicle,
        driver: Driver,
        schedule: str
    ):
        self.name = name
        self.vehicle = vehicle
        self.driver = driver
        self.schedule = schedule
    
    def __call__(self, time: int, mileage: int) -> Vehicle:
        '''Shortcut for `Route.drive_route()`

        :param int time: route time in h
        :param int mileage: route mileage in km
        :return Vehicle: route Vehicle 
        '''
        return self.drive_route(time, mileage)

    def drive_route(self, time: int, mileage: int):
        self.vehicle._operating_hours += time
        self.vehicle._mileage += mileage
        return Vehicle


class GarageFacilities():

    def __init__(
        self,
        name: str,
        vehicle_under_repair: Vehicle,
        repair_type: str,
        receipt_date: str,
        repair_result: str,
        service_staff_list: list
    ):
        self.name = name
        self.vehicle_under_repair = vehicle_under_repair
        self.repair_type = repair_type
        self.receipt_date = receipt_date
        self.repair_result = repair_result
        self.service_staff_list = service_staff_list
