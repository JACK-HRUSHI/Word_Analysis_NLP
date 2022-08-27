import time

def tense(x):
    t = {
        's': 'simple-present',
        'ing': 'present-continuous',
        'ed': 'simple-past',
        'ies': 'simple-present',
        'iness': 'simple-present'
    }
    tense = t[x]
    return tense

def category():
    pass

def lemmatization_morphological_analysis(x, y):
    str = x
    count = y
    list = ['best', 'worst']
    word = {
        'best' : 'good',
        'worst' : 'bad'
    }
    for i in list:
        if str == i:
            print("It's a type of Lemmatization")
            print("Root word is " + word[str])
            count = 1
            delay()

    if count == 0:
        if str == 'stop':
            exit()
        elif len(str) == 1:
            print("Error...")
            delay()
        else:
            print("You have entered root word only !")
            print("So, root word is " + str)
            print("Entered word is Singular")
            print("It\'s Tense is " + "simple-present")
            # print("It\'s Category is ", category())
            delay()

def inflectional_morphological_analysis(x, y):
    str = x
    count = y
    # List of suffix
    list = ['ies', 'iness', 'ing', 'ed', 's']

    # List of suffixes for Dervational Morphological Analysis
    # dlist = ['iance', 'ied', 'ial', 'ize', 'ier', 'iest', 'ily', 'iage', 'iful', 'iment']

    for i in list:
        length = len(i)
        word = str[0:-length]
        suffix = str.removeprefix(word)

        if suffix == i:
            if i == 'ies' or i == 'iness':
                print("It's a type of Derivational Morphological Analysis")
                root = str.removesuffix(suffix)
                root = root + 'y'
                print("Root word is " + root)
                count = 1
                print("It\'s Tense is ", tense(suffix))
                # print("It\'s Category is ", category())
                if suffix == 's':
                    print("Entered word is Plural")
                else:
                    print("Entered word is Singular")
                delay()
            else:
                print("It's a type of Inflectional Morphological Analysis")
                root = str.removesuffix(i)
                print("Root word is " + root)
                count = 1
                print("It\'s Tense is ", tense(suffix))
                # print("It\'s Category is ", category())
                if suffix == 's':
                    print("Entered word is Plural")
                else:
                    print("Entered word is Singular")
                delay()

    if count == 0:
         lemmatization_morphological_analysis(str, count)

def delay():
    print("\nWait...\n")
    time.sleep(2)
    main()

def main():
    str = input("Enter your word here : ")  # Take input from user
    str = str.lower()
    count = 0
    inflectional_morphological_analysis(str, count)

main()