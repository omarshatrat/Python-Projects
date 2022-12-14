# -*- coding: utf-8 -*-
"""computer_assisted_functions

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vxnen9PZxXQniu7omG6bW_AV6xGSrTHE
"""

'''
Program:computer_assisted_functions.py. 

Programmer: Omar Shatrat

Date: 10/01/2022

Description: Computer-assisted instruction (CAI) refers to the use of computers in education. Write a program to help an elementary school student learn multiplication, division, addition, and subtraction.

'''

def get_operation():
  #Prints menu and stores choice to a variable
  print('1 = addition \n2 = subtraction \n3 = multiplication \n4 = division')
  operation = int(input('Enter the operation (1 to 4) or -1 to exit: '))
  return operation

def create_question(operation):
  #Uses choice previously made to carry out operation on two integers, return question and answer
  int1 = 8
  int2 = 2
  question_answer = 0
  question_text = ''
  if operation == 1:
    question_text = 'How much is ' + str(int1) + ' + ' + str(int2)
    question_answer = int1 + int2
  
  if operation == 2:
    question_text = 'How much is ' + str(int1) + ' - ' + str(int2)
    question_answer = int1 - int2
  
  if operation == 3:
    question_text = 'How much is ' + str(int1) + ' * ' + str(int2)
    question_answer = int1 * int2
  
  if operation == 4:
    question_text = 'How much is ' + str(int1) + ' / ' + str(int2)
    question_answer = int1 / int2
  
  return question_text, question_answer

def check_answer(guess, answer):
  #Checks if the guess is equal to the answer and sets boolean to True if so
  boolean = False
  if guess == answer:
    boolean = True
  else:
    boolean = False
  return boolean

def get_response(is_correct):
  #Assigns an approrpiate string to print based on whether a boolean is True or False
  t_or_f = ''
  if is_correct == True:
    t_or_f = 'Correct, good work! \n'
  else:
    t_or_f = 'Incorrect, please try again!'
  return t_or_f

def main():
  #Carries out all the other functions, repeating them until -1 is entered
  operation = get_operation()
  if operation == -1:
    print('Thanks for playing!')
    return None
  question, answer = create_question(operation)
  print(question)
  guess = int(input("Enter your answer: "))
  is_correct = check_answer(guess, answer)
  response = get_response(is_correct)
  print(response)
  
  while is_correct == True:
    operation = get_operation()
    if operation == -1:
      print('Thanks for playing!')
      return None
    question, answer = create_question(operation)
    print(question)
    guess = int(input("Enter your answer: "))
    is_correct = check_answer(guess, answer)
    response = get_response(is_correct)
    print(response)
  
  while is_correct == False:
    print(question)
    guess = int(input("Enter your answer: "))
    is_correct = check_answer(guess, answer)
    response = get_response(is_correct)
    print(response)

  main()

main()

'''Sample run
1 = addition 
2 = subtraction 
3 = multiplication 
4 = division
Enter the operation (1 to 4) or -1 to exit: 2
How much is 8 - 2
Enter your answer: 12
Incorrect, please try again!
How much is 8 - 2
Enter your answer: 6
Correct, good work! 

1 = addition 
2 = subtraction 
3 = multiplication 
4 = division
Enter the operation (1 to 4) or -1 to exit: 1
How much is 8 + 2
Enter your answer: 11
Incorrect, please try again!
How much is 8 + 2
Enter your answer: 10
Correct, good work! 

1 = addition 
2 = subtraction 
3 = multiplication 
4 = division
Enter the operation (1 to 4) or -1 to exit: -1
Thanks for playing!
'''