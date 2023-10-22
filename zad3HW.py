"""Не можах да изкарам останалите 
порички, опитах и стигнах до тук. Постоянно
ми изписваше този ерор ('>' not supported between instances of 'list' and 'int') 
и не знаех как да го опратя.Иначе другото работи"""

food_quantity = int(input())
orders = [int(x) for x in input().split(" ")]

max_order = max(orders)
total_orders = sum(orders)

if total_orders <= food_quantity:
    print(max_order)
    print("Orders complete")
else:
    print(max_order)
    remaining_orders = [str(order) for order in orders if order > food_quantity]
    remaining_orders.append(orders)
    print("Orders left: ".join(remaining_orders))
