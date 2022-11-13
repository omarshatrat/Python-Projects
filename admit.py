# -*- coding: utf-8 -*-
"""admit

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oFSzWMfqLRgYC2Tg1DXMtoxZQYnsIIsQ
"""

'''
Program:  admit.py. 

Programmer: Omar Shatrat

Date: 09/17/2022

Description:  The program compares two college applicants. The program should prompt for each student’s GPA, SAT, and ACT exam scores and report which candidate is more qualified on the basis of these scores.
'''

#This code introduces the program and its purpose to the user.

print("This program compares two applicants to determine which one seems like the stronger applicant. \nFor each candidate I will need either SAT or ACT scores as well as a weighted GPA.")

#This block of code takes all of the relevant information from applicant 1 and converts it into a standardized metric.

print("Information for the first applicant:")
exam_type = int(input("\tdo you have 1) SAT scores or 2) ACT scores? ")) #SAT or ACT taken

if exam_type == 1:
  s_math_score = int(input("\tSAT math? ")) #SAT math score
  verbal_score = int(input("\tSAT verbal? ")) #SAT verbal score
  gpa = float(input("\toverall GPA? ")) #overall GPA
  max_gpa = float(input("\tmax GPA? ")) #maximum possible GPA
elif exam_type == 2:
  english_score = int(input("\tACT English? ")) #ACT English score
  a_math_score = int(input("\tACT math? ")) #ACT math score
  reading_score = int(input("\tACT reading? ")) #ACT reading score
  science_score = int(input("\tACT science? ")) #ACT science score
  ovr_gpa = float(input("\toverall GPA? ")) #overall GPA
  max_gpa = float(input("\tmax GPA? ")) #maximum possible GPA
    
sat_score = (2 * verbal_score + s_math_score) / 24.0 #SAT score calculation
act_score = (2 * reading_score + english_score + a_math_score + science_score) / 1.8 #ACT score calculation
gpa_score = gpa / max_gpa * 100.0 #GPA converted to percentage

if exam_type == 1:
  applicant_1_score = sat_score + gpa_score #Applicant 1 score if they took SAT
else:
  applicant_1_score = act_score + gpa_score #Applicant 1 score if they took ACT

#This block of code takes all of the relevant information from applicant 2 and converts it into a standardized metric.

print("Information for the second applicant:")
exam_type = int(input("\tdo you have 1) SAT scores or 2) ACT scores? ")) #SAT or ACT taken

if exam_type == 1:
  s_math_score = int(input("\tSAT math? ")) #SAT math score
  verbal_score = int(input("\tSAT verbal? ")) #SAT verbal score
  gpa = float(input("\toverall GPA? ")) #overall GPA
  max_gpa = float(input("\tmax GPA? ")) #maximum possible GPA
elif exam_type == 2:
  english_score = int(input("\tACT English? ")) #ACT English score
  a_math_score = int(input("\tACT math? ")) #ACT math score
  reading_score = int(input("\tACT reading? ")) #ACT reading score
  science_score = int(input("\tACT science? ")) #ACT science score
  ovr_gpa = float(input("\toverall GPA? ")) #overall GPA
  max_gpa = float(input("\tmax GPA? ")) #maximum possible GPA


sat_score = (2 * verbal_score + s_math_score) / 24.0 #SAT score calculation
act_score = (2 * reading_score + english_score + a_math_score + science_score) / 1.8 #ACT score calculation
gpa_score = gpa / max_gpa * 100.0 #GPA converted to percentage
   
if exam_type == 1:
  applicant_2_score = sat_score + gpa_score #Applicant 2 score if they took SAT
else:
  applicant_2_score = act_score + gpa_score #Applicant 2 score if they took ACT

#This code block assesses which applicant took which test and makes a comparison as to which applicant is better.

print('First applicant overall score =', round(applicant_1_score, 2))
print('Second applicant overall score =', round(applicant_2_score, 2))

if applicant_1_score > applicant_2_score:
  print("The first applicant seems to be better")
elif applicant_2_score > applicant_1_score:
  print("The second applicant seems to be better")
else:
  print("The two applicants seem to be equal")

#This is a source run

'''
This program compares two applicants to determine which one seems like the stronger applicant. 
For each candidate I will need either SAT or ACT scores as well as a weighted GPA.

Information for the first applicant:
	do you have 1) SAT scores or 2) ACT scores? 1
  SAT math? 510
  SAT verbal? 530
  overall GPA? 3.4
  max GPA? 4.0

Information for the second applicant:
	do you have 1) SAT scores or 2) ACT scores? 1
  SAT math? 570
  SAT verbal? 500
  overall GPA? 3.4
  max GPA? 4.0

First applicant overall score = 150.42
Second applicant overall score = 150.42
The two applicants seem to be equal
'''