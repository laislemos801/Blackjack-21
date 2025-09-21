import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_playing = True

def sort_initial_cards() -> list[int]:
    chosen_cards = random.choices(cards, k=2)

    return chosen_cards

def sum_cards(cards: list[int]) -> int:
    sum = 0
    for card in cards:
        sum += card

    return sum

def get_another_card(cards: list[int]) -> list[int]:
    new_card = random.choice(cards)
    cards.append(new_card)

    return cards
        

while keep_playing:
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_choice == 'y':
        print(logo)

        user_cards = sort_initial_cards()
        computer_cards = sort_initial_cards()

        user_sum = sum_cards(user_cards)

        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        while user_sum < 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                get_another_card(user_cards)
                user_sum = sum_cards(user_cards)
            elif another_card == 'n':
                pass
            else:
                print("What you typed is not an option. Try again.")
        
    elif user_choice == 'n':
        keep_playing = False

    else:
        print("What you typed is not an option. Try again.")