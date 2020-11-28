String=input("Enter a String : ")
Vowels=0
Consonants=0
Digits=0
Spaces=0
Length=len(String)
String=String.lower()
for loop in range (0, Length):
    if (String[loop]=='a' or String[loop]=='e' or String[loop]=='i' or String[loop]=='o' or String[loop]=='u'):
        Vowels+=1
    if (String[loop]!='a' or String[loop]!='e' or String[loop]!='i' or String[loop]!='o' or String[loop]!='u'):
        Consonants+=1
    if (String[loop]>='0' or String[loop]<='9'):
        Digits+=1
    if (String[loop]==" "):
        Spaces+=1
print ("Number of Vowels in given string are : ",Vowels)
print ("Number of Consonants in given string are : ",Consonants)
print ("Number of Digits in given string are : ",Digits)
print ("Number of Spaces in given string are : ",Spaces)
