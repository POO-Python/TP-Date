#=====================================================================================================================
#  ?  ABOUT
#  @author : Germain LEIGNEL, Thibault BARRAL, Quentin SAR, Jathursan
#  MEHAVARNAN
#  @repo : https://github.com/POO-Python/TP-Date
#  @createdOn : 12/04/2021
#  @description : TP Dates of the POO module in python, Group N°2.
#=====================================================================================================================



#===================================================================================================
#                                          IMPORT AND START
#===================================================================================================
class Date(object):
    
    #-------- Definition of the constructor ---------
    def __init__ (self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

    #-------- Definition of the error method ---------
    def error (self, error):
        if error == "error_day":
            return "\nPlease enter a number of day between the first and the last day of the month."
        elif error == "error_month":
            return "\nPlease enter a number of month between the first and the last month of the year."
        elif error == "error_year":
            return "\nPlease enter a number of year between 1000 and 9999."

    #-------- Definition of the Getters ---------
    @property
    def day(self):
        return self.__day
    @property
    def month(self):
        return self.__month
    @property
    def year(self):
        return self.__year
    


    #-------- Definition of the Setters ---------
    @day.setter
    def day(self, value):
        #If day is not an integer
        if isinstance(value, int) == False:
            raise TypeError
        #If day is not between the first and the last day of the month
        elif  value < 1 or value > 31:
            self.__day = "error_day"
        else:
            self.__day = value

    @month.setter
    def month(self, value):
        #If month is not an integer
        if isinstance(value, int) == False:
           raise TypeError
        #If month is not between the first and the last month of the year
        elif  value < 1 or value > 12:
            self.__month = "error_month"
        else:
            self.__month = value

    @year.setter
    def year(self, value):
        #If year is not an integer
        if isinstance(value, int) == False:
           raise TypeError
        #If year is not between 1000 and 9999 
        elif  value < 1000 or  value > 9999:
           self.__year = "error_year"
        else:
           self.__year = value





