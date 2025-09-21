# Blackjack Game 🃏

A **terminal-based Blackjack game** written in Python, where you play against a computer dealer.  
Follow classic Blackjack rules and try to get as close to 21 as possible without going over!

---

## Features

- Command-line interface with clear prompts.
- Player can choose to **draw another card** or **pass**.
- Automatic handling of **Ace** (`11` → `1`) if the total exceeds 21.
- Computer dealer draws cards until reaching at least 17.
- Round reset with screen clearing for smooth gameplay.
- ASCII art logo for a fun retro feel.

---

## How to Play

1. Run the game.
2. You will start with 2 cards, and the computer will reveal one card.
3. Decide whether to draw another card (y) or pass (n).
4. After your turn, the computer will draw until reaching at least 17.
5. The winner is the one with the closest score to 21 without going over.

## Example Gameplay
```bash
Do you want to play a game of Blackjack? Type 'y' or 'n': y
     Your cards: [10, 7], current score: 17
     Computer\'s first card: 9

Type 'y' to get another card, type 'n' to pass: n
     Your final hand: [10, 7], final score: 17
     Computer\'s final hand: [9, 8], final score: 17
It\'s a Draw!
```
## Installation

No special installation is required. Just make sure you have Python 3 installed.
Clone the repository:
```bash
git clone https://github.com/laislemos801/Blackjack-21.git
cd blackjack
```
Run the game:
```bash
python blackjack.py
```

## License
This project is open-source and available under the MIT License.
