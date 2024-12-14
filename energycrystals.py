# Input energy crystals and target energy as strings
#energy_crystals = input()  # Input as a string
#target_energy = input()  # Input as a string

# Write your solution below and make sure to print the number of ways

energy_crystals  = '[2,5,3,6]'
target_energy = '10'

energy_crystals = energy_crystals.replace('[', '').replace(']','')

l_energy_crystals = []
for n in energy_crystals.split(','):
    n = int(n)
    l_energy_crystals.append(n)

target_energy = int(target_energy)


def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

sublists = list(powerset(l_energy_crystals))

print(sublists)

if [] in sublists:
    sublists.remove([])

result = []
for sublist in sublists:
    sum = 0
    for i in sublist:
        sum = sum + i

    j = 0
    while j <= target_energy:
        if sum == target_energy:
            result.append(sublist)
        elif sum < target_energy:
            sum = sum + sublist[0]

        j = j + 1

s = set()
for item in result:
    s.add(tuple(item))


print(s)

###################

for i in range(len(sublists)):
    for j in range(len(sublists[i])):
        c_current  = target_energy - max(sublists[i])

        sl = sorted(sublists[i])


        for k in range(len(sublists[i])):
            diff = c_current - max(sl)
