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

from ClassDate import Date
import datetime

class Id(Date):
    
    #-------- Definition of the constructor ---------
    def __init__ (self, register_number, name, first_name, register_day, register_month, register_year):
        
        self.registerNumber = register_number
        self.name = name
        self.firstName = first_name
        self.registerDate = Date(register_day, register_month, register_year)

    #-------- Definition of the Getters ---------
    @property
    def registerNumber(self):
        return self.__registerNumber
    @property
    def name(self):
        return self.__name
    @property
    def firstName(self):
        return self.__firstName
    @property
    def registerDate(self):
        return self.__registerDate

    #-------- Definition of the Setters ---------
    @registerNumber.setter
    def registerNumber(self, value):
        #If day is not an integer
        if isinstance(value, int) == False:
            raise ValueError
        #Other case
        else:
            self.__registerNumber = value

    @name.setter
    def name(self, value):
        #If month is not an integer
        if isinstance(value, str) == False:
           raise ValueError
        #Other case
        else:
            self.__name = value

    @firstName.setter
    def firstName(self, value):
        #If year is not an integer
        if isinstance(value, str) == False:
           raise ValueError
        #Other case
        else:
           self.__firstName = value

    @registerDate.setter
    def registerDate(self, value):
        #If error_date is not an integer
        if isinstance(value, Date) == False:
            raise ValueError
        #Other case
        else:
            self.__registerDate = value





