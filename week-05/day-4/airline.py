def pricing_function(days_left, tickets_left, demand_level):
    if demand_level < 150:
        if days_left > 3:
            price = demand_level + 1
        else:
            price = demand_level - 5
    elif demand_level in range(150, 165):
        if days_left > 3:
            price = demand_level - 5
        else:
            price = demand_level - 10
    elif demand_level in range(165, 180):
        price = demand_leve - 20
    else:
        price = demand_level - 50
    return price