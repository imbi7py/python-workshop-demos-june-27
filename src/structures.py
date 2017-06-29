
# lists
nums = [1,2,3,4, 20]
names = ['kevin', 'hayk', 'dan']

print(names)
print("The first name: {}".format(names[0]))
print("The last name: {}".format(names[-1]))

# add new people
names.append('michael')
names.append('hannah')
names.append('ted')
names.append('rob')
print(names)

print(names[0][0])

print( names[1:4]  )
print( names[4:7]  )
print( names[4:]  )
print( names[:4]  )
print( names[-3:]  )
print( names[::-1]  )


print("This can be reversed"[::-1])

first_letters = []
for name in names:
    first_letters.append(name[0])

print(first_letters)


first_letters = [
    n[0] # thing to add
    for n in names # set to take from
    if len(n) > 3 # condition
]

print(first_letters)


# tuples:

t = ('michael', 'rob', 'ted')

m, r, _ = t

m = t[0]
r = t[1]
_ = t[2]

m

import collections
m = (23, 73, 1.02)

Measurement = collections.namedtuple("Measurement", 'x y ph')
m = Measurement(23, 73, 1.02)
print(m.ph)

# fast look ups
names = dict()
names = {}
names = {
    'm': 'Michael',
    'j': 'Jeff',
    't': 'Ted'
}
names['m'] = 'Michael'
names['j'] = 'Jeff'
names['t'] = 'Ted'

print(names.get('boo', 'MISSING'))






