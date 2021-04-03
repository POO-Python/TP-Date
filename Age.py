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



#-------- Definition of the reboot function ---------
def reboot():
    print("Reboot in progress.", end = '')
    sleep(1)
    print(".", end = '')
    sleep(1)
    print(".")



#-------- Definition of the main function ---------
def main():
    print("\nEnter your date of birth: \n")
    try:
        #We ask the day, month, year of the user and we call the class Date
        day = input("Days : ")
        month = input("Month : ")
        year = input("Year : ")
        class_date = Date(int(day), int(month), int(year))

        #Check if we have errors in our getters and we display it
        if class_date.day == "error_day":
            print(class_date.display(class_date.day))
            main()
        elif class_date.month == "error_month":
            print(class_date.display(class_date.month))
            main()
        elif class_date.year == "error_year":
            print(class_date.display(class_date.year))
            main()

        #Check if a date exist
        date_existe_state = class_date.check_day_exist()
        if date_existe_state == "error_date":
            print(class_date.display(date_existe_state))
            main()

    except ValueError:
        print("Please enter an integer! \n")
        reboot()
        main()
    except Exception as e:
        print(e)
        print(type(e))
        print("An error has occurred. \n")
        reboot()
        main()

#-------- Calling of the main function ---------
print("\nTP Dates of the POO module in python, Group N°2.")
main()