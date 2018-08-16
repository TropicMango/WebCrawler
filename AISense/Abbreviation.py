
LetterToWord = {"A":"EY", "B":"B IY", "C":"S IY", "D":"D IY", "E":"IY", "F":"EH F",
        "G":"JH IY", "H":"EY CH", "I":"AY", "J":"JH EY", "K":"K EY", "L":"EH L",
        "M":"EH M", "N":"EH N", "O":"OW", "P":"P IY", "Q":"K Y UW", "R":"AA R",
        "S":"EH S", "T":"T IY", "U":"Y UW", "V":"V IY", "W":"D AH B AH L Y UW",
        "X":"EH K S", "Y":"W AY", "Z":"Z IY"}

def Conversion (ABV):
    ABV = ABV.upper()
    output = ""
    for char in ABV:
        output += LetterToWord[char]
        output += " "

    return output


print (Conversion (input ("Abbreviation input: ")))
