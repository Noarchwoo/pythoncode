import random
import string

words = string.ascii_letters + string.digits

def  get_coupon(digit):
    conpon = ''
    for i in range(digit):
        conpon += random.choice(words)
    return conpon

def two_hundred_coupons():
    digit = 10
    for i in range(200):
        data = '%03d' % i
        data += get_coupon(digit)
        print(data)

two_hundred_coupons()
