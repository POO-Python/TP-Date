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

from ClassDateException import *

class Date(object):
    
    #-------- Definition of the constructor ---------
    def __init__ (self, day=1, month=1, year=1000):

        self.day = day
        self.month = month
        self.year = year
        self.error = ""

    #-------- Definition of the check year is a leap method ---------
    def check_year_is_leap (self, year):

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    #-------- Definition of the check day exist method ---------
    def check_day_exist (self):
        if self.day <= 29:
            if self.month == 2:
                state_year = self.check_year_is_leap(self.year)
                if state_year == False:
                    raise DateException

    #-------- Definition of the representation of the object ---------
    def __str__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)


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
    @property
    def error(self):
        return self.__error

    #-------- Definition of the Setters ---------
    @day.setter
    def day(self, value):
        #If day is not an integer
        if isinstance(value, int) == False:
            raise ValueError
        #If day is not between the first and the last day of the month
        elif  value < 1 or value > 31:
            raise DayException
        #Other case
        else:
            self.__day = value

    @month.setter
    def month(self, value):
        #If month is not an integer
        if isinstance(value, int) == False:
           raise ValueError
        #If month is not between the first and the last month of the year
        elif  value < 1 or value > 12:
            raise MonthException
        #Other case
        else:
            self.__month = value

    @year.setter
    def year(self, value):
        #If year is not an integer
        if isinstance(value, int) == False:
           raise ValueError
        #If year is not between 1000 and 9999 
        elif  value < 1000 or  value > 9999:
           raise YearException
        #Other case
        else:
           self.__year = value
    @error.setter
    def error(self, value):
        #If error_date is not an integer
        if isinstance(value, str) == False:
            raise ValueError
        #If the day is greater than 29 and the month is Febryary
        if self.day > 29 and self.month == 2:
            raise DateException
        #Other case
        else:
            self.__error = value





