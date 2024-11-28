# Functions

# def hello_function():
#     print('Hello Function!')


# hello_function()
# hello_function()
# hello_function()
# hello_function()

# print(hello_function())

# Functions help in many ways such as keeping the code dry

# def hello_function(greeting):
#     return '{} Function.'.format(greeting).upper()


# print(hello_function("Hey"))
# # or
# hello_function("Hey")

# def hello_function(greeting,name = 'You'):
#     return '{}, {}'.format(greeting,name)


# print(hello_function('Hi', name ='John'))


# def student_info(*args,**kwargs):
#     print(args)
#     print(kwargs)

# courses =  ['Math','Art']
# info = {'name': 'John',  'age': '22'}

# student_info(*courses,**info)
 
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# %  = divisibilty

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2016,2))