__author__ = 'Srkn'
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
	print
	"Player chooses", str(player_choice)

def player choice(player_number):
	name_to_number(player_choice)
	return player_number

def comp_number(random.randrange):
	random.randrange(0, 4)
	number_to_name(comp_number)
	return comp_number
	print "Computer's choice:", str(comp_number)

def difference(comp_difference)
	difference = (player_number - comp_number) % 5
	if difference =< 2
	print "Player Wins!"
else:
	print "Computer Wins!"

