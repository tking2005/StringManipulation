import sys

def main():
    print("")
    print("******************************************************************************************************************************************")
    print("\t\t\tWelcome To Taryn's & Josue's \'Essay Buddy\' Software Program."
          "\nThis Program Will Assist You In Keeping Track With Your Words Count & Average, In An Uploaded English Language Essay In Text File Format."
          "\n\t\t\tPlease Upload Your Text or \'.txt\' File Into The Program:"
          "\n\t\tPlease Type In The Following Command To Begin, Example: python EssayBuddy.py YourEssay.txt."
          "\n\t\t\tWhere, \'YourEssay.txt\', Will Be The Name Of Your Text File.")
    print("******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print("")

    readfile()

def readfile():
    file=sys.argv[1] #get the file from the argument

    if not file.lower().endswith('.txt'):
        print("")
        print("Only text files with a \'.txt\' extension are supported. Please upload a valid text file to be read.")
        print("")
        return
    else:
        print("")
        print("Your uploaded file:",file,"is a valid text file. See your word counts and average below.")
        print("")

    f=open(file,"r") #opens the file essay.txt
    report=f.read()
    checkfile(report)
    f.close()
def checkfile(report):
    a=0
    endofsentence=0
    count=len(report)
    for a in range(0,count):
        if report[a]=='.'or report[a]=='!'or report[a]==';' or report[a]==':' or report[a]=='?':
            #print("Where special characters are found in the words of the report: ", report[a])
            endofsentence+=1
            #print("")
            #print("Keeping Track of the number of \'end of sentence characters\': ", endofsentence)
            #print("")

    words=report.split()
    print("")
    #print(words)
    print("")

    validwords=0
    wordsLength=0
    b=0
    for a in words:
        actualWord=words[b]

        wordsLength=len(actualWord)
        if ((wordsLength >=4 and actualWord.isalpha()) or (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith(';')) or (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith('!')) or
           (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith('!!!')) or (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith(':')) or (wordsLength >=5 and actualWord.isalpha() + actualWord.endswith('...')) or
           (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith('.')) or (wordsLength >=6 and actualWord.isalpha() + actualWord.endswith('\'s')) or  (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith(' ')) or
           (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith('?')) or (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith(',')) or (wordsLength >=4 and actualWord.isalpha() + actualWord.endswith('???'))):
           validwords+=1
           #print("***VALID WORDS***: ", actualWord)
        b+=1

    print("")

    numberOfWords=len(words)
    print("The number of words is",numberOfWords,"The total number of valid or accepted words is", validwords)
    print("The average number of words per sentence is",validwords/endofsentence)

    print("")
    print("Thank you for using our program. We are delighted that it could serve you in your writing assignment. Have a great day!")

main()
