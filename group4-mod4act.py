"""
CCS7 Lab Activity - Module 4
This is a Python program which simulates the computations done for a K-means clustering method.
Submitted by Group 4 CITCS 2B

Members:
1. BIN ALSHAIBAH, ZAYED
2. FERRER, JEANNE ADELINE
3. RAMOS, GARHETT LEI
"""
import random


# Retrieves the dataset with no duplicate inputs
def input_to_list():
    while True:
        try:
            user_input = input('Input only 15 unique numbers for clustering: ')
            # Sample Input: 1, 2, 4, 5, 9, 13, 16, 17, 18, 19, 23, 24, 25, 26, 28
            list_input = [int(s) for s in user_input.split(',')]
            if len(list_input) == 15 and len(set(list_input)) == 15:
                return list_input
            else:
                print('Please provide exact 15 unique values.')
        except ValueError:
            print('Invalid input detected! Please enter either integer or float values.')


def k_mean(k_list):
    total = 0
    for e in k_list:
        total += e
    return format(total / float(len(k_list)), '.2f')


def new_or_not_new(prev_k_m, new_k_m, k_no):
    if new_k_m != prev_k_m:
        return f"K{k_no} Mean is {new_k_m} is NEW (Not equal to {prev_k_m})"
    else:
        return f"K{k_no} Mean is {new_k_m} is NOT NEW (Equal to {prev_k_m})"


def k_clustering():
    print('Welcome to the Cluster Simulator! Please enter 15 integers to proceed!')
    dataset = input_to_list()  # print(dataset)

    # STEP 1: Determine the value of k
    k_value = 3
    print(f'STEP 1: The number of clusters is {k_value}.\n')

    # STEP 2: Determine k random data/object points from the dataset
    k_list = sorted(random.sample(dataset, k=k_value))  # print(k_list)
    k1 = k_list[0]
    k2 = k_list[1]
    k3 = k_list[2]
    print(f"STEP 2:\n"
          f"K1 = {k1}\n"
          f"K2 = {k2}\n"
          f"K3 = {k3}\n")

    while True:
        # STEP 3: Cluster the other data/objects to their nearest k points
        k1_list = []
        k2_list = []
        k3_list = []
        for d in dataset:
            diff1 = abs(k1-d)
            diff2 = abs(k2-d)
            diff3 = abs(k3-d)
            if diff1 <= diff2 and diff1 <= diff3:
                k1_list.append(d)
            elif diff2 <= diff1 and diff2 <= diff3:
                k2_list.append(d)
            else:
                k3_list.append(d)
        print(f'STEP 3:\n'
              f'- K1 = {k1} has {set(k1_list)}\n'
              f'- K2 = {k2} has {set(k2_list)}\n'
              f'- K3 = {k3} has {set(k3_list)}\n')

        # STEP 4: Determine the mean of the clusters and assign these as the new points for k
        k1_mean = float(k_mean(k1_list))
        k2_mean = float(k_mean(k2_list))
        k3_mean = float(k_mean(k3_list))
        print(f'STEP 4:\n'
              f'- K1 Mean is {k1_mean}\n'
              f'- K2 Mean is {k2_mean}\n'
              f'- K3 Mean is {k3_mean}\n')

        # STEP 5: Check if mean values encountered are new
        print(f'STEP 5:\n'
              f'- {new_or_not_new(k1, k1_mean, 1)}\n'
              f'- {new_or_not_new(k2, k2_mean, 2)}\n'
              f'- {new_or_not_new(k3, k3_mean, 3)}')
        if k1 != k1_mean or k2_mean != k2_mean or k3 != k3_mean:
            print("New assignments are encountered.\n\n"
                  "-----------------REPEATING STEPS 3-5-----------------")
            k1 = k1_mean
            k2 = k2_mean
            k3 = k3_mean
        else:
            print("No new assignments are encountered.\n\n"
                  "------------------THE MODEL IS READY------------------\n"
                  "For prediction, a data or an object belongs to the nearest cluster: K1, K2 or K3.")
            break


k_clustering()
