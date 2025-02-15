friend_ages = {"rolf": 24, "atanu": 32}  # associated array
print(friend_ages['rolf'])

friend_ages['bob'] = 43
print(friend_ages)

friends = [
    {'name': 'rolf', 'age': 34},
    {'name': 'bob', 'age': 32}
]

print(friends)
print(friends[1])
print(friends[1]['name'])

student_attendances = {'rahul': 40, 'david': 50}
for student in student_attendances:
    print(student)
    print(f"{student}: has attendance {student_attendances[student]}%")

# Better way

for a, b in student_attendances.items():
    print(f"{a}: {b}")

# 2. for single key value pair, not array of object
if 'rahul' in student_attendances:
    print('present')
else:
    print('not present')

print('values', {student_attendances.values()})

print('items', {student_attendances.items()})
