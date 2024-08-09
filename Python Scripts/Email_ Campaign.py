import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


#_______________________________________________________________________________
# makes a prehemptive disclaimer
print("_______________________________________________________________________________________________\n")

Disclaimer = input("Would you like an excerpt explaining what to expect from this script. (y/n) ")
if Disclaimer == "n":
	pass
elif Disclaimer == "y":
	print("""DICLAIMER!!!
This script will only work if your using gmail,... (it depends,...read the 2nd paragraph for more clarification)
You can always edit the script to add the email server and port number of your choice on line 179 and 262.
You dont really need to change the PORT number unless you going to use a different protocol other thatn SMTP.
You can always replace the "input variables" with "strings" to hardcode any information so that can decrease the 
amount of promted questions. (should be super easy.)

You'll be asked for an app password,... different email services such as gmail offer this capability.
if your email service supports having "app passwords" then this script can still work for you no problem.
If your using gmail you can set one up by going to this URL ---> https://myaccount.google.com/apppasswords
it will prompt you to login to your account,... then create a name for your app. (it doesnt matter what name you give it, "ex.Python")
click "create",... you should now see your "app password".
Go ahead and add this password to your script when the question prompts you to do so. 
(I wouldnt advice hardcoding the password into the script for security reasons)
(The password should not include spaces when you enter it in.)

Afterward you will go through a Questionnaire procces for the purpose of setting up your email Campaign.
This includes the subject title, message body and the company naming convention.
Any information fed into the system is private and confidential.
All questions are necessary, and answers will be used to create unique talored messages to each recipient in the campaign.
It's important to come prepared beforehand,... so that you can answer the questions correctly.
You must understand what a "Company email naming convention" is.
	   
You will eventually be asked to privide a path to your .txt file. (The script will scan this .txt file)
This .txt file is something that you'll create.
This .txt file and will contain all the first and last names of staff members of the organization.
It's imperitive that the file follows the correct format. 
The format is as follows:
	- First and last names in the file needs to be SEPERATED BY SPACES.
	- Each pair of first and last names in the file need to be ON THEIR OWN LINES,... starting from top to bottom.
	- So each pair of names needs to be on a seperate line.
	   Ex. Cory Lody
		   Andrew Gifford 
	       Brett Wilson\n""")
	forward = input("Are you ready to continue? (y/n) ")
	if forward.lower() == "n":
		exit()
	elif forward.lower() == "y":
		pass
	else:
		print("\nInvalid syntax")
		exit()
else:
    print("\nInvalid syntax")
    exit()
	
print("\nloading...")
time.sleep(1)
#________________________________________________________________________________________________________________________________

print("_______________________________________________________________________________________________\n")
print(""""We will now ask questions to help "login" and set up your "email", "subject", and "body message".\n""")

name = input("What is your name? ")
my_email = input("What is your email? " )
app_password = input("""What is your "app passowrd"? (no spaces) """)
position = input("What is the name of the position that you are applying for? ")
company = input("What is the name of the company? ")
Linkedin_profile = input("What is your Linkedin profile URL? ")

print("\nloading...")
time.sleep(1)
#_________________________________________________________________________________________________________________________________
# The Questions below are to help set up the company naming convention.
print("_______________________________________________________________________________________________\n")
print("""Okay, we will now start asking questions to set up the "Company naming convention."\n""")

Co_domain = input("""what is the Company email domain? (Remember to include the @ at the beginning)
(Ex. @gmail.com)
(Ex. @ecstech.com)
""")

dot = input("Does the Company email convention use a dot in between the names? ---> (.) (y/n) ")
if dot.lower() == "n":
	dot = ""
elif dot.lower() == "y":
    dot = "."
else:
    print("\nInvalid syntax")
    exit()
	
Co_names = input("Does the naming convention use first and last names? (y/n) ")
if Co_names.lower() == "n":
	print("""\nThats weird,...but okay,... we are done with the Questionnaire\n""")
elif Co_names.lower() == "y":
	initals = input("Are either of those names initialed? (y/n) ")
	if initals.lower() == "n":
		first_name = False
		last_name = False
		print("""\nPerfect,Thank you,... we are done with the Questionnaire.\n""")
		pass
	elif initals.lower() == "y":
		init_answer = input("Are both names initaled or just one? (both/one) ")
		if init_answer.lower() == "both":
			print("""\nThats weird,...but okay,... we are done with the Questionnaire\n""")
		elif init_answer.lower() == "one":
			first_last_anwser = input("Is it the first or last name that is initialed? (first/last) ")
			if first_last_anwser.lower() == "first":
				first_name = True
				last_name = False
				print("""\nPerfect,Thank you,... we are done with the Questionnaire.\n""")
			elif first_last_anwser.lower() == "last":
				first_name = False
				last_name = True
				print("""\nPerfect,Thank you,... we are done with the Questionnaire.\n""")
			else:
				print("\nInvalid syntax")
				exit()
		else:
			print("\nInvalid syntax")
			exit()
	else:
		print("\nInvalid syntax")
		exit()
