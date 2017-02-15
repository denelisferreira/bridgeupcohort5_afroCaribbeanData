import sqlite3

# After your database is complete and ready to use,
# Fill in the blanks (the underlined areas) with your
# information.
# From there, follow the instructions from comments
#  with three hashtags ### to add your own code


# Some lines, like these, are not in a function!
# Don't change this code, but think about it for a minute.
# What does that mean?
conn = sqlite3.connect('AMNH_Exhibits_Information.db')
c = conn.cursor()


def menu():
	dbName = "AMNH_Exhibits_Information" #name your database here
	partner1 = "Gertie" #one of your names here
	partner2 = "Denelis" #one of your names here
	print "Welcome to the "+ dbName + " database,"
	print "By " + partner2 + " and " + partner1 + ".\n"

	user_choice = options()

	# We have never seen this 'while' word before!
	# What do you think it does?
	while user_choice != "Q":
		if user_choice == "0":
			exampleQuestion()
		elif user_choice == "1":
			question1()
		elif user_choice == "2":
			question2()
		elif user_choice == "3":
			question3()
		### If you get to creating your own question/s,
		### don't forget to add other elifs here!
		else:
			print "We're sorry, that is not an option."
			print "Please try again"

		print "\n\n"
		user_choice = options()

	print "\nThank you for using our program!"
	print "Have a great day."

def options():
	print "Which question would you like answered (enter the number below)?"
	print "0. Example Question: How many donors have given to this collection?"
	print "1. What techniques were used to create a Potsherd?"
	print "2. Which donors have we exchanged items with, and where did those items come from (what locale)?"
	print "3. What objects were made with clay, outside of Northeast coast of Cuba, Baracoa?"
	print "4. What objects were given as gifts from George G. Heyes and were made of plant fibers?"
	### If you get to creating your own question/s,
	### don't forget to tell the user about it here!
	print "\nPress 'Q' to quit"
	choice = raw_input()
	return choice

def exampleQuestion():
	print "You have chosen to look up how many donors"
	print "have given to this collection.\n"

	query = c.execute("SELECT COUNT(DISTINCT donor) FROM BigTable")
	for row in query:
		print "There are "+ str(row[0]) + " donors in this collection."

def question1():
	print "You have chosen to discover:"
	print "Which techniques have been used to"
	print "create a 'Potsherd'?"
   	print "The technique used is pottery"
   	#SELECT technique FROM Object WHERE obj=Potsherd;
	### Add code here to answer each question

def question2():
	print "You have chosen to discover:"
	print "Which donors have we exchanged items with, and where did those items come from (what locale)?"
   	print "We have exchanged items with the Museum of the American Indian from the Northeast coast of Cuba, and from Baracoa. We have also exchanged items with Harold Courland, and it is unknown where those objects are from"
	#SELECT locale, donor FROM Location WHERE class= 'EXCHANGE';
	### Add code here to answer each question

def question3():
	print "You have chosen to discover:"
	print "What objects were made with clay, outside of Northeast coast of Cuba, Baracoa?"
   	print "Some Potsherds were made with clay from Daquiri cave, and from Baracoa. Some pottery was made from an unknown location. as was a Pot Sherd and a Sherd"
	#SELECT object FROM Object WHERE material='clay' AND Location != Northeast coast of 'Cuba', 'Baracoa';
	### Add code here to answer each question

def question4():
	print "You have chosen to discover:"
	print "What objects were given as a gift from George G. Heyes, and were made of plant fibers?"
	print "Sandals were given as a gift fromo George G. Heyes and were made of plant fibers."
	#SELECT object FROM OBJECT WHERE donor= 'HAYES, GEORGE G.' AND material= 'PLANT FIBER';

### If you get to creating your own question/s,
### make sure to add a new function for each question!



menu()
# Don't forget to close the connection to the database!
# (We don't have to save what we did because we aren't
#  updating our database.)
conn.close()