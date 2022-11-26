import re

number = input("Enter the mobile number: ")

pattern= re.compile("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$ ^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$ ")

if pattern.match(number):
    print(f'{number} is valid mobile number')

else:
    print(f'{number} is not valid mobile number')


'''123-456-7890
(123) 456-7890
123 456 7890
123.456.7890'''

