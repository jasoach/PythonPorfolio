#word count
#jason
#counts the words in a given doc

def word_counter(text):
    x = text.split() #splits words and puts into array
    y=len(x)
    print(f"the text has {y} words") # prints how many split words there are

word_counter("hello hi how are you my name is nola")
