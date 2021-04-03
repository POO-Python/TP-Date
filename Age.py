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
        day = input("Days : ")
        month = input("Month : ")
        year = input("Year : ")
        class_date = Date(int(day), int(month), int(year))

        #Check if we have errors in our getters
        if class_date.day == "error_day":
            print(class_date.error(class_date.day))
            main()
        elif class_date.month == "error_month":
            print(class_date.error(class_date.month))
            main()
        elif class_date.year == "error_year":
            print(class_date.error(class_date.year))
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