is_hot = False
is_cold = False


# python using indentation instead of curly braces for code blocks
# if is_hot:
#     print("its a hot day")
#     print('drink waster')
# elif is_cold:
#     print('its a cold day')
#     print('wear a jacket')
# else:
#     print('enjoy your day')

has_good_credit = False
home_cost = 1000000

if has_good_credit:
    print(f'down payment: {int(home_cost * .1)}')
else:
    print(f'down payment: {int(home_cost * .2)}')
