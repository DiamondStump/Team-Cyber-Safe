# Helpful links
# https://www.youtube.com/watch?v=KzqSDvzOFNA
# https://www.youtube.com/watch?v=yIhSk4Ws0ag
# https://www.youtube.com/watch?v=rHTwjV1ORUQ
# https://www.py4e.com/html3/06-strings
# https://docs.python.org/3/library/string.html#
# https://docs.python.org/3/library/random.html#examples


import string
import random
import hashlib

# the code below is just a formal greeting

Greeting = input("\nWelcome to PASSWORD GENERATOR! \n\nWould you like for me Generate a password for you? \n")
if Greeting.lower() == "no":
    print("Hope it works out for ya.")
    exit()
elif Greeting.lower() == "yes":
    print( "Alright, lets get started!")
else:
    print("Thats not a valid input.\nPlease specify yes or no.")
    exit()

# The code below sets the value for "length" and will crash and end the script if user doesnt input an integer.
length = int(input("\n\nHow many characters do you want to have in your password?\n(There's no limit. Choose as many as you like)\n"))

# The code below is just a place holder that will later get changed by the 2nd "if" statment in this script.
algor = "5"

# The code below is just a place holder that will later get changed by the 3nd "if" statment in this script.
digest = " "

# The code below controls what the user is allowed to input 
# if the answer is yes, a list of algorithims will be displayed for the user to choose from.
# The code also exists for the purpose of changing the data inside the variable "algor" if the answer is yes,..
# and skips the question if the answer is no.
Hash = input("\n\nWould you like to create a hash digest of the randomly generated password?\n")
if Hash.lower() == "no":
       pass
elif Hash.lower() == "yes":
       algorithim = input("Here is a list of available hashing algorithms that you \ncan choose from to run against your plaintext password.\n|\n|\n-- md5 \n-- sha1, sha224, sha256, sha384, sha512 \n-- blake2b, blake2s \n|\n|\nPlease choose from the following list above.\n")
       algor = algorithim
else:
      print("Thats not a valid input.\nPlease specify yes or no." )
      exit()

# i would like to use the constant variable called "printable" in the string module,
# but i couldnt because it has the "whitespace" variable included in it that
# has buttons like "tab","enter", "spacebar" and etc within it.
# So i decided to make a new variable by using the the preexisting constant varibales that only
# contain the charaters i want.
# Then i sperated each character in the string and turned it into a list.

# #  ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyz
allchar = list(string.ascii_uppercase + string.punctuation + string.digits + string.ascii_lowercase)

# I wanted to use "random.choices" for multple reasons. I Mainly chose ".choices" because it
# allows for the possibiliy for same element in the list to be selected multiple times.
# Whereas ".sample" won't select the same element in the list specified more than once, which also means 
# that the lenght will be limited to only 95 characters as a result.
# I also used ".choices" for 2 other reasons.
#     1. To specify the length of characters desired by using the integer provided in the "length" variable.
#     2. To use "weight" to decrease the likelyhood of capital letters and symbols from being selected.
# I know it looks a little silly but it didnt take long.


#                   Weight Template  ----->   A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,!,",#,$,%,&,',(,),*,+,,,-,.,/,:,;,<,=,>,?,@,[,\,],^,_,`,{,|,},~,
Generation = random.choices(allchar, weights=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,
#                   Weight Template  ----->   0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
                                              3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
                                              k=length)

# and then i chose ".shuffle" to shuffle the list,... which rearranges the order of the list.
# Doing this was a little needless but i did it anyways to prove that i understand the modules.

rearrange = random.shuffle(Generation)

# The code below turns the list in "Generation" into a string.
# and it prints out the plaintext password.
results = "".join(Generation)
print("\nHere is your new generated plaintext password. -------------->   " + results + "\n")

# The code below is an "if" Statement and is the only code that uses the functionaliy provided in the "hashlib" module.
# its a repeated pattern that changes depending upon what is specified in "algor"
# If algor contains any of the strings that were specified in the "algorithim list" that was displayed to the user to choose from,...it will perform that algorithm against the string inside the variable "Generation".
# And in the end it will change the data in the variable "digest" to the output of that hash.
# and of cousrse if "hash" equals "no",.... then this all gets skipped.

if Hash.lower() == "yes" and algor.lower() == "md5":
        Generation = "".join(Generation)
        md5 = hashlib.md5()
        md5.update(Generation.encode('utf-8'))
        hashed_string = md5.hexdigest()
        digest = "Here is your md5 hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "sha1":
        Generation = "".join(Generation)
        sha1 = hashlib.sha1()
        sha1.update(Generation.encode('utf-8'))
        hashed_string = sha1.hexdigest()
        digest = "Here is your sha1 hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "sha224":
        Generation = "".join(Generation)
        sha224 = hashlib.sha224()
        sha224.update(Generation.encode('utf-8'))
        hashed_string = sha224.hexdigest()
        digest = "Here is your sha224 hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "sha256":
        Generation = "".join(Generation)
        sha256 = hashlib.sha256()
        sha256.update(Generation.encode('utf-8'))
        hashed_string = sha256.hexdigest()
        digest = "Here is your sha256 hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "sha384":
        Generation = "".join(Generation)
        sha384 = hashlib.sha384()
        sha384.update(Generation.encode('utf-8'))
        hashed_string = sha384.hexdigest()
        digest = "Here is your sha384 hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "sha512":
        Generation = "".join(Generation)
        sha512 = hashlib.sha512()
        sha512.update(Generation.encode('utf-8'))
        hashed_string = sha512.hexdigest()
        digest = "Here is your sha512 hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "blake2b":
        Generation = "".join(Generation)
        blake2b = hashlib.blake2b()
        blake2b.update(Generation.encode('utf-8'))
        hashed_string = blake2b.hexdigest()
        digest = "Here is your blake2b hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif algor.lower() == "blake2s":
        Generation = "".join(Generation)
        blake2s = hashlib.blake2s()
        blake2s.update(Generation.encode('utf-8'))
        hashed_string = blake2s.hexdigest()
        digest = "Here is your blake2s hash digest of your plaintext password. ---->   " + hashed_string + "\n\n"
elif Hash.lower() == "no":
    pass


# The code below prints out the digest that was created based upon the hashing algorithim that was specified by the user.
print(digest)
