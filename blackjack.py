import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_playing = True

def sort_initial_cards() -> list[int]:
    chosen_cards = random.choices(cards, k=2)

    return chosen_cards

def sum_cards(hand: list[int]) -> int:
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

def get_another_card(current_cards: list[int]) -> list[int]:
    new_card = random.choice(cards)
    current_cards.append(new_card)

    return current_cards

def print_final_hands(user_cards: list[int], user_sum: int, computer_cards: list[int], computer_sum: int):
    print(f"     Your final hand: {user_cards}, final score: {user_sum}")
    print(f"     Computer's final hand: {computer_cards}, final score: {computer_sum}")

def check_winner(user_cards: list[int], user_sum: int, computer_cards: list[int], computer_sum: int):
    while computer_sum < 17:
        computer_cards = get_another_card(computer_cards)
        computer_sum = sum_cards(computer_cards)

    if user_sum > 21:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("\nYou went over. You lose :(")

    elif computer_sum > 21:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("\nOpponent went over. You win :)")

    elif user_sum == computer_sum:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("\nIt's a Draw!")

    elif user_sum > computer_sum:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("\nYou win! :)")

    elif user_sum < computer_sum:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("\nYou lose :(")

    else:
        None

def clear():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac/Linux
    else:
        os.system('clear')

while keep_playing:
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if user_choice == 'y':
        clear()
        print(logo)

        user_cards = []
        computer_cards = []
        user_sum = 0
        computer_sum = 0

        user_cards = sort_initial_cards()
        computer_cards = sort_initial_cards()

        user_sum = sum_cards(user_cards)
        computer_sum = sum_cards(computer_cards)

        print(f"     Your cards: {user_cards}, current score: {user_sum}")
        print(f"     Computer's first card: {computer_cards[0]}")

        keep_getting_cards = True

        while keep_getting_cards:
            another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                new_cards = get_another_card(user_cards)
                user_sum = sum_cards(new_cards)

                if user_sum > 21:
                    check_winner(user_cards, user_sum, computer_cards, computer_sum)
                    keep_getting_cards = False

                else:
                    print(f"     Your cards: {user_cards}, current score: {user_sum}")
                    print(f"     Computer's first card: {computer_cards[0]}")

            elif another_card == 'n':
                check_winner(user_cards, user_sum, computer_cards, computer_sum)
                keep_getting_cards = False
            else:
                print("\nWhat you typed is not an option. Try again.\n")

    elif user_choice == 'n':
        keep_playing = False

    else:
        print("\nWhat you typed is not an option. Try again.\n")