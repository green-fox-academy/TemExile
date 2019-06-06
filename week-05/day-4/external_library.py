# 2xercise 1
def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(0)
    graph.set_ylabel('Balance')
graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

# Exercise 2
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        racer = racers[i]
        if racer['finish'] == 1:
            # change the iteration itme name
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Exercise 3
def total_point(arr):
    total = 0
    ace = 0
    for i in arr:
        if i in ['J', 'Q', 'K']:
            total += 10
        elif i == 'A':
            ace += 1
        else:
            total += int(i)
    for i in range(ace):
        if (total + 11) >= 21:
            total += 1
        else:
            total += 11
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = total_point(hand_1)
    total_2 = total_point(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)