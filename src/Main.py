# -*- coding: utf-8 -*-
import sys
from PlayingCards.Blackjack import Blackjack

MENU_CHOICES_LIST = ["quit", "poker", "blackjack"]


def main():
    choice = ""

    # Menu handling, will finally quit out after a good choice
    while choice not in MENU_CHOICES_LIST:
        choice = input("Hi there! What you wanna do? (Poker/Blackjack/Quit) : ").lower()

        while choice == "poker":
            print("Starting Poker...")
            break

        while choice == "blackjack":
            print("\nNew Blackjack round...")
            blackjack = Blackjack(num_players=int(input("How many are playing? ")))
            blackjack.setup()
            blackjack.play()
            blackjack.console_finish()

            if input("\nWant to do another round? ").lower()[0] != "y":
                break

        if choice == "quit":
            print("Quitting...")
            break

    print("Leaving, all OK...")
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "blackjack":
            players = 2
            cmd_blackjack = Blackjack(num_players=players)
            cmd_blackjack.setup()
            cmd_blackjack.play()
            cmd_blackjack.console_finish()
    else:
        main()
