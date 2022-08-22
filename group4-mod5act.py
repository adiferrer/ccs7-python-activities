"""
CCS7 Lab Activity - Module 5
This is a Python program which simulates the computations done for a perceptron.
Submitted by Group 4 CITCS 2B

Members:
1. BIN ALSHAIBAH, ZAYED
2. FERRER, JEANNE ADELINE
3. RAMOS, GARHETT LEI
"""


def input_weight(n):
    words = ['first', 'second', 'third']
    while True:
        try:
            w = float(input(f'Enter the {words[n]} weight: '))
            return w
        except ValueError:
            print('Please provide a valid number.')


def spaces(s, val):
    available_space = s - len(str(val))
    return ' ' * available_space


def perceptron():
    l_list = [1, 0]

    w0 = input_weight(0)  # sample input: -30
    w1 = input_weight(1)  # sample input: 20
    w2 = input_weight(2)  # sample input: 20

    print('l1    l2   W0          W1          W2          Neuron      Sigmoid Function    Outputs   \n'
          '----  ---- ----------  ----------  ----------  ----------  ------------------  ----------')
    for i in l_list:
        for j in l_list:
            l1 = i
            l2 = j
            x = w0 + (w1 * l1) + (w2 * l2)
            y = 1 / (1 + (2.718 ** -x))
            y_string = format(y, '.5f')
            final_y = 1 if y >= 0.5 else 0
            print(f'{l1}     {l2}    {w0}{spaces(10, w0)}  {w1}{spaces(10, w1)}  {w2}{spaces(10, w2)}  {x}'
                  f'{spaces(10, x)}  {y_string}{spaces(18, y_string)}  {final_y}')


perceptron()
