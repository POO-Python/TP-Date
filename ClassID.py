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
from datetime import date

class Id(Date):
    
    #-------- Definition of the constructor ---------
    def __init__ (self, register_number, name, first_name, register_date):
        
        self.registerNumber = register_number
        self.name = name
        self.firstName = first_name
        self.registerDate = register_date

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
        #If registerNumber is not an integer
        if isinstance(value, int) == False:
            raise ValueError
        #Other case
        else:
            self.__registerNumber = value

    @name.setter
    def name(self, value):
        #If name is not an string
        if isinstance(value, str) == False:
           raise ValueError
        #Other case
        else:
            self.__name = value

    @firstName.setter
    def firstName(self, value):
        #If firstName is not an string
        if isinstance(value, str) == False:
           raise ValueError
        #Other case
        else:
           self.__firstName = value

    @registerDate.setter
    def registerDate(self, value):
        #If registerDate is not an instance of the Date Class
        if isinstance(value, Date) == False:
            raise ValueError
        #Other case
        else:
            self.__registerDate = value






