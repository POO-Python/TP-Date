#=====================================================================================================================
#  ?  ABOUT
#  @author : Clément LO-CASCIO, Thibault BARRAL, Quentin SAR, Jathursan
#  MEHAVARNAN
#  @repo : https://github.com/POO-Python/TP-Date
#  @createdOn : 12/04/2021
#  @description : TP Dates of the POO module in python, Group N°2.
#=====================================================================================================================

class DayException(Exception):

    #-------- Definition of the constructor ---------
    def __init__ (self):

        self.errorDay = "\nPlease enter a number of day between the 1 and the 31 day of a month.\n"
    
    #-------- Definition of the Getters ---------
    @property
    def errorDay(self):
        return self.__errorDay

    #-------- Definition of the Setters ---------
    @errorDay.setter
    def errorDay (self, value):
        #If errorDay is not an string
        if isinstance(value, str) == False:
            raise ValueError
        #In other case
        else:
            self.__errorDay = value

class MonthException(Exception):

    #-------- Definition of the constructor ---------
    def __init__ (self):

        self.errorMonth = "\nPlease enter a number of month between the 1 and 12 month of a year.\n"
    
    #-------- Definition of the Getters ---------
    @property
    def errorMonth(self):
        return self.__errorMonth

    #-------- Definition of the Setters ---------
    @errorMonth.setter
    def errorMonth (self, value):
        #If errorMonth is not an string
        if isinstance(value, str) == False:
            raise ValueError
        #In other case
        else:
            self.__errorMonth = value

class YearException(Exception):

    #-------- Definition of the constructor ---------
    def __init__ (self):

        self.errorYear = "\nPlease enter a number of year between 1000 and 9999.\n"
    
    #-------- Definition of the Getters ---------
    @property
    def errorYear(self):
        return self.__errorYear

    #-------- Definition of the Setters ---------
    @errorYear.setter
    def errorYear (self, value):
        #If errorYear is not an string
        if isinstance(value, str) == False:
            raise ValueError
        #In other case
        else:
            self.__errorYear = value

class DateException(Exception):

    #-------- Definition of the constructor ---------
    def __init__ (self):

        self.errorDate = "\nThis date does not exist.\n"
    
    #-------- Definition of the Getters ---------
    @property
    def errorDate(self):
        return self.__errorDate

    #-------- Definition of the Setters ---------
    @errorDate.setter
    def errorDate (self, value):
        #If errorDate is not an string
        if isinstance(value, str) == False:
            raise ValueError
        #In other case
        else:
            self.__errorDate = value

class DateBiggerException(Exception):

    #-------- Definition of the constructor ---------
    def __init__ (self):

        self.biggerDate = "\nThis date is earlier than your date of birth.\n"
    
    #-------- Definition of the Getters ---------
    @property
    def errorDate(self):
        return self.__biggerDate

    #-------- Definition of the Setters ---------
    @errorDate.setter
    def errorDate (self, value):
        #If errorDate is not an string
        if isinstance(value, str) == False:
            raise ValueError
        #In other case
        else:
            self.__biggerDate = value

class DateSmallerException(Exception):

    #-------- Definition of the constructor ---------
    def __init__ (self):

        self.smallerDate = "\nThis date is earlier than the current date.\n"
    
    #-------- Definition of the Getters ---------
    @property
    def errorDate(self):
        return self.__smallerDate

    #-------- Definition of the Setters ---------
    @errorDate.setter
    def errorDate (self, value):
        #If errorDate is not an string
        if isinstance(value, str) == False:
            raise ValueError
        #In other case
        else:
            self.__smallerDate = value
