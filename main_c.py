from FullName_c import *

# __init__
fn1 = FullName('Micheal', 'Remington')
fn2 = FullName('Regina', 'Marshall')
fn3 = FullName('Micheal', 'Marshall')
fn4 = FullName('Regina', 'Marshall')

# all fn list
# __repr__
all_fn_list = [fn1, fn2, fn3, fn4]

# __str__
print(f'Full Name 1: {fn1}')
print(f'Full Name 2: {fn2}')
print(f'Full Name 3: {fn3}')
print(f'Full Name 4: {fn4}')
# __gt__

# return T as Remington is after Marshall
print(f'FN1 > FN2: {fn1 > fn2}')
# return F
print(f'FN2 > FN1: {fn2 > fn1}')
# return F as Micheal does not come after Regina
print(f'FN3 > FN4: {fn3 > fn4}')
# return T
print(f'FN4 > FN3: {fn4 > fn3}')
# comparing sane name so return F
print(f'FN4 > FN2: {fn4 > fn2}')
print(f'FN2 > FN4: {fn2 > fn4}')

# sort obj in list
print()
print("Original List:")
print(all_fn_list)
# __repr__
print("Sorted Lists:")
all_fn_list.sort(key=lambda x: x.first_n)
print(all_fn_list)
all_fn_list.sort()
print(all_fn_list)

# other comparisons
print()
print(f'Other Comparisons:')
print(f'FN4 > FN1: {fn4 > fn1}')
print(f'FN1 > FN4: {fn1 > fn4}')
print(f'FN2 > FN3: {fn2 > fn3}')
print(f'FN3 > FN2: {fn3 > fn2}')
print(f'FN1 > FN3: {fn1 > fn3}')
print(f'FN3 > FN1: {fn3 > fn1}')
