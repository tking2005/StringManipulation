
class MyString():
    def __init__(self, str=""): # initializes  the object
        self.str=str

    #Returns the current string.

    def getString(self):
        return self.str

    #Returns a string that consists of all and only the vowels in the current string.
    #Only letters a, e, i, o, and u (both lower and upper case) are considered vowels.
    #The returned string contains each occurrence of a vowel in the current string.
    def getVowels(self):
        lowercase=self.str
        lowercase=lowercase.lower()
        vowels=""
        count=len(lowercase)

        for a in range(0,count):
            if lowercase[a]=='a'or lowercase[a]=='e' or lowercase[a]== 'i' or lowercase[a]=='o' or lowercase[a]== 'u':
                vowels=vowels+self.str[a]
        return vowels

    #Returns a string that consists of the substring between start and end indexes (both included) in the current string.
    #Index 1 corresponds to the first character in the current string.'''
    def getSubstring( self,start, end):
        originalWord = self.str
        wordCount = len(originalWord)
        subString = ""
        startSubString = start-1
        endSubString=end
        if startSubString>=0 and endSubString<=wordCount:
            try:
                for count in range(startSubString,endSubString):
                    subString=subString+originalWord[count]
            except IndexError:
                return("Index out of bounds")
            return subString
        else:
            return ("Index out of bounds")

    #Breaks the string down, and returns it as a character string
    def getCharList(self):
        originalWord = self.str
        wordCount = len(originalWord)
        CharacterList=[]
        for counter in range(0, wordCount):
            CharacterList.append(originalWord[counter])

        return CharacterList

    # Returns the index of the first occurrence of a character in the current string.
    # Index 1 corresponds to the first character in the current string.
    # return 0 if no match is found
    def indexOf(self, c):
        originalWord = self.str
        wordCount = len(originalWord)
        wordIndex = c

        for count in range(0, wordCount):
            if originalWord[count] == wordIndex:
                return count
                vowels = vowels + self.str[a]
            return originalWord[wordIndex]

    #Returns the index of the first occurrence of a character in the current string.
    #Index 1 corresponds to the first character in the current string.
    # return 0 if no match is found
    def indexOfChar(self,c):
        originalWord = self.str
        wordCount = len(originalWord)
        wordIndex = c-1

        if wordCount<c:
            return 0
        else:
            return originalWord[wordIndex]




    # Removes all occurrences of the specified character from the current string.
    def removeChar(self,c):
        originalWord = self.str
        wordCount = len(originalWord)
        removeCharater = c
        newRemoveCharWord = ""
        counter = 0
        while counter < wordCount:
            if originalWord[counter]==removeCharater:

                counter += 1
            else:
                newRemoveCharWord = newRemoveCharWord+originalWord[counter]
                counter += 1

        return newRemoveCharWord


    #Invert the current string.
    def invert(self):
        originalWord=self.str
        wordCount = len(originalWord)
        inverseWord=""
        countDown = 1
        while countDown < wordCount+1:
            inverseWord = inverseWord+(originalWord[wordCount-countDown])
            countDown += 1

        return inverseWord
