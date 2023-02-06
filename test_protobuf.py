import Person_pb2

person = Person_pb2.Person()

person.name = "Hello"
person.id = 123456789
person.email = "mail@gmail.com"
phone = person.phones.add()
phone.number = "7777774444"
phone.type = Person_pb2.Person.PhoneType.MOBILE

print("Source object:")
print("Name:", person.name)
print("ID:", person.id)
print("Email:", person.email)
print("Phone:", person.phones)

print("Serialized string:", person.SerializeToString())

person2 = Person_pb2.Person()
person2.ParseFromString(person.SerializeToString())

print("Target object:")
print("Name:", person2.name)
print("ID:", person2.id)
print("Email:", person2.email)
print("Phone:", person2.phones)