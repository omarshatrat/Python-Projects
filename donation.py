# -*- coding: utf-8 -*-
"""donation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/172fprojX8BGPceq3BL0mhJ5Ys8ze_7c3
"""

'''
Program: donation.py. 

Programmer: Omar Shatrat

Date: 10/15/2022

Description: Program for Red Cross which calculates average, high, and low pints of blood donated.

'''

def main():
  again = 'no'
  while again == 'no':
    pints = []
    total_pints = 0
    average_pints = 0
    high_pints = 0
    low_pints = 0
    get_pints(pints)
    total_pints = get_total(pints, total_pints)
    average_pints = get_average(total_pints, average_pints)
    high_pints = get_high(pints, high_pints)
    low_pints = get_low(pints, low_pints)
    display_results(average_pints, high_pints, low_pints)
    again = input("\nDo you want to end program (Enter no or yes): ")

def get_pints(pints):
  for i in range(0,7):
    ele = input('\nEnter pints collected: ')
    pints.append(int(ele))
  return pints

def get_total(pints, total_pints):
  total_pints = 0
  for i in pints:
    total_pints += i
  return total_pints

def get_average(total_pints, average_pints):
  average_pints = total_pints / 7
  return average_pints

def get_high(pints, high_pints):
  high_pints = max(pints)
  return high_pints

def get_low(pints, low_pints):
  low_pints = min(pints)
  return low_pints

def display_results(average_pints, high_pints, low_pints):
  print("\nThe average number of pints donated is ", average_pints)
  print("\nThe highest pints donated is ", high_pints)
  print("\nThe lowest pints donated is ", low_pints)

main()

'''Sample run
Enter pints collected: 43

Enter pints collected: 25

Enter pints collected: 64

Enter pints collected: 35

Enter pints collected: 19

Enter pints collected: 37

Enter pints collected: 46

The average number of pints donated is  38.42857142857143

The highest pints donated is  64

The lowest pints donated is  19

Do you want to end program (Enter no or yes): no

Enter pints collected: 1

Enter pints collected: 2

Enter pints collected: 3

Enter pints collected: 4

Enter pints collected: 5

Enter pints collected: 6

Enter pints collected: 7

The average number of pints donated is  4.0

The highest pints donated is  7

The lowest pints donated is  1

Do you want to end program (Enter no or yes): yes
'''