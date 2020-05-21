import re

countryList = ['Russia','Finland','Britain','France','Germany','Spain','Italy']

class NewRegistration():
    def __init__(self, fname, lname, email, affil, year, country, city, postalCode, adress, hdyk):
        try:
            arg1 = self.__fname_check(fname)
            arg2 = self.__lname_check(lname)
            arg3 = self.__email_check(email)
            arg4 = self.__affil_check(affil)
            arg5 = self.__year_check(year)
            arg6 = self.__country_check(country)
            arg7 = self.__city_check(city)
            arg8 = self.__postalCode_check(postalCode)
            arg9 = self.__adress_check(adress)
            arg10 = self.__hdyk_check(hdyk)
        except ValueError as e:
            print(f'Неверная запись: {e}')
        else:
            self.fname = arg1
            self.lname = arg2
            self.email = arg3
            self.affil = arg4
            self.year = arg5
            self.country = arg6
            self.city = arg7
            self.postalCode = arg8
            self.adress = arg9
            self.hdyk = arg10
            print('Ваша заявка принята')

    def __fname_check(self, value):
        if len(value) < 2:
            raise ValueError('Параметр First Name должен содержать не менее 2 символов')
        if re.search('[0-9]', value) != None:
            raise ValueError('Параметр First Name не должен содержать цифр')
        return value
    
    def __lname_check(self, value):
        if re.search('[0-9]', value) != None:
            raise ValueError('Параметр Last Name не должен содержать цифр')
        return value
    
    def __email_check(self, value):
        if re.fullmatch(r'[\w.-]+@[\w.-]+\.?[\w]+?',value) == False:
            raise ValueError('Неверно введен параметр Email')
        return value
            
    def __affil_check(self, value):
        if value.find('University') == -1:
            raise ValueError('Параметр Affiliation должен содержать слово "University"')
        return value
    
    def __year_check(self, value):
        if int(value) < 1900 and int(value) > 2015:
            raise ValueError('Невозможное значение параметра Year of birth')
        return value
    
    def __country_check(self, value):
        if value not in countryList:
            raise ValueError('Данная страна не принимает участие в конференции')
        return value
    
    def __city_check(self, value):
        if re.search('[0-9]', value) != None:
            raise ValueError('Параметр City не должен содержать цифр')
        if len(value) < 4:
            raise ValueError('Параметр City должен содержать не менее 4 символов')
        return value
    
    def __postalCode_check(self, value):
        if len(value) < 6:
            raise ValueError('Параметр Postal Code должен содержать не менее 6 цифр')
        if re.search('\D',value) != None:
            raise ValueError('Параметр Postal Code должен состоять только из цифр')
        return value
    
    def __adress_check(self, value):
        re.fullmatch('st.[\w]+?, [\d]+?', value) == False:
            raise ValueError('Неверно введен параметр Adress. Введите его по шаблону "st. NameOfStreet, NumberOfHouse"')
        return value
    
    def __hdyk_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр "How Did You Know About Us?"')
        return value

new_form = NewRegistration('Anna','Piterson','fuflya12@yahoo.com','Herzen University','1999', 'Russia', 'St.Petersburg', '196521', 'st. Vishnevskogo, 52', 'Internet')
# https://trinket.io/python3/ed41c9c244
# https://trinket.io/python3/fbd996a9df


# class User():
#   def __init__(self):
#     self.__email = ""
#     self.__password = ""
#     
#   @property
#   def email(self):
#     return self.__email
#     
#     
#   @email.setter
#   def email(self, new_email):
#     # проверка email на валидность
#     self._email = new_email
# 
# 
#   def __del__(self):
#     print('Deleting object ... done')
# 
# # u1 = User()
# # print('other way to delete object')
# # u1 = '' 
# 
# # del u1