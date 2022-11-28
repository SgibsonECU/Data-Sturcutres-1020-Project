from users import Person
import datetime
date = str(datetime.date.today())

# Create a new Person entry in the database
Person_1 = Person('Mutulu Shakur', 21, 100)
Person_2 = Person('Ricky Bobby', 42, 0)
def begin_budget():
    # WELCOME MESSAGE (START OF PROGRAM)
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Welcome to Bloodhound Budgets!                         *")
    print("*                                                                          *")
    print("****************************************************************************")

    # Request User-Account PIN
    entered_pin = (input('Please Enter Your PIN Below to Get Started: \n')).strip()
    if entered_pin == '1':

        # Display user-name & date
        date = str(datetime.date.today())
        print(Person_1, f"{date:8s}")

        # Display Divider
        print('-' * 35)

        # User Commands
        # Added slot for transaction log and exit
        # Added slot to display Account info
        print(f'{"0 : Deposit":20} {"1 : Withdraw":16s}')
        print(f'{"2 : Get Balance":20s} {"3 : Add Expense":16s}')
        print(f'{"4 : Transfer Funds":20s} {"5 : View Transaction Log"}')
        print(f'{"6 : Display Info":20s} {"7 : Exit"}\n')

        #Ask User for next input
        # Added groundwork for the user functions
        user_input = input('Enter your selection:\n').strip().lower()
        print('\n\n\n\n\n')

        if user_input != 'exit':

            if user_input == '0' or user_input.lower() == 'Deposit':
                # set class variables
                amount = int(input("Please enter the amount you wish to deposit:\n"))
                self = Person_1.income

                #Initialize class def add_pay_check
                Person_1.add_pay_check(amount)

                #Ask for user input
                user_input = input('Press 1 or restart to return to main menu:\n').strip().lower()
                print('\n\n\n\n\n')

                # restart program
                if user_input == '1' or user_input.lower() == 'restart':
                    begin_budget()

                # end program
                else:
                    print("Thank you for using Bloodhound Budgets!")


            if user_input == '1' or user_input.lower() == 'Withdraw':
                # Display user-name & date
                date = str(datetime.date.today())
                print(Person_1, f"{date:8s}")

                # Display Divider
                print('-' * 35)

                print(f'{"0 : Housing":20} {"1 : Groceries":16s}')
                print(f'{"2 : Transportation":20s} {"3 : Utilities":16s}')
                print(f'{"4 : Dining":20s} {"5 : Entertainment"}')
                print(f'{"6 : Exit":20s}\n')

                user_input = input('Which expense would you like to withdraw from?:\n').strip().lower()
                print('\n\n\n\n\n')

                if user_input == '0' or user_input.lower() == 'Housing':

                    for Housing in ['Housing']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_1.decrease_category_funds(Housing, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '1' or user_input.lower() == 'Groceries':
                    for Groceries in ['Groceries']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_1.decrease_category_funds(Groceries, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()



                if user_input == '2' or user_input.lower() == 'Transportation':
                    for Transportation in ['Transportation']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_1.decrease_category_funds(Transportation, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '3' or user_input.lower() == 'Utilities':
                    for Utilities in ['Utilities']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_1.decrease_category_funds(Utilities, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '4' or user_input.lower() == 'Dining':
                    for Utilities in ['Dining']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_1.decrease_category_funds(Dining, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '5' or user_input.lower() == 'Entertainment':
                    for Entertainment in ['Entertainment']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_1.decrease_category_funds(Entertainment, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '6' or user_input.lower() == 'Exit':
                    begin_budget()


            if user_input == '2' or user_input.lower() == 'Get Balance':
                print("Total account balance:\n")
                Person_1.get_balance()
                user_input = input('Press 1 to return to the main menu:\n')
                if user_input == '1':
                    begin_budget()








            if user_input == '3' or user_input.lower() == 'Add expense':
                # Display user-name & date
                date = str(datetime.date.today())
                print(Person_1, f"{date:8s}")

                # Display Divider
                print('-' * 35)
                #Menu Options
                print(f'{"0 : Housing":20} {"1 : Groceries":16s}')
                print(f'{"2 : Transportation":20s} {"3 : Utilities":16s}')
                print(f'{"4 : Dining":20s} {"5 : Entertainment"}')
                print(f'{"6 : Exit":20s}\n')

                user_input = input('Enter your selection:\n').strip().lower()
                print('\n\n\n\n\n')

                if user_input == '0' or user_input.lower() == 'Housing':

                    for Housing in ['Housing']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))
                        Person_1.add_category_funds(Housing, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '1' or user_input.lower() == 'Groceries':

                    for Groceries in ['Groceries']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))

                        Person_1.add_category_funds(Groceries, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '2' or user_input.lower() == 'Transportation':

                    for Transportation in ['Transportation']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))

                        Person_1.add_category_funds(Transportation, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '3' or user_input.lower() == 'Utilities':

                    for Utilities in ['Utilities']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))

                        Person_1.add_category_funds(Utilities, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '4' or user_input.lower() == 'Dining':

                    for Dining in ['Dining']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))
                        Person_1.add_category_funds(Dining, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '5' or user_input.lower() == 'Entertainment':

                    for Entertainment in ['Entertainment']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))
                        Person_1.add_category_funds(Entertainment, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                    user_input = input('Press 1 to reset or any other key to exit\n')
                    if user_input == '1':
                        begin_budget()

                if user_input == '6' or user_input.lower() == 'Exit':
                    begin_budget()






            if user_input == '4' or user_input.lower() == 'Transfer Funds':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '5' or user_input.lower() == 'View Transaction Log':
                #FixMe Add the code here for person 1
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '6' or user_input.lower() == 'Display info':
                print(Person_1.print_all_info())
                print("Press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()



            if user_input == '7' or user_input.lower() == 'Exit':
                print("Thank you for choosing Bloodhound Budgets!")
                # reset program
                begin_budget()




    elif entered_pin == '2':
        date = str(datetime.date.today())
        print(Person_2, f"{date:8s}")

        # Display Divider
        print('-' * 35)

        # User Commands
        # Added slot for transaction log and exit
        #Added Slot to display account info
        print(f'{"0 : Deposit":20} {"1 : Withdraw":16s}')
        print(f'{"2 : Get Balance":20s} {"3 : Add Expense":16s}')
        print(f'{"4 : Transfer Funds":20s} {"5 : View Transaction Log"}')
        print(f'{"6 : Display Info":20s} {"7 : Exit"}\n')

        # Ask User for next input
        # Added groundwork for the user functions
        user_input = input('Enter your selection:\n').strip().lower()
        print('\n\n\n\n\n')

        if user_input != 'exit':

            if user_input == '0' or user_input.lower() == 'Deposit':
                # set class variables
                amount = int(input("Please enter the amount you wish to deposit"))
                self = Person_2.income

                # Initialize class def add_pay_check
                Person_2.add_pay_check(amount)

                # Ask for user input
                user_input = input('Press 1 or type restart to return to the main program:\n').strip().lower()
                print('\n\n\n\n\n')

                # restart program
                if user_input == '1' or user_input.lower() == 'restart':
                    begin_budget()

                # end program
                else:
                    print("Thank you for using Bloodhound Budgets!")

                if user_input == '1' or user_input.lower() == 'restart':
                    begin_budget()

                else:
                    print("Thank you for using Bloodhound Budgets!")
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '1' or user_input.lower() == 'Withdraw':
                # Display user-name & date
                date = str(datetime.date.today())
                print(Person_2, f"{date:8s}")

                # Display Divider
                print('-' * 35)

                print(f'{"0 : Housing":20} {"1 : Groceries":16s}')
                print(f'{"2 : Transportation":20s} {"3 : Utilities":16s}')
                print(f'{"4 : Dining":20s} {"5 : Entertainment"}')
                print(f'{"6 : Exit":20s}\n')

                user_input = input('Which expense would you like to withdraw from?:\n').strip().lower()
                print('\n\n\n\n\n')

                if user_input == '0' or user_input.lower() == 'Housing':

                    for Housing in ['Housing']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_2.decrease_category_funds(Housing, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '1' or user_input.lower() == 'Groceries':
                    for Groceries in ['Groceries']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_2.decrease_category_funds(Groceries, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '2' or user_input.lower() == 'Transportation':
                    for Transportation in ['Transportation']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_2.decrease_category_funds(Transportation, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '3' or user_input.lower() == 'Utilities':
                    for Utilities in ['Utilities']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_2.decrease_category_funds(Utilities, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '4' or user_input.lower() == 'Dining':
                    for Utilities in ['Dining']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_2.decrease_category_funds(Dining, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '5' or user_input.lower() == 'Entertainment':
                    for Entertainment in ['Entertainment']:
                        amount = int(input('Please enter the amount you wish to withdraw:\n'))
                        Person_2.decrease_category_funds(Entertainment, amount)
                        #Restart the program
                        user_input = input('Press 1 to reset\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '6' or user_input.lower() == 'Exit':
                    begin_budget()

            if user_input == '2' or user_input.lower() == 'Get Balance':
                print("Total account balance:\n")
                Person_2.get_balance()
                user_input = input('Press 1 to reset:\n')
                if user_input == '1':
                    begin_budget()


            if user_input == '3' or user_input.lower() == 'Add expense':
                print(f'{"0 : Housing":20} {"1 : Groceries":16s}')
                print(f'{"2 : Transportation":20s} {"3 : Utilities":16s}')
                print(f'{"4 : Dining":20s} {"5 : Entertainment"}')
                print(f'{"6 : Exit":20s}\n')

                user_input = input('Enter your selection:\n').strip().lower()
                print('\n\n\n\n\n')

                if user_input == '0' or user_input.lower() == 'Housing':

                    for Housing in ['Housing']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))
                        Person_2.add_category_funds(Housing, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '1' or user_input.lower() == 'Groceries':

                    for Groceries in ['Groceries']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))

                        Person_2.add_category_funds(Groceries, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '2' or user_input.lower() == 'Transportation':

                    for Transportation in ['Transportation']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))

                        Person_2.add_category_funds(Transportation, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '3' or user_input.lower() == 'Utilities':

                    for Utilities in ['Utilities']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))

                        Person_2.add_category_funds(Utilities, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '4' or user_input.lower() == 'Dining':

                    for Dining in ['Dining']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))
                        Person_2.add_category_funds(Dining, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                if user_input == '5' or user_input.lower() == 'Entertainment':

                    for Entertainment in ['Entertainment']:
                        amount = int(input('Please enter the amount you wish to transfer:\n'))
                        Person_2.add_category_funds(Entertainment, amount)
                        # Restart the program
                        user_input = input('Press 1 to reset or any other key to exit\n')
                        if user_input == '1':
                            begin_budget()

                    user_input = input('Press 1 to reset\n')
                    if user_input == '1':
                        begin_budget()

            if user_input == '4' or user_input.lower() == 'Transfer Funds':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '5' or user_input.lower() == 'View Transaction Log':
                #FixMe Add the code here for person 2
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '6' or user_input.lower() == 'Display info':
                print(Person_2.print_all_info())
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '7' or user_input.lower() == 'Exit':
                print("Thank you for choosing Bloodhound Budgets!")
                # reset program
                begin_budget()

    else:
        #Added user command to restart program on invalid input
        print("Sorry, invalid PIN, press 1 to restart")
        user_input = input()
        if user_input == '1':
            begin_budget()






#Person_1.add_pay_check(1000)
# Deposit PayCheck
#Person_1.add_pay_check(75)

# Add Expense
#Person_1.add_expense(200)
# Add Expense

#Person_1.add_expense(23)


# Request Balance
#Person_1.get_balance()

# Request All User Data
#Person_1.print_all_info()
#Person_2.print_all_info()

## Add Category Funds
#Person_1.add_category_funds('Housing', 331)
## Decrease Category Funds
#Person_1.decrease_category_funds('Housing', 300)
##Display Category Value
#Person_1.print_category('Housing')
##Create Additional Category
#Person_1.add_custom_category('Dating', 100_000)
##Transfer Category to Category Funds
#Person_1.transfer_category_funds('Housing', 'Dating', 10_000)
# Transfer All Category Funds
#Person_1.transfer_all_category_funds('Housing', 'Dating')
##Display All Person's Info
#Person_1.print_all_info()
##Display Person's Log
#Person_1.print_logs()

##Request Usage Percentage
#Person_1.get_use_percentage()

begin_budget()

