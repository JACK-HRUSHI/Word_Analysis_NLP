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
            print("\nIt's a type of Lemmatization")
            print("Root word is " + word[str])
            count = 1

    if count == 0:
        print("\nYou have entered root word only !")
        print("So, root word is " + str)
        print("Entered word is Singular")
        print("It\'s Tense is " + "simple-present")

def inflectional_morphological_analysis(x, y):
    str = x
    count = y
    # List of suffix
    list = ['ies', 'iness', 'ing', 'ed', 's']
    dlist = ['ies', 'iness']

    # str = input("\nEnter your word here : ") # Take input from user
    # str = str.lower()

    for i in list:
        length = len(i)
        word = str[0:-length]
        suffix = str.removeprefix(word)

        if suffix == i:
            if i == 'ies' or i == 'iness':
                print("\nIt's a type of Derivational Morphological Analysis")
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
                break
            else:
                print("\nIt's a type of Inflectional Morphological Analysis")
                root = str.removesuffix(i)
                print("Root word is " + root)
                count = 1
                print("It\'s Tense is ", tense(suffix))
                # print("It\'s Category is ", category())
                if suffix == 's':
                    print("Entered word is Plural")
                else:
                    print("Entered word is Singular")

    if count == 0:
         lemmatization_morphological_analysis(str, count)

def main():
    str = input("\nEnter your word here : ")  # Take input from user
    str = str.lower()
    count = 0
    inflectional_morphological_analysis(str, count)

main()