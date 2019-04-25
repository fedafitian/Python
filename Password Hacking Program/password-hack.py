def main():

    #Opens my dictionary.txt file
    f = open("dictionary.txt","r")
    inDictionary = False

    print("Can your password survive a dictionary attack?")
    #Below takes the input from the keyboard and stores it to a variable
    password = input("Type in a trial password: ")

    #Logic to see if the password is in the dictionary file
    for line in f:
        password = converts(password)
        if password.strip() == line.strip():
            inDictionary = True
            print("I found your password: ", line.strip())
            break
    if not inDictionary:
        print("I couldn't find your password")

#Function below checks and converts common letter-number combinations
def converts(password):
    password = password.lower()
    password = password.replace("@","a")
    password = password.replace("2","7")
    password = password.replace("1","i")
    password = password.replace("3","e")
    password = password.replace("4","a")
    password = password.replace("5","s")
    password = password.replace("6","b")
    password = password.replace("7","t")
    password = password.replace("8","b")
    password = password.replace("9","g")
    password = password.replace("0","o")
    password = password.replace("+","t")
    password = password.replace("!","i")
    password = password.replace("$","s")
    return password

if __name__ == '__main__':
    main()