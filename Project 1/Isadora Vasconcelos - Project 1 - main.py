
#—————————————————————————————————————
#Student Name: Isadora Vasconcelos De Lima
#Course: 2023SP-CIT-134A-201
#Term/Year: Spring 2023
#Date: 2/18/2023
#Project Number: 1
#find project also at: https://replit.com/join/ruidtjktkg-ivlm
#—————————————————————————————————————

#For this program, first I will present the program using the function #print. 

print ( 'Welcome to Employee Management Hub')
print()
#Now we will request #inputs from the user, such as their full name, company, address and the year they were hired. 

first_name = input ('Please, enter your first name: ')
print()
last_name = input ('Please, enter your last name: ')
print(f'Hello, {first_name} {last_name} ! Please respond to the prompts:')

company_name = input('Enter your company’s name: ')

print(f'You entered  {company_name}')

company_address = input ('Enter your company’s address: ')
print( f'You entered  {company_address}')

hire_year = input ('Enter the year you were hired: ') 
print(f'You entered {hire_year}')

#Now I want to confirm with the user that the information they entered is correct. For that I will prompt the user to check the information. If all is correct they can say Yes, if they say no, they can restart the program. 
print (f'Your Profile {last_name}, {first_name},  {company_name}, {company_address}, {hire_year}')

print(f'Your temporary password:{first_name}*{last_name}%{hire_year}')

