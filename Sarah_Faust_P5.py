#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#-------------------------------------------------------------------------------
# Student Name: Sarah Faust / Assignment: P5 / Date: 11/07/2012
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: None other than Piazza
#-------------------------------------------------------------------------------
# Comments: None
#-------------------------------------------------------------------------------
# Pseudocode:
#BEGIN
#	function 1:
#		MyFile=open(fileName, "r")
#		MyFile.read()
#		copy file into dictionary
#		close file
#		return whether done or not
#	function 2:
#		write to dictionary
#		return dictionary
#	function 3:
#		search dictionary for e-mail
#		delete name&e-mail from dictionary
#		print whether deleted or not found (or return)
#	function 4:
#		open/create csv file
#		write dictionary to file
#		close the file
#		return whether done or not
#	function 5:
#		organize names into list alphabetically
#		print contents of list
#		return none
#	function 6:
#		organize emails into list alphabetically
#		print contents of list
#		return none
#	function 7:
#		search e-mail in dictionary
#		print name or not found, or return
#	function 8:
#		search name in dictionary
#		print all e-mails or not found, or return
#	function 9:
#		search name
#		print matching names-and-emails
#		search e-mail
#		print matching names-and-emails
#		return none
#	run=-1
#	while run!=10:
#		Answer=-1
#		while Answer<1 and Answer>10:
#			print Menu
#			Answer=int(input(menu choice))
#		if Answer==1:
#			FileName="Nyeh"
#			temp=".csv"
#			while (FileName.endswith(temp))==False:
#				FileName=input(ask for file name)
#			call function 1(FileName)
#		if Answer==2:
#			Name=input(ask for name)
#			Email=input(ask for e-mail address)
#			call function 2(FileName, Name, Email)
#		if Answer==3:
#			Email=input(ask for e-mail)
#			call function 3(FileName, Email)
#		if Answer==4:
#			Name=input(ask for file name)
#			call function 4(FileName, Name)
#		if Answer==5:
#			call function 5
#		if Answer==6:
#			call function 6
#		if Answer==7:
#			Email=input(ask for e-mail)
#			call function 7(Email)
#		if Answer==8:
#			Name=input(ask for name)
#			call function 8(Name)
#		if Answer==9:
#			Name=input(ask user for name)
#			Email=input(ask user for e-mail)
#			call function 9(Name, Email)
#		else:
#			print("Goodbye!")
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#Copies a file into a dictonary named Address
def OpenFile(fileName):
	Address={12:1}
	MyFile=open(fileName, "r")
	FileList=MyFile.readlines()
	for aLine in FileList:
		#A line from the file is copied into a list and cleaned up
		TempList=aLine.split('","')
		TempList[1]=TempList[1].replace("\n","")
		TempList[0]=TempList[0].replace('"','')
		TempList[0]=TempList[0].capitalize()
		TempList[1]=TempList[1].replace('"','')
		TempList[1]=TempList[1].capitalize()
		#Contents move from the list into the dictionary
		Address[TempList[0]]=TempList[1]
	MyFile.close()
	del Address[12]
	return Address
#-------------------------------------------------------------------------------	
#Adds a name and an email into the dictionary
def add(Address, name, email):
	name=name.capitalize()
	email=email.capitalize()
	Address[email]=name
	return Address
#------------------------------------------------------------------------------
#Removes and email and a name from the dictionary
def remove(Address, email):
	email=email.capitalize()
	Check="n"
	for (k) in Address.keys():
		if (email in k)==True:
			del Address[k]	
			print("It had been Removed.")
			Check="y"
			break
	if Check=="n":
		print("Email was not found.")		
	return Address
#-------------------------------------------------------------------------------
#Copies the dictionary into a new file named by the user
def addressbook(Address, name):
	NewFile=open(name, "w")
	for (k,v) in Address.items():
		NewFile.write('"'+k+'"'+","+'"'+v+'"\n')
	NewFile.close()
	return 
#-------------------------------------------------------------------------------
#Prints out the names (with emails) alphabetically
def NameList(Address):
	Order=[]	#lists the names alphabetically
