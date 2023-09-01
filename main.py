
import phonenumbers

from number import number

from phonenumbers import geocoder

c_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(c_number, "en"))

from phonenumbers import carrier
ser_number = phonenumbers.parse(number, "SP")
print(carrier.name_for_number(ser_number, "en"))







