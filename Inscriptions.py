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
from ClassDate import Date
from time import sleep
from datetime import date, datetime
from ClassDateException import *
import sys

#-------- Definition of the reboot function ---------
def reboot(step, currentDate, chooseRegistration, numberRegistration):
    state = input("\nDo you want to enter another registration date? (Answer Y for yes or N for no) : ")
    if state == "Y" or state == "Yes" or state == "y" or state == "yes":
        main("new_registration", currentDate, chooseRegistration, numberRegistration)
    elif state == "N" or state == "No" or state == "n" or state == "no":
        #The user does not want to add a new record, we invite him to enter the current date
        main()
    else:
        print("\nIncorrect answer.")
        reboot(step, currentDate, chooseRegistration, numberRegistration)

#-------- Definition of the check user exists in registration list function ---------
def check_user(name, first_name):
    for element in listRegistration:
        if element.name == name and element.firstName == first_name:
            return True
    return False

#-------- Definition of the ask new register function ---------
def ask_new_register(currentDate, chooseRegistration, numberRegistration):
    print("\nTo cancel the registration, press ctrl + c\n")
    #We ask the name
    name = input('\nName: ').upper()
    #If the name is a empty string, we ask his name
    while name == "" :
        name = input("").upper()
    #We ask the first name
    first_name = input('First name: ').upper()
    #If the name is a empty string, we ask his first name
    while first_name == "":
        first_name = input("").upper()
    #Check if the user exist is in registration list
    user_exists = check_user(name, first_name)

    if user_exists == False:
        print("\nEnter a registration date: (which cannot be earlier than the current date)")
        register_day = input("\nDays : ")
        register_month = input("Month : ")
        register_year = input("Year : ")
        return name, first_name, register_day, register_month, register_year
    else:
        #If User exists we ask if he want to continue  to enter an new user registration
        print("\nThis identity already appears in the list of registrants.")
        continue_state = input("\nDo you want to continue with the registration? (Answer Y for yes or N for no) : ")
        #If his choice is a empty string, we ask his choice
        while continue_state == "":
            print("\nIncorrect answer.")
            continue_state = input("\nDo you want to continue with the registration? (Answer Y for yes or N for no) : ")
        if continue_state == "Y" or continue_state == "Yes" or continue_state == "y" or continue_state == "yes":
            #If he want, we redirect to create it 
            main("new_registration", currentDate, chooseRegistration, numberRegistration)
        elif continue_state == "N" or continue_state == "No" or continue_state == "n" or continue_state == "no":
            #If he don't want, we cancel the registration, we ask if he want to add a new registration today
            # and call the main function with the step for new registration
            print("\nRegistration cancelled.")
            add_registration = input("\nWould you like to add a new registration today? (Answer Y for yes or N for no) : ")
            #If his choice is a empty string, we ask his choice
            while add_registration == "":
                add_registration = input("\nWould you like to add a new registration today? (Answer Y for yes or N for no) : ")
            if add_registration == "Y" or add_registration == "Yes" or add_registration == "y" or add_registration == "yes":
                main("new_registration", currentDate, chooseRegistration, numberRegistration)
            else:
                #If he don't want we call the main function
                main()