#Check makes sure if the the Order list has a starting value to compare with
	Check="n"
	for v in Address.values():
	#Check allows comparisons once Order has at least one value to use
		if Check=="y":
			char1=v[0]
			isSmaller=[] #for values/names that are smaller (x,y,z)
			isLarger=[]  #for values/names that are larger (a,b,c)
	 #This loop runs through Order, comparing v (a name from Address) to 
	 #every name Order has already collected
			for index in range(len(Order)):
				word=Order[index]
				char2=word[0]
				count=0
		#the first letters of v and a name from Order are compared
				if char1<char2:
					TempList=[index]
					#name from order goes after v
					isSmaller=isSmaller+TempList
				if char1>char2:
					TempList=[index]
					#name from order goes before v
					isLarger=isLarger+TempList
		#Goes down the line of letters, searching to compare
				while char1==char2:
					count+=1
				#if v or word (name from Order)run out of
				#letters to compare, then they go before
				#the longer one alphabetically
					if count>=len(v):
						TempList=[index]
						isSmaller=isSmaller+TempList
						char1="1000" #breaks the loop
					elif count>=len(word):
						TempList=[index]
						isLarger=isLarger+TempList
						char2="1000" #breaks the loop
					else:
		#Rolls down the line of letters until it finds two different 
		#letters, and then compares them like normal
						char1=v[count]
						char2=word[count]
						if char1<char2:
							TempList=[index]
							isSmaller=isSmaller+TempList
						if char1>char2:
							TempList=[index]
							isLarger=isLarger+TempList
                        #if the smaller list is empty, v is the smallest
			if isSmaller==[]:
				TempList=[v]
				Order=Order+TempList
			#if the larger list is empty, v is the largest
			elif isLarger==[]:
				Order.insert(0,v)	
			#otherwise, v always take the place of the first
			#name/index in smaller
			else:
				index=isSmaller[0]
				Order.insert(index,v)
	#Check has the first values from the dict. Address put into Order
	#for it to compare with
		if Check=="n":
			Order.insert(0,v)
			Check="y"
		
	CountV=0
	CountK=0
#Counts the character length of each value and key, records the longest of each
	for (k,v)in Address.items():
		if CountK<=(len(k)):
			CountK=len(k)
		if CountV<=(len(v)):
			CountV=len(v)
#Bases the character box (the box of space every key and value will fit into)
#off of the largest key or value
	if CountV<CountK:
		Box=CountK
	if CountK<CountV:
		Box=CountV
	
	index=[]
	count=0
#Two loops check for repeats in Order, the indexes of the repeats are put in a list
	for n in range(len(Order)):
		for n2 in range(n+1,(len(Order)-1)):
			if Order[n]==Order[n2]:
				index.insert(count,n)
				count+=1
				break
#The repeats are deleted from the list
	count=0			
	for n in index:
		del Order[n-count]
		count+=1
#Each name is printed with it's email(s) in alphabetical order and within 
#the character box set on the largest key/value
	for n in range(len(Order)):
		Word = Order[n]
		for (k,v) in Address.items():
			if v==Word:
				print("{:<{x}}".format(Word, x=Box),end="")
				print("{:<{x}}".format(k, x=Box))
	return 
#-------------------------------------------------------------------------------	
#Prints out the emails (with names) alphabetically
def EmailList(Address):
	Order=[]	#lists the emails alphabetically
#Check makes sure if the the Order list has a starting value to compare with
	Check="n"
	for k in Address.keys():
	#Check allows comparisons once Order has at least one value to use
		if Check=="y":
			char1=k[0]
			isSmaller=[] #for keys/emails that are smaller (x,y,z)
			isLarger=[]  #for keys/emails that are larger (a,b,c)
	 #This loop runs through Order, comparing k (an email from Address) to 
	 #every email Order has already collected
			for index in range(len(Order)):
				word=Order[index]
				char2=word[0]
				count=0
		#the first letters of k and an email from Order are compared
				if char1<char2:
					TempList=[index]
					#email from order goes after k
					isSmaller=isSmaller+TempList
				if char1>char2:
					TempList=[index]
					#email from order goes before k
					isLarger=isLarger+TempList
		#Goes down the line of letters, searching to compare
				while char1==char2:
					count+=1
				#if k or word (email from Order)run out of
				#letters to compare, then they go before
				#the longer one alphabetically
					if count>=len(k):
						TempList=[index]
						isSmaller=isSmaller+TempList
						char1="1000" #breaks the loop
					elif count>=len(word):
						TempList=[index]
						isLarger=isLarger+TempList
						char2="1000" #breaks the loop
					else:
		#Rolls down the line of letters until it finds two different 
		#letters, and then compares them like normal
						char1=k[count]
						char2=word[count]
						if char1<char2:
							TempList=[index]
							isSmaller=isSmaller+TempList
						if char1>char2:
							TempList=[index]
							isLarger=isLarger+TempList
                        #if the smaller list is empty, k is the smallest
			if isSmaller==[]:
				TempList=[k]
				Order=Order+TempList
			#if the larger list is empty, k is the largest
			elif isLarger==[]:
				Order.insert(0,k)	
			#otherwise, k always take the place of the first
			#email/index in smaller
			else:
				index=isSmaller[0]
				Order.insert(index,k)
	#Check has the first key from the dict. Address put into Order
	#for it to compare with
		if Check=="n":
			Order.insert(0,k)
			Check="y"

	CountV=0
	CountK=0
