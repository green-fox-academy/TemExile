def pricing_function(days_left, tickets_left, demand_level):
    if demand_level < 165 and days_left <= 2:
        if tickets_left > 20:
            price = demand_level - int(tickets_left * 0.4)
        else:
            price = demand_level - tickets_left
    elif demand_level < 165 and days_left > 2:
        if tickets_left > 20:
            price = demand_level + 1
        else:
            price = demand_level + 1
    elif demand_level > 165 and days_left <= 2:
        if tickets_left > 20:
            price = demand_level - int(tickets_left * 0.7)
        else:
            price = demand_level - int(tickets_left * 0.5)
    elif demand_level > 165 and days_left > 2:
        if tickets_left > 20:
            price = demand_level - int(tickets_left * 0.5)
        else:
            price = demand_level - tickets_left
    return price