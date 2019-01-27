# put your code here.
with open('test.txt') as poem: 
    # go through each line DONE
    # find all words in line DONE
    # pass words into a dictionary with a counter DONE
    # check if word exists DONE
    # if no, create it DONE
    # if yes, increment it DONE
    # repeat and increment counters as we go through each word in a line DONE
    # when completed with all lines, print results of the dictionary (not just the dict), following format DONE
    wordcount_dictionary = {}

    for line in poem:
        strip_line = line.strip()
        list_line = line.split(' ')
        for word in list_line:
            word = word.strip()
            # if word in wordcount_dictionary:
            #     wordcount_dictionary[word] += 1 
            # else:
            #     wordcount_dictionary[word] = 1
            wordcount_dictionary[word] = wordcount_dictionary.get(word, 0) + 1

    for key, value in wordcount_dictionary.items():
        print(key, value)




"""
NOTES:
we get back lines of text stored as a string
example: 'As I was going to St. Ives'
    we want to check the number of times each 'word' appears

Q: how do we get from a string of words to a single word that we can use to measure/count?
A: We want to split the string of words by SOMETHING. SOMETHING = ' '

['As', 'I', 'was', 'going', 'to', 'St.', 'Ives']

Q: How do we create a dictionary?
A: we name a variable with {}

wordcount_dictionary = {}

Q: How do we create a new key in a dictionary?
A: We need to use some kind of a bracket. dictionary_name[key] = value

"""