else:
    print("\nInvalid syntax")
    exit()


print("\nloading...")
time.sleep(1)
print("_______________________________________________________________________________________________\n")
#______________________________________________________________________________________________________________________________


path = input("what is the path to your .txt file containg staff names? \n")

print("\nloading...")
time.sleep(1)

print("_______________________________________________________________________________________________\n")

#__________________________________________________________________________________________________________________________

preview = f"""\nSUBJECT: {position} Position - {name}

Hello __(text file 1st name)__

I'm wanting to apply for the {position} Role at {company}. I found you on LinkedIn and I was wondering,... 
What is your favorite thing about your company culture?
What's your day to day look like?
Any input would be amazing.
    			
Sincerely, {name}
{Linkedin_profile}\n\n"""

check = input("Would you like to see a Preview of your email messages before sending? (y/n) ")
if check == "n":
	pass
elif check == "y":
	print("\nloading...")
	time.sleep(1)
	print(preview)
	forward_1 = input("""Are you satisfied with this message? Would you like to officially start the email Campaign.? (y/n) """)
	if forward_1 == "n":
		print("Campaign canceled!")
		exit()
	elif forward_1 == "y":
		forward_2 = input("\nAre you sure? (y/n) ")
		if forward_2 == "n":
			print("Campaign canceled!")
			exit()
		elif forward_1 == "y":
			print("\ninitiating and sending emails now!...loading...")
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login(my_email, app_password )
			file = open(path, 'r')
			for line in file:
				if first_name == True:
					first = line.split()[0]
					first = first[0]
				elif first_name == False:
					first = line.split()[0]
				if last_name == True:
					last = line.split()[1]
					last = last[0]
				elif last_name == False:
					last = line.split()[1]
		
				mess_f_name = line.split()[0]
				final_r_email = f"{first}{dot}{last}{Co_domain}"
	
				body = f'''
					<html>
  						<body>
    						<p>Hello {mess_f_name},<br>
    						<br>
    						I'm wanting to apply for the <b>{position}</b> Role at <b>{company}</b>. I found you on LinkedIn and I was wondering,... <br>what is your favorite thing about your company culture?<br>
    						What's your day to day look like?<br>
    						Any input would be amazing.<br>
    						<br>
    						Sincerely,{name}<br>
    						{Linkedin_profile}</p>
  						</body>
					</html>
					'''
				message = MIMEMultipart('alternative')
				message['From'] = my_email
				message['To'] = final_r_email  # Recipient email address
				message['Subject'] = f"{position} Position - {name}"

				message.attach(MIMEText(body, 'html'))

				server.sendmail(my_email, final_r_email , message.as_string())


			print("----------Emails sent Successfully!----------")
			server.quit()
# END of Program @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			exit()
		else:
			print("\nInvalid syntax")
			exit()
	else:
		print("\nInvalid syntax")
		exit()
else:
    print("\nInvalid syntax")
    exit()


forward_3 = input("""Would you like to officially start the email Campaign.? (y/n) """)
if forward_3 == "n":
	print("Campaign canceled!")
	exit()
elif forward_3 == "y":
	forward_4 = input("\nAre you sure? (y/n) ")
	if forward_4 == "n":
		print("Campaign canceled!")
		exit()
	elif forward_4 == "y":
		pass
	else:
		print("\nInvalid syntax")
		exit()
else:
    print("\nInvalid syntax")
    exit()


print("\ninitiating and sending emails now!...loading...")
#_________________________________________________________________________________________________________________________
# setting up the email client/server session
# Upgrading to secure cipher suite
# Logging into email account

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(my_email, app_password )


#___________________________________________________________________________________________________________________________


file = open(path, 'r')

for line in file:
	if first_name == True:
		first = line.split()[0]
		first = first[0]
	elif first_name == False:
		first = line.split()[0]
	if last_name == True:
		last = line.split()[1]
		last = last[0]
	elif last_name == False:
		last = line.split()[1]
		
	mess_f_name = line.split()[0]
	final_r_email = f"{first}{dot}{last}{Co_domain}"
	
	body = f'''
		<html>
  			<body>
    			<p>Hello {mess_f_name},<br>
    			<br>
    			I'm wanting to apply for the <b>{position}</b> Role at <b>{company}</b>. I found you on LinkedIn and I was wondering,... <br>what is your favorite thing about your company culture?<br>
    			What's your day to day look like?<br>
    			Any input would be amazing.<br>
    			<br>
    			Sincerely,{name}<br>
    			{Linkedin_profile}</p>
  			</body>
		</html>
		'''
	message = MIMEMultipart('alternative')
	message['From'] = my_email
	message['To'] = final_r_email  # Recipient email address
	message['Subject'] = f"{position} Position - {name}"

	message.attach(MIMEText(body, 'html'))

	server.sendmail(my_email, final_r_email , message.as_string())


print("----------Emails sent Successfully!----------")
server.quit()






#__________________________________________________________________________