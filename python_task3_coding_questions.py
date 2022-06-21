# QUESTION 1
def hello_name(user_name):
    '''write a fn to print "hello_USERNAME!" 
    USERNAME is the input of the fn'''
    print(f"hello_{user_name.upper()}!")

hello_name('Alex')


# QUESTION 2
def first_odds():
    '''print all odd numbers from 1-100'''
    for num in range(1,101):
        if num % 2 != 0:
            print(num)

first_odds()


# QUESTION 3
def max_num_in_list(a_list):
    '''return the max number in a given list'''
    return max(a_list)

print(max_num_in_list([500,2,3,4,1000,6,7,8,99,9,9,]))


# QUESTION 4
def is_leap_year(a_year):
    '''return True/False if a given year is a leap year.'''
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0:
        if a_year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

print(is_leap_year(1980))


# QUESTION 5
def is_consecutive(a_list):
    '''write a fn to check if all numbers in a list are consecutive numbers, 
    return True if so.'''
    return True if max(a_list) - min(a_list) + 1 == len(a_list) else False
    

print(is_consecutive([2,3,4,5,6,7,8,9,10,11,12]))