#Counts the character length of each value and key, records the longest of each
	for (k,v)in Address.items():
		if CountK<=(len(k)):
			CountK=len(k)
		if CountV<=(len(v)):
			CountV=len(v)

#Bases the character box (the box of space every key and value will fit into)
#off of the largest key or value
	if CountV<CountK:
		Box=CountK+1
	if CountK<CountV:
		Box=CountV+1

#Each email is printed with it's name in alphabetical order and within 
#the character box set on the largest key/value
	for n in range(len(Order)):
		Word = Order[n]
		for (k,v) in Address.items():
			if k==Word:
				print("{:<{x}}".format(Word, x=Box),end="")
				print("{:<{x}}".format(v, x=Box))
	return
#------------------------------------------------------------------------------
#Searches all keys in the dictinary for the email the user requested
#Returns the name attached to that email
def SearchEmail(Address,email):
	email=email.capitalize()
	for (k,v) in Address.items():
		if (email in k)==True:
			return(v+ " was found.")	
	return("Nothing found.")		
#------------------------------------------------------------------------------
#Searches the values in the dictionary for the name the user requested
#Returns the email(s) attached to that name
def SearchName(Address, name):
	name=name.capitalize()
	emails=[]
	count=0
	for (k,v) in Address.items():
		if (name in v)==True:
			emails.insert(count, k)
	return(emails)
#-------------------------------------------------------------------------------	
#seaches both keys and values in the dictionary for the name and email the 
# user requested, returns any name(s) and email(s) that match
def SearchBoth(Address, both):
	TempList=both.split(",")
	TempList[0]=TempList[0].capitalize()
	TempList[1]=TempList[1].capitalize()
	Check ="n"
	for (k,v) in Address.items():
		if ((TempList[1] in k)==True):
			print(k+" "+v)
			Check="y"
	print("\n")
	for (k,v) in Address.items():		
		if ((TempList[0] in v)==True):	
			print(v+" "+k)
			Check="y"
	if Check=="n":
		print("Nothing was found containing either.")		
	return
#-------------------------------------------------------------------------------	
def main():
	Answer=1000 #allows the while-loop to start
	while Answer!=10:
		while Answer<1 or Answer>10:
			print("1 - Open address book")
			print("2 - Add entry")
			print("3 - Remove entry")
			print("4 - Store address book")
			print("5 - View address book by name, alphabetically")
			print("6 - View address book by email, alphabetically")
			print("7 - Search email addesses")
			print("8 - Search names")
			print("9 - Search names and email addresses")
			print("10 - Quit")
			Answer=int(input("What is your choice? "))
#Asks for a file name, checks the name for ".csv" and sends it to a function			
			if Answer==1:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				FileName="Nyeh"
				while (FileName.endswith(".csv"))==False:
					FileName=input("What is the name of the file? ")
				Address=OpenFile(FileName)
				print("File was saved into the program.")
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Asks for a name and an email and sends it to a function				
			if Answer==2:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				Name=input("What's the name you wish to add? ")
				Email=input("What's the email? ")
				Address=add(Address, Name, Email)
				print("It has been added to the Address book.")
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Asks for an email and sends it to a funtion				
			if Answer==3:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				Email=input("What is the email? ")
				Address=remove(Address, Email)
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Asks for a name and sends it to a function				
			if Answer==4:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				Name=input("What name do you want for the file? ")
				Name=Name+".csv"
				addressbook(Address, Name)
				print("The file has been created.")
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Calls the function that alphabetizes names				
			if Answer==5:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				NameList(Address)
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Calls the funtion that alphabetizes emails				
			if Answer==6:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				EmailList(Address)
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")			
#Asks for an email and sends it to a function
			if Answer==7:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				Email=input("What's the email? ")
				Name=SearchEmail(Address,Email)
				print(Name)
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Asks for a name and send it to a function				
			if Answer==8:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				Name=input("What's the name? ")
				Email=SearchName(Address,Name)
				print("\n")
				if Email==[]:
					print("No entries found.")
				if Email!=[]:
					for n in Email:
						print(n)
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Asks for a name & email and sends it to a function
			if Answer==9:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				Both=input("Put in the name and email like name,email: ")
				Response=SearchBoth(Address, Both)
				Answer=1000 #tells the loop to run again
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
#Allows the loop to end and allows the program to come to an end
			if Answer==10:
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("Goodbye!")
	return
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
