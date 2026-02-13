# input 
'''
1.how much rent
2.how much food bill
3.how much electricity unit consume
4.how much price per unit 
5.number of persons 
'''
rent=int(input("Enter the room rent amount: "))
food_bill=int(input("Enter the food  amount: "))
electricity_units=int(input("Enter the consume unit : "))
electricity_per_unit_charge=int(input("Enter the price per unit : "))
person=int(input("Enter the number of person : "))

total_electric_bill=electricity_units*electricity_per_unit_charge

print((rent+food_bill+total_electric_bill)/person)

