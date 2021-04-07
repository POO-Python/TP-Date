#=====================================================================================================================
#  ?                                           ABOUT
#  @author         :  Germain LEIGNEL, Thibault BARRAL, Quentin SAR, Jathursan MEHAVARNAN
#  @repo           :  https://github.com/POO-Python/TP-Date
#  @createdOn      :  12/04/2021
#  @description    :  TP Dates of the POO module in python, Group N°2.
#=====================================================================================================================



#===================================================================================================
#                                          IMPORT AND START
#===================================================================================================

from ClassDate import Date
from time import sleep
from ClassDateException import *

#-------- Definition of the reboot function ---------
def reboot():
    print("Reboot in progress.", end = '')
    sleep(1)
    print(".", end = '')
    sleep(1)
    print(".")

#-------- Definition of the calling Date Class function ---------
def call_date_class():
    day = input("Days : ")
    month = input("Month : ")
    year = input("Year : ")
    return Date(int(day), int(month), int(year))

#-------- Definition of the Ask Date of birth function ---------
def ask_birth_date():
    #We ask the day, month, year of the user and we call the class Date
    print("\nEnter your date of birth:\n")
    birth_date = call_date_class()

    #Check if this date exist
    date_existe_state = birth_date.check_day_exist()

    #Display the birthday of the user
    print("\nYour date of birth is : ", birth_date)
    return birth_date

#-------- Definition of the main function ---------
def main(finish_step_1=None):
    try:
        #If the ask_birth_date function has not returned an instance of the Date class then we call it. 
        #After, we call the main function with like parameter the instance of the Date class

        if  isinstance(finish_step_1, Date) == False:
            finish_step_1 = ask_birth_date()
            main(finish_step_1)
        else:
            #In this case we know the birth date of the user

            #We ask a second time, the day, month, year of the user and we call the class Date
            print("\nEnter the date you want to know your age:\n")
            date_know_age = call_date_class()

            #Check if this date exist
            date_existe_state = date_know_age.check_day_exist()

            #Check if the fist date is smaller than the second
            date_know_age.smaller_than_bigger(finish_step_1)

            age = finish_step_1 - date_know_age

            print(age)

    #We generate differente error, then we call the reboot function, at the end we call the main with 
    #the instance of date of birth if it exist
    except ValueError:
        print("\nPlease enter an integer! \n")
        reboot()
        main(finish_step_1)
    except DayException as e:
        print(e.errorDay)
        reboot()
        main(finish_step_1)
    except MonthException as e:
        print(e.errorMonth)
        reboot()
        main(finish_step_1)
    except YearException as e:
        print(e.errorYear)
        reboot()
        main(finish_step_1)
    except DateException as e:
        print(e.errorDate)
        reboot()
        main(finish_step_1)
    except DateBiggerException as e:
        print(e.biggerDate)
        reboot()
        main(finish_step_1)
    except Exception as e:
        print(e)
        print(type(e))
        print("\nAn error has occurred. \n")
        reboot()
        main(finish_step_1)

#-------- Starting  ---------
print("\nTP Dates of the POO module in python, Group N°2.")
main()