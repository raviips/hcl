#Function to reduce string

def MaxReducedString(S):

    S=list(S)# converting string tplist
    for i in range(len(S)-1):
        if S[i]==S[i+1]:
            return MaxReducedString(S[:i]+S[i+2:])
        else:
            continue
    return "".join(S)    
     
#Enter  astring          
S1 =input("Enter a string :\n")
print(MaxReducedString(S1))

