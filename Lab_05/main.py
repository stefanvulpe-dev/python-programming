import decimal
import random

from animals.Bird import Bird
from animals.Fish import Fish
from animals.Mammal import Mammal
from employees.Manager import Manager
from bank_accounts.SavingsAccount import SavingsAccount
from library.Book import Book
from library.DVD import DVD
from shapes.Triangle import Triangle
from vehicles.Car import Car
from vehicles.Truck import Truck

s = Triangle(3, 4, 5)
print(s.calculate_area())

account = SavingsAccount("savings", decimal.Decimal(100), decimal.Decimal(100));
print(account)
account.deposit(decimal.Decimal(100))
account.withdraw(decimal.Decimal(25))
print(account)

skoda = Car("Skoda", "Octavia", 2015, "white", 220)
print(skoda)
print(f"Skoda millage: {skoda.get_millage()} km")
volvo = Truck("Volvo", "FH16", 2018, "red", 250, 20000)
print(f"Volvo millage: {volvo.get_millage()} km")
print(f"Volvo towing capacity: {volvo.get_towing_capacity()} tons")

john = Manager("John", 30, 1000, 100, "IT")
print(john)
print(f"John bonus: {john.get_bonus()}")
print(f"John department: {john.get_department()}")

cow = Mammal("Cow", 100)
print(f"Cow's milk amount: {cow.get_milk_amount()}")
nemo = Fish("Nemo", 0.5)
nemo.swim()
zolly = Bird("Zolly", 0.3)
zolly.fly()

linkin_park = DVD("Minutes to Midnight", random.randint(1000, 9999).__str__(), 1_000_000, "2007-05-14", 0)
print(linkin_park)
print(linkin_park.check_availability())
furniture_polish = DVD("Furniture Polish", random.randint(1000, 9999).__str__(), 1_000_000, "2007-05-14", 1)
print(furniture_polish)
print(furniture_polish.check_availability())
harry_potter = Book("Harry Potter", random.randint(1000, 9999).__str__(), 1_000_000,
                    "JK Rowling", "Fantasy")
print(harry_potter)
print(harry_potter.check_availability())


