t2production = 78
t3production = 198
<<<<<<< HEAD
pearls = 1
=======
pearls = 2
item =30
>>>>>>> 5a9bc81aeb87d03debd4986f09f989d5047984b2

baseFish = int(input('What is todays current normal fish price? '))

t2Fish = int(input('What is todays current tier 2 fish price? '))
t3Fish = int(input('What is todays current tier 3 fish price? '))
t2combinePrice = baseFish + t2Fish + t2production + pearls
t3combinePrice = baseFish + t3Fish + t3production + pearls
print(f'The crafting cost is tier 2 will be {t2combinePrice} gold')
print(f'The crafting cost is tier 3 will be {t3combinePrice} gold')
t2sellPrice = int(input('How much is the TIER 2 item going for on the market? '))
t3sellPrice = int(input('How much is the TIER 3 item going for on the market? '))
t2itemPrice = t2sellPrice * item
t3itemPrice = t3sellPrice * item
t2TransactionFee = item * 1
t3TransactionFee = item * 1
t2profit = t2itemPrice - (t2combinePrice + t2TransactionFee) 
t3profit = t3itemPrice - (t3combinePrice + t3TransactionFee) 
print(f' Your profit is from Tier 2 is {t2profit} \n Your profit from Tier 3 is {t3profit} gold. ')

