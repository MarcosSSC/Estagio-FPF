from datetime import datetime, date

class employee:

    def __init__(self, name=None, gender=None, salary=None, birth_date=None):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.birth_date = birth_date

    @property
    def age(self):
        _now = datetime.now().date()
        diff = _now - self.birth_date
        return int(diff.days / 365)

e1 = employee()

e1.name = 'Marcos'
e1.gender = 'M'
e1.salary = '1600'
e1.birth_date = date(year=2000, month=8, day=16)

e2 = employee(name='Livia', gender='F', salary='4000', birth_date=date(year=2001, month=1, day=12))

e3 = employee()

print(e1.name)
print(e1.age)
#print(e2)
#print(e3)