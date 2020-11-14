__author__ = 'Srkn'
# Rock-paper-scissors-lizard-Spock mini-project
import random

def name_to_number(name):
    """Converts names to their corresponding number"""
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "We have a problem with names here!!"


def number_to_name(number):
    """Converts numbers to their corresponding name"""
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "We have a problem with numbers here!!"


def rpsls(player_choice):
    """Main Function"""
    print
    print "Player choose:", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer choose:", comp_choice
    difference = (player_number - comp_number) % 5
    if difference == 0:
        print "Tie!"
    elif difference == 1:
        print "Player Wins!"
        return
    elif difference == 2:
        print "Player Wins!"
    else:
        print "Computer Wins!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


http://www.codeskulptor.org/#user39_5IH7RGMXVhda3A4.py