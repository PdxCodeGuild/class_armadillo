


# build a list of even numbers
evens = []
for i in range(2, 20, 2):
  evens.append(i)
print(evens)



evens = [i for i in range(2, 20, 2)]
print(evens)



people = ['Joe Schmoe', 'Jill Schmill', 'Jane Schplain']
people = [person.lower() for person in people]
people = [person.split(' ') for person in people]
people = [person for person in people if person[0] != 'joe']
print(people)

nums = [4, 5, 6, 14, 15, 16]
exclamation = '!'
nums = [str(num)+exclamation for num in nums if num < 10]
print(nums)


identity_matrix = [[1 if i == j else 0 for i in range(10)] for j in range(10)]
# print(identity_matrix)

for row in identity_matrix:
  print(row)
