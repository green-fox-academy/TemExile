def should_hit(player_total, dealer_card_val, player_aces):
    if player_total < 14 and player_total > dealer_card_val:
        return True
    elif player_total < 12:
        return True
    elif player_total < 19 and player_aces >= 1:
        return True
    else:
        return False