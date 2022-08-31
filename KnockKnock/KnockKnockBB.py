""" Knock knock joke machine. Requests the user's name, greets them, then engages in an infinite exchange of knock knock jokes. Several checks to ensure
 that the exchange follows the format of knock knock jokes. When user tells jokes, any input is allowed as long as it starts with knock knock and no empty
 strings are entered."""

# list that holds knock knock joke lead-ins

leadin=["Who","Cow says","A little old lady","Etch","Cash","Mustache","Thank","Yah","Voodoo","KGB","Spell","Canoe","Candice","Boo","Stopwatch","To","Dewey","Lettuce","Mikey","Razor","Olive","Howl","Iran","Needle","Thermos","Water","Annie","A herd","Abby","Amish","Comb","Chick","Cheese","Dishes","Earl","Emma","Fork","Harry","Nose","Police","Yah","Figs","Fiddle","Ish"]

# list that holds corresponding joke punchlines

punchline=["Who who, sounds like there's an owl out there.","No, a cow says mooooo!","I didn't no you could yodel.","Gesundheidt.","No thank you, I'm allergic to nuts.","I mustache you a question, but I'll shave it for later.","You're welcome.","Yahoo? Calm down, it's just a boring joke.","Voodoo you think you are, asking so many questions.","Ve vill ask the questions!","Ok. W-H-0.","Canoe just let me in?","Candice door not open?","Don't cry, it's just a joke.","Stopwatch you're doing and pay attention.","Correct grammar is to WHOM.","Dewey have to keep doing these jokes?","Lettuce in, it's cold out here.","Mikey doesn't work. Open up!","Razor hands and give me all your money!","Aw, thanks. I love you too.","Howl you know unless you open the door.","Iran all the way here, can I have some water?","Needle-il help getting in.","Thermos be a way to open the door.","Water you doing? Open the door!","Annie way you can let me in?","A herd you were home, so I came over.","Abby birthday to you!","Aw, I miss you too.","Comb on down and I'll tell you!","Chick your phone already, I've called three times. ","Cheese a nice girl.","Dishes nice, but I'd rather talk inside.","Earl be glad when you finally open the door.","Emma bit tired of waiting, can you let me in?","Fork-get it, this is hopeless.","Harry up and open the door!","I nose plenty more knock knock jokes.","Please let me in.","Nah, Google is my search engine of choice.","Figs the doorbell, it's broken.","Fiddle make you open the door, I'll do anything.","Sorry, what's the issue?"]

# initialize a variable that will later help move to a new joke

x=0

# ask the user his or her name

name=input("What's your name?\n")

#greet the user

print("Hi, " + name.capitalize() + ". This is a joke machine. Type exit at anytime if you've laughed enough and want to exit. Otherwise, let's tell some jokes!") 

# an infinite loop that allows the user to keep exchanging jokes or leave the program

while(2==2):
	
	# takes in the role of the user in joke exchange, converted to lowercase to make conditionals efficient

	role=input("Do you want to hear a joke or tell a joke?\n").lower()

	# allows the user to quit the program 

	if "exit" in role:
	
		break

	# checks if the user wants to hear a joke

	elif "hear" in role:

		# Greet the user and tell them they're about to hear a joke

		print("I've got a knock-knock joke for you.")

		# Print out "Knock knock" and continue only if the user enters the right format for a knock knock joke
	
		knockKnock=input("Knock knock\n")
		
		# allows the user to quit the program
		
		if "exit" in knockKnock:

                	break
		
		# proceeds only if the convential knock knock joke format is followed

		elif "whos there" in knockKnock.replace("'", "").lower():

			# Print out a new lead in from the list and wait for the user's input

			leadinResponse=input(leadin[x]+"\n")
			
			#allows the user to quit the program

			if "exit" in leadinResponse:

				break
			
			# proceeds only if the conventional knock knock joke format is followed

			elif leadin[x].lower() + " who" in leadinResponse.lower():

                		# Print out corresponding punchline to the joke

                		print(punchline[x])

                        # Make sure that next time a new joke is used

                		x=x+1

                		# Once all the jokes are used, they will be re-used

                		if x==len(leadin):

                        		print("Bummer. I'm all out of jokes. Oh well. I'll just tell 'em all again.")
			
                        		x=0
		
			# Notify the user if the format is wrong and restart the exchange
			
			else:
		
				print("You're supposed to say " + leadin[x]  + " who? Let's try again.")

		# Notify the user if the format is wrong and restart the exchange
		
		else:
	
			print("You're supposed to say 'Who's there?'. Let's try again.")	

	# check if the user wants to tell a joke

	elif "tell" in role:

		# tell the user it's ready to hear a joke

		jokeIntro=input("I'm ready to hear a joke, but it has to be a knock knock joke.\n")

		# allows the user to quit the program

		if "exit" in jokeIntro:

                	break
		
		# proceeds only if the conventional knock knock joke format is followed
		
		elif "knock knock" in jokeIntro.lower():
	
			# respond with who's there

			intro=input("Who's there?\n")

			# allows the user to quit the program

			if "exit" in intro:

                		break
			
			# proceed only if the intro isn't an empty string

			elif ""!=intro.replace(" ",""):

				# respond to the next input with the user's intro, in camel case, and who?

				userPunchLine=input(intro.capitalize() + " who?\n")

				# allows the user to quit the program

				if "exit" in userPunchLine:

                			break
			
				# proceeds if the punchline isn't empty

				elif ""!=userPunchLine.replace(" ",""):

					# tell the user the joke is funny, even if it isn't

					print("Ha ha ha ha ha ha ha- Oh my. That was sooo funny. Good one.")

				# restart the exchange if userPunchLine was empty

				else:

					print("You didn't say a punchline. Let's try again.")
			
			# restart the exchange if the lead in was empty

			else:

				print("You didn't say anything. Let's try again.")

		# Notify the user if the format is wrong and restart the exchange

		else:
	
			print("You're supposed to say 'Knock knock'. Let's try again.")

	# Remind the user to pick a valid role and restart the exchange

	else:
		print("I'm sorry, I only understand the words hear and tell.")
											
# Program ends if the user doesn't feel like exchanging jokes.

print("Good-bye")
