# List of root words
list = ['park', 'book', 'play', 'train', 'study']

# Dictionary for category
category = {
    'park' : 'verb',
    'book' : 'verb',
    'play' : 'verb',
    'train' : 'verb',
    'study' : 'verb'
}

# Dictionary for tenses
tense = {
    's' : 'simple-present',
    'ing' : 'present-continuous',
    'ed' : 'simple-past',
    'ies' : 'simple-present'
}

str = input("Enter your word here : ") # Take input from user
count = 0
for i in list:
    length = len(i) # Finding length of root word from list
    new = str[0:length] # Removing root word from input given by user
    unique = new
    if unique == 'studi':
        new = 'study'

    # Checking Root Word, Category and Tense for input from user
    if new == i:
        print("Root word is " + i)
        count = 1 # If root word is found, then increament the count
        print("It's category is " + category[i])
        if len(str) == length:
            tense = 'simple-present'
        else:
            l = str.lstrip(new) # Removing root word from input using lstrip()
            tense = tense[l]
        print("And it's tense is " + tense)

if count != 1:
    print("Root word is not found, try something different")

