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

from ClassDateException import *
import datetime

class Date(object):
    
    #-------- Definition of the constructor ---------
    def __init__ (self, day=1, month=1, year=1000):

        self.day = day
        self.month = month
        self.year = year
        self.error = ""
        self.date = datetime.datetime(self.year, self.month, self.day)

    #-------- Definition of the check year is a leap method ---------
    def check_year_is_leap (self, year):
        #
        #         We check if the date can be a leap yer. If it's we return
        #         True and if isn't we return False.
        #
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
        #       
        #         We check if the date is a leep year and if it isn't
        #         We raise an error because the date doesn't exist
        #         
        #         Ex n°1 : 29/2/2000 => Correct
        #         Ex n°2 : 29/2/2000 => Inccorect
        #
        if self.day >= 29:
            if self.month == 2:
                state_year = self.check_year_is_leap(self.year)
                if state_year == False:
                    raise DateException

    #-------- Definition of the representation of the object ---------
    def __str__(self):
        #
        #         We display the date of birth with format: day/month/year
        #
        #
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

    #-------- Definition of "smaller than bigger" method ---------
    def smaller_than_bigger(self, d2):
        #
        #Ex n°1 : In this case, the date of birth is 5/4/2021 and the date where we
        #         want to know of the user is 31/1/2000.
        #         We raise an error because, the year of the date of birth is bigger 
        #         than the year of the date which the user has entered.
        #         (Cf line XX)
        #
        #       Ex: 31/1/2000 then 5/4/2021 : Correct
        #       Ex: 5/4/2021 then 31/1/2000 : Incorrect
        #
        if self.year < d2.year:
            raise DateBiggerException
        #
        #Ex n°2 : In this case, the date of birth is 5/4/2021 and the date where we
        #         want to know the age of the user is 31/1/2021.
        #         We raise an error because, the month of the date of birth is bigger than
        #         the month of the age of the date which the user has entered.
        #         (Cf line XX)
        #
        #       Ex: 31/1/2021 then 5/4/2021 : Correct
        #       Ex: 5/4/2021 then 31/1/2021 : Incorrect
        # 
        if self.year == d2.year:     
            if self.month < d2.month:
                raise DateBiggerException
        #
        #Ex n°3 : In this case, the date of birth is 5/4/2021 and the date where we
        #         want to know the age of the user is 4/4/2021.
        #         We raise an error because, the day of the date of birth is bigger than
        #         the day of the age of the date which the user has entered.
        #         (Cf line XX)
        #
        #       Ex: 4/4/2021 then 5/4/2021 : Correct
        #       Ex: 5/4/2021 then 4/4/2021 : Incorrect
        #
            elif self.month == d2.month:
                if self.day < d2.day :
                    raise DateBiggerException
            

    #-------- Definition of the age calculation method --------- 
    def __sub__(self, d1):

       #This is the numbers of days since the beginning of the year
       nbr_day_since_birth = d1.date.strftime("%j")
       nbr_day_since_now = self.date.strftime("%j")

       #This is the total numbers of days
       nbr_day_total_birth = d1.year * 365.2425 + int(nbr_day_since_birth)
       nbr_day_total_now = self.year * 365.2425 + int(nbr_day_since_now)

       #This is the numbers of days between two dates
       difference = round(nbr_day_total_birth - nbr_day_total_now, 4)

       #We convert result in year and number of days
       convert = round(difference / 365.2425, 4)
       result = str(convert).split('.')

       #As we split convert into a list of two indexes.
       #The second index is a number > 1
       #So as we round the result to the tenth of a thousandth then we divide the second indexes by 10 000
       result[1] = int(result[1]) / 10000

       nbr_years = result[0]
       nbr_day = round(result[1] * 365.2425, 1)
       format_date = str(d1.day) + "/" + str(d1.month) + "/" + str(d1.year) 

       return "\nLe " +  format_date + ", votre âge est de " + nbr_years + " ans et " + str(nbr_day) + " jours (à un jour près)."

    #-------- Definition of the method which overloads the operator strictly prior to   ---------
    def __lt__(self, currentDate):
        #
        #Ex n°1 : In this case, the date has entered by user is 5/4/2000 and the current date is 7/4/2021.
        #         We raise an error because, the year of the date who is entered by user is smaller 
        #         than the year of the current date.
        #
        #       Ex: 7/4/2021 then 5/4/2000 : Correct
        #       Ex: 5/4/2000 then 7/4/2021 : Incorrect
        #
        if self.year < currentDate.year:
            raise DateSmallerException
        #
        #Ex n°2 : In this case, the date has entered by user is 5/2/2021 and the current date is 7/4/2021.
        #         We raise an error because, the month of the date who is entered by user is smaller 
        #         than the month of the current date.
        #
        #       Ex: 7/4/2021 then 5/2/2021 : Correct
        #       Ex: 5/2/2021 then 7/4/2021 : Incorrect
        # 
        if self.year == currentDate.year:
            if self.month < currentDate.month:
                raise DateSmallerException
        #
        #Ex n°3 : In this case, the date has entered by user is 2/4/2021 and the current date is 7/4/2021.
        #         We raise an error because, the day of the date who is entered by user is smaller 
        #         than the day of the current date.
        #
        #       Ex: 7/4/2021 then 2/4/2021 : Correct
        #       Ex: 2/4/2021 then 7/4/2021 : Incorrect
        #
            elif self.month == currentDate.month:
                if self.day < currentDate.day :
                    raise DateSmallerException
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
    @property
    def date(self):
        return self.__date

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
    @date.setter
    def date(self, value):
        #If self.date is not a date
        if isinstance(value, datetime.datetime) == False:
            raise ValueError
        #Other case
        else:
            self.__date = value





