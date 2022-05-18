import itertools
import pickle


class SampleObject:

    new_id = itertools.count()

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = next(SampleObject.new_id)
        print(f"[+] Whoops, `{self.name}` `{id(self)}` was created!")
    
    def __str__(self) -> str:
        return f"[?] I'm `{self.name}`!"
    
    def __del__(self) -> None:
        print(f"[-] Oh no, `{self.name}` `{id(self)}` will be deleted...")
    
class Database:

    filename: str = 'database.pkl'

    def __init__(self, filename: str=filename) -> None:
        self.filename = filename
        self.storage = {} 
        try:
            self.open()
        except:
            self.save()

    def open(self) -> None:
        with open(self.filename, 'rb') as f:
            self.storage = pickle.load(f)

    def save(self) -> None:
        with open(self.filename, 'wb') as f:
            pickle.dump(self.storage, f)

    def get(self, obj_id: int) -> SampleObject | None:
        return self.storage.get(obj_id)


class CarelessDatabase(Database):

    def add(self, obj: SampleObject) -> None:
        self.storage[obj.id] = obj

    def remove(self, obj_id: int) -> None:
        self.storage.pop(obj_id)


class CarefulDatabase(Database):

    def add(self, **data) -> None:
        obj = SampleObject(**data)
        self.storage[obj.id] = obj

    def remove(self, obj_id: int) -> None:
        obj = super().get(obj_id)
        print('~~~ Before deletion in careful database ~~~')
        print('Object:', obj, id(obj))
        del obj
        print('~~~ After deletion in careful database ~~~')

    def save(self):
        super().save()
        for obj_id in list(self.storage.keys()):
            self.remove(obj_id)


print('=== Creating databases ===')
careless = CarelessDatabase('careless.pkl')
careful = CarefulDatabase('careful.pkl')

print('=== Adding objects ===')
obj = SampleObject('Careless Cube')
careless.add(obj)
careful.add(name='Careful Cube')

print('=== Saving databases ===')
careless.save()
careful.save()

print(obj, id(obj))
