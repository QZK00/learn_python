shoplist = ['apple',  'mango', 'carrot', 'banana']
print('i have ', len(shoplist), 'items to purchase')

print('the items are:', end=' ')
for iteams in shoplist:
    print(iteams, end=' ')

print('\ni also have to buy rice')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)