"""
CCS7 Lab Activity - Module 2
This is a Python program which simulates the computations done for a linear regression problem.
Submitted by Group 4 CITCS 2B

Members:
1. BIN ALSHAIBAH, ZAYED
2. FERRER, JEANNE ADELINE
3. RAMOS, GARHETT LEI
"""


# This function converts the input string of numbers to a list of numbers
def to_list(prompt, t, data_num):
    user_input = input(prompt)
    if t == 'f':
        if len([float(s) for s in user_input.split(',')]) == data_num:
            return [float(s) for s in user_input.split(',')]
        else:
            return []
    elif t == 'i':
        if len([int(s) for s in user_input.split(',')]) == data_num:
            return [int(s) for s in user_input.split(',')]
        else:
            return []


# This function adds even spacing for the table
def spaces(val):
    available_space = 15 - len(str(val))
    return ' ' * available_space


# This function sums up the numbers in a given list
def summation(number_list):
    sum_of_list = 0
    for e in number_list:
        sum_of_list += e
    return sum_of_list


# This function puts the a and b values in a string equation
def to_equation(a, b):
    if b > 0:
        return '\nEquation:  Y = ' + format(a, '.4f') + ' + ' + format(b, '.4f') + 'X'
    else:
        return '\nEquation:  Y = ' + format(a, '.4f') + ' - ' + format(abs(b), '.4f') + 'X'


# This function computes for the simple linear regression for a set of x and y values
def linear_regression():
    number_of_values = 0
    table_of_values = []
    while True:
        try:
            # type 10 for the sample values
            number_of_values = int(input("Input the number of sets of x\'s and y\'s to be calculated: "))
            if number_of_values < 1:
                print('Please enter a number greater than or equal to 1.')
            else:
                break
        except ValueError:
            print('Invalid input! Enter an integer.')

    type_num = ''
    while True:
        # use 'i' for the sample values
        type_num = input('Do your data sets have float or only integer values? Type f or i only: ')
        if type_num.lower() != 'f' and type_num.lower() != 'i':
            print('Not a valid type! Enter either f or i.')
        else:
            break

    while True:
        try:
            # Sample Values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            x_values = to_list(f'Input all the {number_of_values} x values. They should be separated by a comma(,'
                               f') only: ',
                               type_num.lower(), number_of_values)
            if len(x_values) == 0:
                print(f'Input {number_of_values} values.')
                continue

            # Sample Values: 10, 10, 8, 8, 6, 6, 4, 4, 2, 2
            y_values = to_list(f'Input all the {number_of_values} y values. They should be separated by a comma(,'
                               f') only: ',
                               type_num.lower(), number_of_values)
            if len(y_values) == 0:
                print(f'Input {number_of_values} values.')
                continue

            table_of_values.append(x_values)
            table_of_values.append(y_values)
            break
        except:
            print('An error occurred. Enter the correct data sets.\n')

    table_of_values.extend([[], []])

    # Prints the table
    print('\nx              y              x^2            xy')
    print('-' * 60)
    for i in range(0, number_of_values):
        x = table_of_values[0][i]
        y = table_of_values[1][i]
        x_sq = x * x
        xy = x * y
        table_of_values[2].append(x_sq)
        table_of_values[3].append(xy)
        print(str(x) + spaces(x) + str(y) + spaces(y) +
              str(x_sq) + spaces(x_sq) + str(xy) + spaces(xy))

    x_sum = summation(table_of_values[0])
    y_sum = summation(table_of_values[1])
    x_squared_sum = summation(table_of_values[2])
    xy_sum = summation(table_of_values[3])
    print('-' * 60)
    print(str(x_sum) + spaces(x_sum) + str(y_sum) + spaces(y_sum) +
          str(x_squared_sum) + spaces(x_squared_sum) + str(xy_sum) + spaces(xy_sum))

    a = ((y_sum * x_squared_sum) - (x_sum * xy_sum)) / (number_of_values * x_squared_sum - x_sum * x_sum)
    b = ((number_of_values * xy_sum) - (x_sum * y_sum)) / (number_of_values * x_squared_sum - x_sum * x_sum)

    eq = to_equation(a, b)
    print(eq)


linear_regression()
