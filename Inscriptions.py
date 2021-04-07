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
from datetime import date
from ClassDateException import *

#-------- Definition of the reboot function ---------
def reboot(currentDate, chooseRegistration, numberRegistration):
    print("\n/!\ New entry deleted /!\ \n")
    state = input("Do you want to enter another registration date? (Answer Y for yes or N for no) : ")
    if state == "Y" or state == "Yes" or state == "y" or state == "yes":
        main("new_registration", currentDate, chooseRegistration, numberRegistration)


#-------- Definition of the ask new register function ---------
def ask_new_register():
    print("\nTo cancel the registration, press ctrl + c\n")
    name = input('\nName: ')
    first_name = input('First name: ')
    print("\nEnter a registration date: (which cannot be earlier than the current date)")
    register_day = input("\nDays : ")
    register_month = input("Month : ")
    register_year = input("Year : ")
    return name, first_name, register_day, register_month, register_year

#-------- Definition of the main function ---------
def main(step=None, currentDate=None, chooseRegistration=None, numberRegistration=0):
    try:
        #In this case, we have just start the program
        if step == None:
            #We ask the currentDate and we call the date Class
            print("\nEnter today's date :")
            day = input("    Days : ")
            month = input("    Month : ")
            year = input("    Year : ")
            print("\nToday's date is: {0}/{1}/{2}".format(day, month, year))

            #We confirm to the user
            confirmed_state = input("\nDo you confirm this date? (Answer Y for yes or N for no) : ")
            if confirmed_state == "Y" or confirmed_state == "Yes" or confirmed_state == "y" or confirmed_state == "yes":
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

        
        elif step == "new_registration" and currentDate != None and chooseRegistration != None:
            #We ask if the user want to add a new registration today
            if chooseRegistration == "Y" or chooseRegistration == "y" or chooseRegistration == "yes":
                #We ask the name, firstname, registeration date of the user 
                register = ask_new_register()

                registerDate = Date(int(register[2]), int(register[3]), int(register[4]))
               
                #Check if the date of registration is prior to the current date. If it's we raise an error
                #because that means the registerDate is prior to the currentDate.
                registerDate < currentDate

                #We call the class Id and add +1 to the number of registration
                numberRegistration += 1
                registerClass = Id(numberRegistration, register[0], register[1], registerDate)
            else:
                print("\n\n GoodBye...")
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
        reboot()
        main()
    except MonthException as e:
        print(e.errorMonth)
        reboot()
        main()
    except YearException as e:
        print(e.errorYear)
        reboot()
        main()
    except DateException as e:
        print(e.errorDate)
        reboot()
        main()
    except DateSmallerException as e:
        print(e.smallerDate)
        reboot(currentDate, chooseRegistration, numberRegistration)
    except KeyboardInterrupt:
        print("\nAttempt to register cancelled.")
    except Exception as e:
        print(e)
        print(type(e))

#-------- Starting  ---------
print("\nTP Dates of the POO module in python, Group N°2.")
main()
