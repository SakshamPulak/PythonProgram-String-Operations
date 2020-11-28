String=input("Enter a String : ")
Occurrence = {} 
for character in String:
   if character in Occurrence: 
      Occurrence[character]+=1
   else: 
      Occurrence[character]=1
print ("Occurrence of each character in given string is : ")
print (str(Occurrence))
