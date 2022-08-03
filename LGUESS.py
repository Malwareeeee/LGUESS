import random
from colorama import Fore
import time 
from pyfiglet import figlet_format
import string


def init():
	global invalid
	invalid = []
	fop = open('fifty_list.txt').readlines()
	global word
	word = random.choice(fop).strip()
	global wordlist
	wordlist = [x for x in word]
	global spaces
	spaces = ['_'] * len(word)
	global random_select
	random_select = random.choice(wordlist)
	spaces[word.index(random_select)] = random_select
	global already_guessed
	already_guessed = []
	already_guessed.append(random_select)
	global repetition
	repetition = []
	global rep_indicies 
	rep_indicies = []

def loading_screen():
	try:
		guesses = 13		
		print(Fore.YELLOW + figlet_format('LGUESS'))
		print(Fore.GREEN + "Welcome To LGUESS!")
		print("Hint! Press CTRL + C To Skip Dialogue!")
		print(Fore.WHITE + 'Current Version [Beta 1.3] ')
		print(' ')
		time.sleep(1.5)
		print(Fore.WHITE + "I'll Be Randomly Selecting A Word Out Of 58,000 Common English Words")
		time.sleep(1.5)
		print("Your Job Is To Guess That Word By Guessing Different Letters Until You've Fully Guessed The Word!")
		time.sleep(1.5)
		print("Be Careful Though! You Only Have %s Guesses To Spare!" %(guesses))
		time.sleep(1.5)
		print('\n' * 2)
		print("Lets Begin Playing! Im Thinking Of A %s Letter Word!" %(len(word)))
		time.sleep(1.5)
		rand_let = Fore.RED + str(random_select)
		print(Fore.WHITE + "We'll Give You The Letter",rand_let,Fore.WHITE + 'To Start!')
		print(Fore.GREEN + "You Have %s Guesses Currently!"%(guesses))
	except KeyboardInterrupt:
		print('\n' * 2)
		skip()
		
def win_finale():
	print(' ')
	print(Fore.WHITE + str(spaces))
	print(Fore.GREEN + "You Managed To Finish The Word %s With %s Guesses Left!" %(word,guesses))
	print(Fore.GREEN + "It Took You %s Tries To Complete The Word!" %(attempt_quantity))
	again = input(Fore.GREEN + "Would You Like To Play Again? (Y/N) ")
	if again == 'Yes' or again == 'y' or again == 'Y' or again == 'yes':
		print('')
		print(Fore.GREEN + "Loading It Back Up!")
		time.sleep(1)
		start()
	else:
		print(Fore.GREEN + "See You Next Time!")
		exit()

def game_over():
	print(' ')
	print(Fore.WHITE + str(spaces))
	print(Fore.RED + "You Failed To Guess The Word With %s Guesses" %(guesses))
	print(Fore.RED + "The Mystery Word Was: %s" %(word))
	print(Fore.RED + "It Took You %s Attempts To Try And Complete The Word"%(attempt_quantity))
	again = input(Fore.GREEN + "Would You Like To Play Again? (Y/N) ")
	if again == 'Yes' or again == 'y' or again == 'Y' or again == 'yes':
		print(Fore.GREEN + "Loading It Back Up!")
		time.sleep(1)
		start()
	else:
		print(Fore.GREEN + "See You Next Time!")
		exit()

def dup_word(dupwr):
	if guesses == 0:
		game_over()
	else:
		pass
	for i in rep_indicies:
		if word[i] == guess:
			spaces[i] = guess
	if dupwr in already_guessed:
		print(' ')
		print(Fore.GREEN + "The Letter %s Was Already Guessed!" %(dupwr))
		guesses + 1
		print(Fore.GREEN + 'You Have %s Guesses Left!' %(guesses))
	else:
		print(' ')
		print(Fore.YELLOW + '%s Is In The Word!' %(guess))
		print(Fore.YELLOW + "You Have %s Guesses Left!" %(guesses))
		already_guessed.append(dupwr)

def reg_word(regwr):
	if guesses == 0:
			game_over()
	else:
			ind = word.index(regwr)
			spaces[ind] = regwr
	if regwr in already_guessed:
		print(' ')
		print(Fore.GREEN + "The Letter %s Was Already Guessed!" %(regwr))
		guesses + 1
		print(Fore.GREEN + 'You Have %s Guesses Left!' %(guesses))
	else:
		print('  ')
		print(Fore.YELLOW + "%s Is In The Word!" %(regwr))
		print(Fore.YELLOW + "You Have %s Guesses Left!" %(guesses))
		already_guessed.append(regwr)
		
def is_guess_in_word(gss):
	if gss in word:
		return True
	else:
		return False

def main_loop():
	global attempt_quantity 
	attempt_quantity = 0
	global guesses
	guesses = 13
	for i in word:
		if word.count(i) > 1:
			repetition.append(i)
	for i in range(0,len(word)):
		if word[i] in repetition:
			rep_indicies.append(i)
	while guesses > 0:
		if ''.join(spaces) == word:
			win_finale()
		else:
			pass
		print(Fore.WHITE + str(spaces))
		global guess
		guess = input(Fore.WHITE + "Enter Your Guess: ")
		try:
			if int(guess) or int(guess) == 0:
				print(' ')
				print(Fore.RED + "This Character %s Isn't Valid!" %(guess))
				print(Fore.RED + 'You Have %s Guesses Left!' %(guesses))
				continue 
		except Exception:
			if guess == '':
				print('')
				print(Fore.RED + "This Character %s Isn't Valid!" %(guess))
				print(Fore.RED + "You Have %s Guesses Left!" %(guesses))
				continue
			else:
				pass
		if is_guess_in_word(guess):
			attempt_quantity += 1
			guesses += 1
			if guess in repetition:
				guesses -= 1
				dup_word(guess)
			else:
				guesses -= 1
				reg_word(guess)
		else:
			if ''.join(spaces) == word:
				win_finale()
			else:
				pass
			guesses -= 1
			if guesses == 0:
				game_over()
			else:
				pass
			attempt_quantity += 1
			strn = string.ascii_lowercase
			if len(guess) > 1:
				guesses += 1
				print('')
				print(Fore.RED + "Single Characters Only!")
				print(Fore.RED + "You Have %s Guesses Left!" %(guesses))
				continue
			if not guess in strn:
				guesses += 1
				print(' ')
				print(Fore.RED + "This Character %s Isn't Valid!" %(guess))
				print(Fore.RED + "You Have %s Guesses Left!" %(guesses))
				continue
			if guess in already_guessed:
				print(' ')
				print(Fore.GREEN + "The Letter %s Was Already Guessed!" %(guess))
				guesses += 1
				print(Fore.GREEN + 'You Have %s Guesses Left!' %(guesses))
			else:
				print(' ')
				print(Fore.RED + "%s Is Not In The Word!" %(guess))
				print(Fore.RED + "You Have %s Guesses Left!" %(guesses))
				already_guessed.append(guess)

def skip():
	init()
	guesses = 13
	print("Lets Begin Playing! Im Thinking Of A %s Letter Word!" %(len(word)))
	rand_let = Fore.RED + str(random_select)
	print(Fore.WHITE + "We'll Give You The Letter",rand_let,Fore.WHITE + 'To Start!')
	print(Fore.GREEN + "You Have %s Guesses Currently!"%(guesses))
	main_loop()

def start():
	init()
	loading_screen()
	main_loop()

if __name__ == '__main__':
	start()
