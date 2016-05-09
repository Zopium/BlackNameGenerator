import random
counter=0
namebank=[]
blacknamebank=[]
while(1==1):
    user=raw_input("what is your name?")
    prefixes = ["do", "fo", "to", "ty", "tai", "ja", "sha", "shaw", "shao",
    "lo", "ji", "p", "juan", "ali", "aa", "ra", "de", "la", "xa"]

    middle = ["shaun", "quan", "quandra", "quisha"]

    if (user in namebank):
        print blacknamebank[namebank.index(user)]
        counter+=1

    if(user=="DONE"):
        break;
    elif (user.lower()=="josh"):

        print "your black name is Shineal Jackson"
    elif (user.lower()=="hassan"):
        print "Your black name is Fo\'quisha Tai\'quan Jones"

    else:
        index1=random.randrange(0, 18)
        index2=random.randrange(0, 4)
        namebank.append(user)
        storage= "Your black name is" +  prefixes[index1] + "\'"+ middle[index2]
        blacknamebank.append(storage)
        print storage
        counter+=1
    if (counter>=20 and user.lower() != "josh" and user.lower() != "hassan"):
        print "your black name is courtney"
