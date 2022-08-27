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
            print("Root word is ", word[str])
            count = 1

    if count == 0:
        print("Root word is ", str)

def inflectional_morphological_analysis(x, y):
    str = x
    count = y
    # List of suffix
    list = ['ing', 'ed']

    # str = input("\nEnter your word here : ") # Take input from user
    # str = str.lower()

    for i in list:
        length = len(i)
        word = str[0:-length]
        suffix = str.removeprefix(word)

        if suffix == i:
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

    if count == 0:
        derivational_morphological_analysis(str, count)

def derivational_morphological_analysis(x, y):
    str = x
    count = y
    # List of suffix
    list = ['ies', 'iness']

    # str = input("\nEnter your word here : ") # Take input from user
    # str = str.lower()

    for i in list:
        length = len(i)
        word = str[0:-length]
        suffix = str.removeprefix(word)

        if suffix == i:
            print("It's a type of Derivational Morphological Analysis")
            root = str.removesuffix(i)
            root = root + 'y'
            print("Root word is " + root)
            count = 1
            print("It\'s Tense is ", tense(i))
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