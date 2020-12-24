from itertools import combinations
from random import sample

def check_ticket(winning_set, numbers_on_ticket):
    numbers_on_ticket = list(numbers_on_ticket)
    matches = list(set(winning_set) & set(numbers_on_ticket))

    # Prizes
    winnings = [0, 0, 30, 140, 1750, 15000000]

    # Return matches and winnings for this ticket
    return matches, winnings[len(matches)-1]

if __name__ == '__main__':
    # Define the winning numbers (23rd Dec 2020)
    winning = [20, 42, 48, 51, 52, 54]
    
    # Obtain all possible combinations and generate a random sample
    max_ball_range = 59
    number_combinations = list(combinations(range(1, max_ball_range), 6))
    purchased_tickets = 10000
    tickets = sample(number_combinations, purchased_tickets)
    
    # Calculate winnings
    total_winnings = 0
    for index, ticket in enumerate(tickets):
        matches, value = check_ticket(winning, ticket)

        # You only win oney from 3 or more numbers
        if len(matches) >= 3:
            total_winnings = total_winnings+value
            print(f'{index}: {len(matches)}, £{value} ({matches})')
    
    # Output totals
    print(f'Total winnings of £{total_winnings} against £{purchased_tickets*2} spend = £{total_winnings - (purchased_tickets*2)}')

