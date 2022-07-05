# def get_water_bill(num_gallons):
#     if num_gallons<= 8000:
#         bill = num_gallons*5/1000
#     elif num_gallons<=22000:
#         bill = num_gallons*6/1000
#     elif num_gallons<=30000:
#         bill = num_gallons*7/1000
#     else:
#         bill = num_gallons*10/1000
#     return bill

# print(get_water_bill(10000))

# def get_phone_bill(gb):
#     if gb<=15:
#         bill = 100
#     else:
#         bill = 100 + (gb-15)*100
#     return bill
# print(get_phone_bill(15.1))


# num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
#                  141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
#                  141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# print('avg_first_seven' , sum(num_customers[:7])/7)
# print('avg_last_seven',  sum(num_customers[23:])/7)
# print('max_month', max(num_customers))
# print('min_month',  min(num_customers))\


# def percentage_liked(ratings):
#     list_liked = [i>=4 for i in ratings]
#     percentage_liked = sum(list_liked)/len(ratings)
#     return percentage_liked

# # Do not change: should return 0.5
# print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))


# def percentage_growth(num_users, yrs_ago):
#     growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
#     return growth

# # Do not change: Variable for calculating some test examples
# num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
# # Do not change: Should return .036
# print(percentage_growth(num_users_test, 1))

# # Do not change: Should return 0.66
# print(percentage_growth(num_users_test, 7))

print(round(3.7834349635634, 4))

def get_least(a, b, c):
    """the function returns the least among input values a, b, and c
    it can further do this this this this and this."""
    number  = a+b-c
    return number


mystery = print()
print(mystery)
print(1, 2, 4, 5)

def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
greet()

# def mult_by_five(x):
#     return 5 * x

# def call(fn, arg):
#     """Call fn on arg"""
#     return fn(arg)

# def squared_call(fn, arg):
#     """Call fn on the result of calling fn on arg"""
#     return fn(fn(arg))

# print(
#     call(mult_by_five, 1),
#     squared_call(mult_by_five, 1), 
#     sep='\n', # '\n' is the newline character - it starts a new line
# )

# def round_to_two_places(num):
#     """Return the given number rounded to two decimal places. 
    
#     >>> round_to_two_places(3.14159)
#     3.14
#     """
#     # Replace this body with your own code.
#     # ("pass" is a keyword that does literally nothing. We used it as a placeholder
#     # because after we begin a code block, Python requires at least one line of code)
#     a = round(num, 2)
#     return a
# print(round_to_two_places(3.14159))


def to_smash(total_candies, are_Three = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if are_Three == None:
        smashed = total_candies%3
    else: 
        smashed = total_candies%are_Three
    return smashed
print(to_smash(65, 4))