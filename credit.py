from cs50 import get_string
from cs50 import get_int
import math

number = get_int("Number: ")
string = str(number)
sum1 = 0
sum2 = 0
count = 0
digits = 0

while (number >= 1):
    if (count % 2 == 0):
        sum1 += number % 10

    elif (count % 2 != 0):
        digits = ((number % 10) * 2)
        if (digits < 10):
            sum2 += digits
        else:
            sum2 += (digits % 10) + math.floor(digits / 10)

    number = math.floor(number / 10)
    count = count + 1

sum_total = sum1 + sum2
if ((sum_total) % 10 != 0):
    print("INVALID")

if ((sum_total) % 10 == 0):
    if (string[0] == '3' and (string[1] == '4' or string[1] == '7')) and len(string) == 15:
        print("AMEX")
    if (string[0] == '5' and (string[1] == '1' or string[1] == '2' or string[1] == '3' or string[1] == '4' or string[1] == '5')) and len(string) == 16:
        print("MASTERCARD")
    if (string[0] == '4' and (len(string) == 13 or len(string) == 16)):
        print("VISA")
    else:
        print("INVALID")
