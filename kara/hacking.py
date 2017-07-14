# hacking, exploiting, and denial of service

#DOS
#(effectively) shut down a service by flooding it with requests or sending it requests that drain computationl power


#    DDOS (distributed denial of service)
#same as above, but with multiple machines, connections, etc,
#just scaling up the DOS to make it more powerful
# 100 machines > 1 machine

#Exploits
'''
1.) incorrect code
2.) missing code (checking errors,etc.)



HACKING AND SECURITY PART 2: PASSWORDS

-Admin Priviledges: locked with a password, but USUALLY PRESENT!


how do we maintain security when our system is breached?
-encrpyt the data
-Restrict IP"s so that only certain connections can access admin


HASH FUNCTIONS

    Function that takes in data (any data) and gives back a 'hash'
    Hash = fixed-length, 'pseudo-unique'.

    Basically: hash function acts like a 'random' function.. but it's deterministic

    Idea: instead of storing PASSWORD, store HASH OF PASSWORD! Then, compare (has of ) user's passwrod at autehnitcation
    time with has of correct password

CRPTOGRAPHIC HASH FUNCTIONS

    1. Given a hash h, it should be REALLY hard to find a piece of data x such that hash(x) == h

    2. It should be REALLY hard to find two pieces of data x1 and x2 such that hash(x1) == hash(x2)


    SHA-1 : 20+ year old cryptohash    been collided

    SHA-2: 10+ year old crpytohash  not been collided


CRACKING PASSWORD; BRUTE FORCE

idea:  just check every possible password ( take hash, check against target hash... if equal, you found the password)
* takes a long time, yet possible  on today's computers, 8-9 characters

CRACKING PASSWORDS:  DICTIONARY ATTACKS

Idea: obtain a list of the most common passwords

CRACKING PASSWORDS: EPILOGUE

it gets way, way more complicated
-hybrid dictionary
rainbow tables
reverse lookup


'''