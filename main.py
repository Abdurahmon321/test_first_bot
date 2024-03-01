from collections import namedtuple

#
# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self. lastname = lastname
#         self.age = age
#         self.email = email
#

# users = [
#     (1, "toxir", "Toxir", 18, "toxir@gmail"),
#     (2, "Sobir", "Toxir", 28, "toxir@gmail"),
#     (3, "Botir", "Toxir", 38, "toxir@gmail")
# ]

# user = User(*users)
#
# print(user.name)


# employee = namedtuple("Employee", "id name lastname age email")
#
# for user in users:
#     data = employee(*user)
#     print(*data)

car = ("malibu", "Red", "300 km/h", 2000, 4, "avtomat")

Car = namedtuple("Car", "name color speed price seats gearbox")

car_data = Car(*car)

print(*car_data)
