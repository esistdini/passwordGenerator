"""

Python module for password generation made using
python with the help of 'random' module

This tool contains topic about both
for loop , function and random module usage referrence

"""

import random

#Performs password generation operation

class passwordGenerator:
        
        def operation(self,user_input):

            user_input = int(user_input)

            password = ""

            symbols = "!@#$%^&*()_+=-?/><.,:;\'\"}{|"
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower_case = upper_case.lower()


            lower_case = list(lower_case)
            upper_case = list(upper_case)
            symbols = list(symbols)

            
            for x in range(user_input):
                l = random.randint(0,3)
                if l == 0:
                    a = random.randint(0,25)
                    password = password + upper_case[a]
                elif l == 1:
                    a = random.randint(0,25)
                    password = password + lower_case[a]
                elif l == 3:
                    a = random.randint(0,26)
                    password = password + symbols[a]
                else:
                    a = random.randint(0,9)
                    password = password + str(a)

            return str(password)


