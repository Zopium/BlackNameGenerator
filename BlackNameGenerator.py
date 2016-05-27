import random
counter=0
while(1==1):

    user=raw_input("what is your name?")
    user=user.lower()
    prefixes = ["do", "fo", "to", "ty", "tai", "ja", "sha", "shaw", "shao",
    "lo", "ji", "p", "juan", "ali", "aa", "ra", "de", "la", "xa"]

    middle = ["shaun", "quan", "quandra", "quisha"]
    if(user=="done"):
        break;
    if (counter>=20 and user.lower() != "josh" and user.lower() != "hassan"):
        print "your black name is quortney"
    elif (user=="josh"):
        print "your black name is Shineal Jackson"
    elif (user=="hassan"):
        print "Your black name is Fo\'quisha Tai\'quan Jones"
    else:
        ansa = 0
        ansb = 0
        counter+=1
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
        input = user
        Final_Number = 0
        array = []
        def letter_to_number():
            global letters
            global input
            global Final_Number
            global array
            input = input.upper()
            for i in range (0, len(str(input))):
                for a in range (0, 27):
                    if letters[a] == input[i]:
                        array.append(a)
        letter_to_number()
        def last_answer():
            global letters
            global input
            global Final_Number
            global array
            for a in range (len(array)):
                Final_Number += (array[a] * (27 ** (len(array) - a - 1)))
            return Final_Number
        ans = last_answer()
        ansa = ans%(len(prefixes))
        ansb = ans%(len(middle))
        print "Your black name is " +  prefixes[ansa] + "\'"+ middle[ansb]
