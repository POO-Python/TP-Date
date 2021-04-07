#=====================================================================================================================
#  ?  ABOUT
#  @author : Clément LO-CASCIO, Thibault BARRAL, Quentin SAR, Jathursan
#  MEHAVARNAN
#  @repo : https://github.com/POO-Python/TP-Date
#  @createdOn : 12/04/2021
#  @description : TP Dates of the POO module in python, Group N°2.
#=====================================================================================================================



#===================================================================================================
#                                          IMPORT AND START
#===================================================================================================

from ClassID import Id
from time import sleep

#-------- Definition of the reboot function ---------
def reboot():
    print("Reboot in progress.", end = '')
    sleep(1)
    print(".", end = '')
    sleep(1)
    print(".")


#-------- Definition of the main function ---------
def main():
    try:

        #We ask the name, firstname, registeration date of the user and we call the class Id
        name = input('\nYour name: ')
        first_name = input('Your first name: ')
        print("\nEnter a registration date: (which cannot be earlier than the current date)\n")
        register_day = input("Days : ")
        register_month = input("Month : ")
        register_year = input("Year : ")

        new = Id(1, name, first_name, int(register_day), int(register_month), int(register_year))

        print(new.firstName)

    except Exception as e:
        print(e)
        print(type(e))

#-------- Starting  ---------
print("\nTP Dates of the POO module in python, Group N°2.")

choose_add_register = input("\nWould you like to add a new registration today? (Answer Y for yes or N for no) : ")
if choose_add_register == "Y" or choose_add_register == "y" or choose_add_register == "yes":
    main()
else:
    print("\n\n GoodBye")
