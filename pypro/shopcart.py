foods=[]
prices=[]
total=0
while True:
    food=input("ENter a food to buy (q to quit):").lower()
    if food=='q':
        break
    else:
        price=float(input(f"Enter the price of {food}:$"))
        foods.append(food)
        prices.append(price)

print("________ your cart __________")
for food in foods:
    print(food)

for price in prices:
    total+=price
print(f'your cart price is {total} ')
