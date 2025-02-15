x = 5, 11
u, v = x

print(
    f"u : {u}, y: {v}"
)

student_attendances = {'rahul': 40, 'david': 50}
print(list(student_attendances))
print(list(student_attendances.items()))

people = [("bob", 23), ("rahul", 35), ("green", 77)]

for name, age in people:
    print(f"{name} has age : {age}")

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)  # it will remove first element and then print all rest of the values
