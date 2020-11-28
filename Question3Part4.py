def firstLetterWord(String): 
    Result = ""  
    Value = True
    for i in range(len(String)): 
        if (String[i] == ' '): 
            Value = True
        elif (String[i] != ' ' and Value == True): 
            Result += (String[i]) 
            Value = False
    return Result

if (__name__ == "__main__"): 
    String = input("Enter a String : ")
    String=String.upper()
    print (firstLetterWord(String))
