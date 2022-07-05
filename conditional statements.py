def get_water_bill(num_gallons):
    if num_gallons<= 8000:
        bill = num_gallons*5/1000
    elif num_gallons<=22000:
        bill = num_gallons*6/1000
    elif num_gallons<=30000:
        bill = num_gallons*7/1000
    else:
        bill = num_gallons*10/1000
    return bill

print(get_water_bill(10000))

def get_phone_bill(gb):
    if gb<=15:
        bill = 100
    else:
        bill = 100 + (gb-15)*100
    return bill
print(get_phone_bill(15.1))