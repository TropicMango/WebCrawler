import Cambridge
import Dictionary
import FreeDictionary
import Google
import Merriam

WordsList = ["cat", "twitch", "minecraft", "facebook", "iphone", "prius", "java", "twitter", "firefox", "walmart", "toyota", "ford"]

def ColorRed (string):
    return "\033[91m {}\033[00m".format(string)
def ColorPink (string):
    return "\033[95m {}\033[00m".format(string)
def Bold (string):
    return "\033[1m {}\033[00m".format(string)

def Pronounce (word):
    try:
        print "Cambridge: "+Cambridge.lookup_word(word)
    except AttributeError:
        print ColorRed("Cambridge does not have a pronunciation")
    try:
        print "Dictionary: "+Dictionary.lookup_word(word)
    except AttributeError:
        print ColorRed("Dictionary does not have a pronunciation")
    try:
        print "FreeDictionary: "+FreeDictionary.lookup_word(word)
    except AttributeError:
        print ColorRed("FreeDictionary does not have a pronunciation")
    try:
        print "Google: "+Google.lookup_word(word)
    except AttributeError:
        print ColorRed("Google does not have a pronunciation")
    try:
        print "Merriam: "+Merriam.lookup_word(word)
    except AttributeError:
        print ColorRed("Merriam does not have a pronunciation")

#Pronounce ("cat")
for word in WordsList:
    print ColorPink(Bold("=================="+word+"=================="))
    Pronounce (word)
   
