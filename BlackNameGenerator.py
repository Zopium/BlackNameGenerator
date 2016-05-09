import random
counter=0
namebank=[]
blacknamebank=[]
while(1==1):

    user=raw_input("what is your name?")
    user=user.lower()
    prefixes = ["do", "fo", "to", "ty", "tai", "ja", "sha", "shaw", "shao",
    "lo", "ji", "p", "juan", "ali", "aa", "ra", "de", "la", "xa"]

    middle = ["shaun", "quan", "quandra", "quisha"]

    if (user in namebank):
        if (counter<20):
            print blacknamebank[namebank.index(user)]
            counter+=1

    if(user=="done"):
        break;

    elif (user=="josh"):

        print "your black name is Shineal Jackson"
    elif (user=="hassan"):
        print "Your black name is Fo\'quisha Tai\'quan Jones"

    if(user not in namebank):
        index1=random.randrange(0, 18)
        index2=random.randrange(0, 4)
        namebank.append(user)
        storage= "Your black name is " +  prefixes[index1] + "\'"+ middle[index2]
        blacknamebank.append(storage)
        print storage
        counter+=1
    if (counter>=20 and user.lower() != "josh" and user.lower() != "hassan"):
        print "your black name is courtney"
