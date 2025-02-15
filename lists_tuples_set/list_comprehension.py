# 1.
numbers = [1, 2, 3]
doubled = [num * 3 for num in numbers]
# here " for num in numbers " is loop
# and num*2 is multiplying each num with number 2
print(doubled)

# The above code is written as
for num in numbers:
    doubled.append(num * 2)

print("\n ")
print(doubled)

#  2.
friends = ['ram', 'rahul', 'jyoti', 'ram', 'sita', 'hanuman']
starts_r = []
for friend in friends:
    if friend.startswith('r'):
        starts_r.append(friend)

print(starts_r)

# the above code is also written in this way
starts_r = [friend for friend in friends if friend.startswith('r')]
print(starts_r)

# a. for loop for friend in friends
# b. fetch current friend in "friend" which is in left side ( friend for friend should be same
# c. after loop there is if condition

# check equality
friends1 = ['ram', 'rahul', 'ram']

print(friends1 is starts_r)
print("firend1", id(friends1), " start ", id(starts_r))
