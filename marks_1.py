import sys
n=10
def section_1():
  while n<=10:  
    print('\t\t\t\t Marks Sheet')
    a=input('Name of the student: ')
    b=input("Father's Name: ")
    print('Section:4-A ')

    d=float(input('Marks scored in History: '))
    print('' if d<=100 and d>=0 else sys.exit('Please enter valid marks'))

    e=float(input('Marks scored in Geography: '))
    print('' if e<=100 and e>=0 else sys.exit('Please enter valid marks'))

    f=float(input('Marks scored in Criminal Laws:'))
    print('' if f<=100 and f>=0 else sys.exit('Please enter valid marks'))

    g=float(input('Marks scored in Cyber Laws:'))
    print('' if g<=100 and g>=0 else sys.exit('Please enter valid marks'))

    total=d+e+f+g
    average=(d+e+f+g)/4
    print('Total: ', round(total,2),'/400')
    print('Average: ', average)



section_1()