#-------- Definition of the main function ---------
def main(step=None, currentDate=None, chooseRegistration=None, numberRegistration=0, UserRegister=None, RegisterDate=None):
    try:
        #In this case, we have just start the program
        if step == None:
            #We ask the currentDate and we call the date Class
            print("\nEnter today's date : (Enter 1/1/9999 to display the registration list)")
            day = input("    Days : ")
            month = input("    Month : ")
            year = input("    Year : ")
            print("\nToday's date is: {0}/{1}/{2}".format(day, month, year))

            #We confirm to the user
            confirmed_state = input("\nDo you confirm this date? (Answer Y for yes or N for no) : ")
            if confirmed_state == "Y" or confirmed_state == "Yes" or confirmed_state == "y" or confirmed_state == "yes":
                #If Date who has entered 1/1/99 and print the list of registrations (sorted by registration number)
                if int(day) == 1 and int(month) == 1 and int(year) == 9999:
                    print("\nEnd of registration.")
                    main("print_list_registration_number")
                else:
                    #We instance the currentDate with Date Class
                    currentDate = Date(int(day), int(month), int(year))
                

                #We ask to the user if he want to add a new registration
                chooseRegistration = input("\nWould you like to add a new registration today? (Answer Y for yes or N for no) : ")
                main("new_registration", currentDate, chooseRegistration)
            elif confirmed_state == "N" or confirmed_state == "No" or confirmed_state == "n" or confirmed_state == "no":
                main()
            else:
                print("\nIncorrect answer.")
                main()

        #In this case, we we carry out a new registration today
        elif step == "new_registration" and currentDate != None and chooseRegistration != None:
           
            if chooseRegistration == "Y" or chooseRegistration == "y" or chooseRegistration == "yes":
                #We ask the name, firstname, registeration date of the user 
                register = ask_new_register(currentDate, chooseRegistration, numberRegistration)

                registerDate = Date(int(register[2]), int(register[3]), int(register[4]))
               
                #Check if the date of registration is prior to the current date. If it's we raise an error
                #because that means the registerDate is prior to the currentDate.
                registerDate < currentDate

                print("\nSummary: {0} {1} {2}/{3}/{4}".format(register[0], register[1], register[2], register[3], register[4]))
                main ("confirm_registration", currentDate, chooseRegistration, numberRegistration, register, registerDate)

            #The user does not want to add a new record, we invite him to enter the current date
            elif chooseRegistration == "N" or chooseRegistration == "No" or chooseRegistration == "n" or chooseRegistration == "no":
                print("\nRegistration closes today.")
                main()
            else:
                print("\nIncorrect answer.")
                chooseRegistration = input("\nWould you like to add a new registration today? (Answer Y for yes or N for no) : ")
                main("new_registration", currentDate, chooseRegistration)

        #In this case, we confirm data before call ClassId and append in the registration list
        elif step == "confirm_registration" and currentDate != None and chooseRegistration != None and UserRegister != None and RegisterDate != None:

                confirm_registeration = input("\nDo you confirm this registration? (Answer Y for yes or N for no) : ")

                if confirm_registeration == "Y" or confirm_registeration == "Yes" or confirm_registeration == "y" or confirm_registeration == "yes":

                    #We call the class Id,  add +1 to the number of registration and confirme the registration to the user
                    numberRegistration += 1
                    registerClass = Id(numberRegistration, UserRegister[0], UserRegister[1], RegisterDate)
                    listRegistration.append(registerClass)
                    print("\nRegistration validated.")
                    state = input("\nDo you want to enter another registration date? (Answer Y for yes or N for no) : ")
                    main("new_registration", currentDate, state, numberRegistration)
                elif confirm_registeration == "N" or confirm_registeration == "No" or confirm_registeration == "n" or confirm_registeration == "no":
                    #We ask for a new registration
                    confirmed_state =  input("\nDo you want to enter another registration date? (Answer Y for yes or N for no) : ")
                    main("new_registration", currentDate, confirmed_state)
                else:
                    #In other case
                    print("\nIncorrect answer.")
                    main("new_registration", currentDate, "Y", numberRegistration, UserRegister, RegisterDate)

        #In this case, we print the list of registration who is ordred by number registration
        elif step == "print_list_registration_number":

            print("\nList of registrations (sorted by registration number)\n")
            print("{:15} {:15} {:15} {:15}".format("Number :", "Name :", "First name :", "Date of registration :")) 

            if listRegistration == []:
                print("\nNo registrations were entered today.\n")
            else:
                i = 0
                for element in listRegistration:
                    i += 1
                    print("{:15} {:15} {:15} {}/{}/{}".format(str(i), element.name, element.firstName, 
                            element.registerDate.day, element.registerDate.month, element.registerDate.year))
            main("print_list_registration_alphabetical")

        #In this case, we print the list of registration who is arranged in alphabetical order
        elif step == "print_list_registration_alphabetical":

            print("\nList of entries (arranged in alphabetical order) :\n")
            print("{:15} {:15} {:15} {:15}".format("Number :", "Name :", "First name :", "Date of registration :"))

            if listRegistration == []:
                print("\nNo registrations were entered today.\n")
            else:
                #We create an empty list where we will store our names.
                listName = []
                for element in listRegistration:
                    listName.append(element.name)
                #Then we short it
                sorted_list = sorted(listName)
                #Finaly, we display it
                i = 0
                for element in listRegistration :
                    i += 1
                    print("{:15} {:15} {:15} {}/{}/{}".format(str(i), sorted_list[i-1], element.firstName,
                               element.registerDate.day, element.registerDate.month, element.registerDate.year))
                main("print_list_registration_date")

        elif step == "print_list_registration_date":
            print("\nList of registrations (sorted by date of registration) :\n")
            print("{:15} {:15} {:15} {:15}".format("Number :", "Name :", "First name :", "Date of registration :"))

            if listRegistration == []:
                print("\nNo registrations were entered today.\n")
            else:
                #We create an empty list where we will store our names.
                listDate = []
                for element in listRegistration:
                    listDate.append(element.registerDate.date)
                #Then we short it
                sorted_list = sorted(listDate)
                #Finaly, we display it
                i = 0
                for element in listRegistration :
                    i += 1
                    print("{:15} {:15} {:15} {}/{}/{}".format(str(i), element.name, element.firstName,
                               sorted_list[i-1].day, sorted_list[i-1].month, sorted_list[i-1].year))

                print("\nGoodBye\n")
                sys.exit(0)
        #In this case, we don't know if the user want to add a new registration
        elif chooseRegistration == None:
            #We ask to the user if he want to add a new registration
            chooseRegistration = input("\nWould you like to add a new registration today? (Answer Y for yes or N for no) : ")
            main("new_registration", currentDate, chooseRegistration)
        #In other case
        else:
            main()
    except DayException as e:
        print(e.errorDay)
        main()
    except MonthException as e:
        print(e.errorMonth)
        main()
    except YearException as e:
        print(e.errorYear)
        main()
    except DateException as e:
        print(e.errorDate)
        main()
    except DateSmallerException as e:
        print(e.smallerDate)
        print("\n/!\ New entry deleted /!\ \n")
        reboot("new_registration", currentDate, chooseRegistration, numberRegistration)
    except KeyboardInterrupt:
        print("\nAttempt to register cancelled.")
        main("new_registration", currentDate, chooseRegistration)
    #except Exception as e:
    #    print(e)
    #    print(type(e))

#-------- Starting  ---------
print("\nTP Dates of the POO module in python, Group N°2.")
listRegistration = []
numberRegistration = 0
main(None, None, None, numberRegistration, None, None)
