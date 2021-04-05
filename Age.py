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

#-------- Definition of the main function ---------
def main():
    try:
        #We ask the day, month, year of the user and we call the class Date
        print("\nEnter your date of birth:\n")
        day = input("Days : ")
        month = input("Month : ")
        year = input("Year : ")
        birth_date =  Date(int(day), int(month), int(year))

        #Check if a date exist
        date_existe_state = birth_date.check_day_exist()

        #Display the birthday of the user
        print("\nYour date of birth is : ", birth_date)

    except ValueError:
        print("\nPlease enter an integer! \n")
        reboot()
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
    except Exception as e:
        print(type(e))
        print("\nAn error has occurred. \n")
        reboot()
        main()

#-------- Calling of the main function ---------
print("\nTP Dates of the POO module in python, Group N°2.")
main()