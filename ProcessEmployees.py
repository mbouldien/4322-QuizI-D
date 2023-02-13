'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r')
reader = csv.reader(infile)

next(reader)

#create an empty dictionary
emp_dict = {}

print()

#use a loop to iterate through the csv file
for row in reader:
    fname = row[1]
    lname = row[2]
    department = row[3]
    title = row[4]
    salary = float(row[5])

    full_name = fname + ' ' + lname

    #check if the employee fits the search criteria
    if department == 'Marketing':
        if title == 'CSR':
            new_salary = salary * 1.10
            emp_dict[full_name] = new_salary
            print('Manager Name:', full_name, 'Current Salary:', '$' + format(salary, ',.2f'))
    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for employee in emp_dict:
    print('Manager Name:', employee, 'New Salary:', '$' + format(emp_dict[employee], ',.2f'))

print()         
        

        
    
