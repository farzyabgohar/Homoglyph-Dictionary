#Farzyab Gohar
#Program purpose: Builds a dictionary of homoglyphs and allows translation of simple text to homoglyphs, and manipulation of the dictionary


def mySize(dic): #function that counts total number of values in a list
	size = 0 #initialise
	for key in dic: 
		if type(dic[key]) == list: #while looping through each key-value pair, it checks if the value is a list. If yes, then it goes through another loop where it adds +1 for each element in that list. There are probably other ways of counting total number of values in a dictionary, but this is the only one that came to mind when i was writing the code.
			for value in dic[key]:
				size = size + 1
		else:
			size = size + 1 #only increments size by 1 if only 1 value is found for the current key.
	return size #returns the total size (total number of values in the dictionary)

def myDelete(dic, key):
	if key in dic: #checks if user inputted key is in dictionary. If yes, replaces value of that key with the key itself (this is what the assignment generator said I should do.) Returns True if key present, false if not.
		dic[key] = key
		return True
	else:
		return False

dic_file = open("glyphs.dat", "r") #opens file
dic_data = dic_file.read() #stores contents of file into dic_data
dic_file.close() #Closing the file since I no longer need it. Everything I need is in dic_data
dic_data = dic_data.strip(":%#") #removes unecessary parts
dic_data = dic_data.split("#") #splits all key value pairs

dicx = {} #initialise
for key in dic_data: #stores each key value pair in dicx
	dicx[key[0]] = key[2:len(key)]


flag = True #this flag checks when user enters valid or invalid input. if user enters anything other than the options provided in the menu, flag remains true and loop repeats. If user enters a valid input, then flag is set to false and loop ends.
while flag:
	operation = input("Would you like to \n[t]ranslate\n[d]elete\n[s]ize\n[q]uit\n",)#I'm very proud of the \n's I put here. Makes my menu look nice.
	operation = operation.lower()#Validation 
	if operation == "t":
		user_input = input("Enter string to translate: ")
		user_input = user_input.upper() #validation
		translation = user_input #made a new variable here for manipulation purposes. I didn't want to use the same variable user_input because It would be bad programming practice to overwrite the orignal text.
		for key in dicx:
			flag2 = True #the entire point of this flag is to handle cases where keys in dicx are found in multiple places in the user input. e.g "A" could be repeated multiple times in different positions. This flag is set to False when no more instances of the same key is found, thus ending the loop for that particular key and moving onto the next key.
			while flag2:
				pos = translation.find(key)
				if not(pos == -1): #checks if match with key exists in user input. If not, then it moves to the else part.
					translation = translation[0:pos] + dicx[key] + translation[pos+1:len(translation)] #adds everything up until the position where key match was found, then adds the key value, and everything from that position+1 to the length of the entire user input string.
				else:
					flag2 = False #point of this is to end the loop for the current key if no match or no further match is found in user input
		print (translation)
		flag = False
	elif operation == "d":
		del_key = input ("Enter key to delete: ")
		del_key = del_key.upper() #validation
		print(myDelete(dicx, del_key))
		flag = False
	elif operation == "s":
		print(mySize(dicx))
		flag = False
	elif operation == "q":
		flag = False
	else:
		print("Incorrect input. Please choose one of the 4 operations from the menu below")
	