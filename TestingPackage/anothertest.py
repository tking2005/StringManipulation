#from TestingPackage.MyString_Student import MyString
from MyString_Student import MyString
s=MyString("MyBigFatGreekWedding")
print(s.getVowels())
print(s.invert())
print(s.removeChar("e"))
print(s.indexOf("z"))
print(s.indexOfChar(7))
print(s.getCharList())
print(s.getSubstring(1,4))