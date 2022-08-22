import time

def inflectional_morphological_analysis():
    # List of suffix
    list = ['s', 'ing', 'ed']

    str = input("\nEnter your word here : ") # Take input from user
    str = str.lower()

    for i in list:
        length = len(i)
        word = str[0:-length]
        suffix = str.removeprefix(word)

        if suffix == i:
            root = str.removesuffix(i)
            print("Root word is " + root)

def derivational_morphological_analysis():
    # List of suffix
    list = ['ies', 'iness']

    str = input("\nEnter your word here : ") # Take input from user
    str = str.lower()

    for i in list:
        length = len(i)
        word = str[0:-length]
        suffix = str.removeprefix(word)

        if suffix == i:
            root = str.removesuffix(i)
            root = root + 'y'
            print("Root word is " + root)

def main():
    print("Which type of analysis do you want to perform :")
    analysis = int(input('1. Inflectional Analysis. \n2. Derivational Analysis. \n'))
    if analysis == 1:
        inflectional_morphological_analysis()
    elif analysis == 2:
        derivational_morphological_analysis()
    else:
        print("Enter correct option \n")
        time.sleep(2)
        main()

main()