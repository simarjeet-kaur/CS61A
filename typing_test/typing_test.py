''""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5

"""Question #1"""

def lines_from_file(path):
    i2 = []
    for i in readlines(open(path, mode='r')):
        i2.append(i.strip())
    return i2
def new_sample(path, i):
    return lines_from_file(path)[i]

"""Question #2 - Analyze"""

# def analyze(sample_paragraph, typed_string, start_time, end_time):
# #words per minute
#     minutes = abs(start_time - end_time) / 60
#     five_letter_words = len(typed_string) / 5
#     speed = five_letter_words / minutes
# #accuracy percentage
#     typed_words = split(typed_string)
#     number_of_typed_words = len(typed_words)
#     sample_words = split(sample_paragraph)
#     number_of_sample_words = len(sample_words)
#
#     if number_of_typed_words > number_of_sample_words:
#         number = number_of_sample_words
#     elif number_of_typed_words <= number_of_sample_words:
#         number = number_of_typed_words
#
#     correct_number = 0
#     for i in range(number):
#         if typed_words[i] == sample_words[i]:
#             correct_number += 1
#
#     if number == 0:
#         accuracy = 0.0
#     else:
#         accuracy = (correct_number / number) * 100
#
#     list = []
#     list = list + [speed] + [accuracy]
#
#     return list

def analyze(sample_paragraph, typed_string, start_time, end_time):
#words per minute
    def words_per_minute(typed_string, start_time, end_time):
        minutes = abs(start_time - end_time) / 60
        five_letter_words = len(typed_string) / 5
        return five_letter_words / minutes
#accuracy percentage
    def accuracy_percentage(typed_string, sample_paragraph):
        number_of_typed_words = len(split(typed_string))
        number_of_sample_words = len(split(sample_paragraph))
        number_of_words = min(number_of_sample_words, number_of_typed_words)

        correct_number = 0
        for i in range(number_of_words):
            if split(typed_string)[i] == split(sample_paragraph)[i]:
                correct_number += 1

        if number_of_words == 0:
            return 0.0
        return (correct_number / number_of_words) * 100

    return [words_per_minute(typed_string, start_time, end_time), accuracy_percentage(typed_string, sample_paragraph)]


"""Question #3 - Pig Latin"""

def pig_latin(sample_paragraph):
    words = split(sample_paragraph)
    def check_consonants(word):
        "returns the beginning consonants of the word"
        consonants = ''
        for w in range(0, len(word)):
            if word[w] not in ['a', 'e', 'i', 'o', 'u']:
                consonants += word[w]
            elif word[w] in ['a', 'e', 'i', 'o', 'u']:
                return consonants
        return consonants
    for i in words:
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            return i + "way"
        else:
            letters = check_consonants(i)
            slice = len(letters)
            return i[slice:] + letters + "ay"

### PHASE THREE ###

"Question 4"
def autocorrect(user_input, word_list, score_function):
    if user_input in word_list:
        return user_input
    else:
        close_words = [[score_function(user_input, i), i] for i in word_list]
        # return [i[1] for i in close_words is i[0] == min(close_words)[]]
        minimum_score = min(close_words)[0]
        for i in close_words:
            if i[0] == minimum_score:
                return i[1]
        # return min(close_words)[1]
        #, key = lamba lst: lst[1])
        # return min()[score_function(user_input, i) for i in word_list]
        # differences = {}
        # for i in word_list:
        #     differences[score_function(user_input, i)] = i
        # return differences[min(differences.keys())]
        #score_function takes in two strings comparing (user_input and
        #word from words_list - do something like for i in words_list)
        #output is a function that represents the difference betwen the two
        #strings, bigger the output of the score function, the greater
        #the difference between the two strings

# END Q1-5
def swap_score(string1, string2):
    if not string1 or not string2:
        return 0
    elif string1[0] == string2[0]:
        return swap_score(string1[1:], string2[1:])
    else:
        return 1 + swap_score(string1[1:], string2[1:])
# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    if word2 == '':
        return len(word1)
    elif word1 == '':
        return len(word2)
    elif word1 == word2:
        return 0
    elif word1[0] == word2[0]:
        return 0 + score_function(word1[1:], word2[1:])
    else:
        add_char = 1 +  score_function(word2[0] + word1[:], word2[:])
        sub_char = 1 + score_function(word1[1:], word2[1:])
        remove_char = 1 + score_function(word1[1:], word2[:])
    return min(add_char, sub_char, remove_char)
    # if word1 == word2: # Fill in the condition
    #     # BEGIN Q6
    #     return 0
    #     # END Q6
    # elif word1[0] == word2[0]: # Feel free to remove or add additional cases
    #     # BEGIN Q6
    #     return score_function(word1[1:], word2[1:])
    #     # END Q6
    # else:
    #
    # elif len(word1) > len(word2):
    #     difference = len(word2) - len(word1)
    #     word2 = word2[0:len(word1)]
    #     return difference + score_function(word1, word2)
    # elif len(word1) == len(word2):
    #     total = 0
    #     for i in word1:
    #         if word1[i] == word2[i]:
    #             total += 1
    #     return total
    # elif len(word1) < len(word2):
    #     difference = len(word2) - len(word1)
    #     word1 = word1 + word2[len(word1):]
    #     return difference + score_function(word1, word2)
    # else:
    #
    #     def add_char(word1, word2):
    #         while len(word1) <= len(word2):
    #             return swap_score(word1, word2)
    #         return 0
    #
    #     def remove_char(word1, word2):
    #         while len(word1) >= len(word2):
    #             if word1[0] != word2[0]:
    #                 return 1 + remove_char(word1[1:], word2[1:])
    #         return 0
    #
    #     def sub_char(word1, word2):
    #         if len(word1) == len(word2):
    #             if word1[0] == word2[0]:
    #                 return 0
    #             else:
    #                 return 1 + sub_char(word1[1:], word2[1:])
    #         return 0
    #     # BEGIN Q6
    #     return add_char(word1, word2) + remove_char(word1, word2) + sub_char(word1, word2)
    #     # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"""Question #7"""
def score_function_accurate(word1, word2):
    if word2 == '':
        return len(word1)
    elif word1 == '':
        return len(word2)
    elif word1 == word2:
        return 0
    elif word1[0] == word2[0]:
        return 0 + score_function_accurate(word1[1:], word2[1:])
    else:
        add_char = 1 +  score_function_accurate(word1[:], word2[1:])
        remove_char = 1 + score_function_accurate(word1[1:], word2[:])
        sub_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(word1[1:], word2[1:])
        return min(add_char, remove_char, sub_char)

"""Question 8"""
def memo(f):
    cache = {}
    def memoized(word1, word2):
        if (word1, word2) in cache:
            return cache[(word1, word2)]
        elif (word2, word1) in cache:
            return cache[(word2, word1)]
        # elif word2 not in cache:
        #
        #     return cache[word2]
        # elif word1 in cache:
        #     return cache[word1]
        # elif word2 in cache:
        #     return cache[word2]
        else:
            cache[(word1, word2)] = f(word1, word2)
            cache[(word2, word1)] = f(word1, word2)
            return f(word1, word2)
    return memoized
#function = score_function_accurate
score_function_accurate = memo(score_function_accurate)
score_function_final = score_function_accurate

# END Q7-8
