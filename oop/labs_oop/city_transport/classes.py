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


class Vehicle():
    def __init__(self, name: str, operating_hours = 0, mileage = 0,
    number_of_repairs = 0, characteristic = "No characteristic yet."):
        self.name = name
        self.operating_hours = operating_hours
        self.mileage = mileage
        self.number_of_repairs = number_of_repairs
        self.characteristic = characteristic

        self.id = _next_vehicle_id()

    def __str__(self):
        return f"Vehicle \"{self.name}\" [ID: {self.id}], {self.operating_hours} operatiing \
hours, {self.mileage} mileage, {self.number_of_repairs} number of repairs, \
characteristic: \"{self.characteristic}\""

class Person():
    def __init__(self, surname: str, name: str, patronymic: str,
    year_of_birth: int, year_of_joining: int, experience: int,
    post: str, sex: str, address: str, city: str, phone_number: str):
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

        self.id = _next_person_id()

class Driver(Person):
    job = "driver"
        

class Service(Person):
    job = "service"

# по идее, для Driver и Service можно создать класс Person и либо от него
# наследовать общий __init__(), либо просто добавить ещё один аргумент типа
# is_driver или что-то вроде этого. но по заданию это две сущности, потому так

# UPD: готово!

class Route():
    def __init__(self, name: str, vehicle: Vehicle, driver: Driver,
    schedule: str):
        self.name = name
        self.vehicle = vehicle
        self.driver = driver
        self.schedule = schedule
    
    def drive_route(self, time, mileage):
        self.vehicle.operating_hours += time
        self.vehicle.mileage += mileage

class GarageFacilities():
    def __init__(self, name: str, vehicle_under_repair: Vehicle,
    repair_type: str, receipt_date: str, repair_result: str,
    service_staff_list: list): 
        self.name = name
        self.vehicle_under_repair = vehicle_under_repair
        self.repair_type = repair_type
        self.receipt_date = receipt_date
        self.repair_result = repair_result
        self.service_staff_list = service_staff_list