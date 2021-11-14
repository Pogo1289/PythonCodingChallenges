#  Imports

# Variables
import string

upper_limit_num = 101
lower_limit_num = 1
reverse_string = "Hello, World!"
reverse_integer = -865
sentence_average = "Hello, my name is Joseph, I'm from Knoxville, Tennessee."
number1 = "123"
number2 = "456"
palindrome = "radkar"
cypher_string = "abcd xyz"


#  Functions
#  Print numbers from low to high
def low_to_high(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit):
        print(i)


#  Print numbers from high to low
def high_to_low(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit):
        print(upper_limit_num - i)


#  Print string in reverse
def reverse_string(input_string):
    print input_string[::-1]


#  Count by given integer
def count_by_integer(lower_limit, upper_limit, integer):
    for i in range(lower_limit, upper_limit):
        if i == lower_limit_num:
            print(i)
            x = i + integer
        if i == x:
            print(i)
            x = i + integer


#  Reverse digits in string of numbers
def reverse_digits(integer):
    num_string = str(integer)
    if num_string[0] == "-":
        print("-" + num_string[:0:-1])
    else:
        print num_string[::-1]


#  Calculate average word length
def average_word_length(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)


#  Add two strings together without casting
def add_strings(string1, string2):
    sum_strings = eval(string1) + eval(string2)
    print(sum_strings)


#  Determine if word is valid palindrome
# def valid_palindrome(word):

#  Determine the index of the first non-repeating character in string
# def first_unique_character(string):

#  Determine whether array of integers is monotonic or not
# def monotonic_array(array):

#  Move zeroes to end of array
# def move_zeroes(array):

#  Fill in None values in array
# def fill_none(array):

#  Matched and mismatched words
# def match_words(sentence1, sentence2):

#  Prime Numbers Array
# def prime_numbers(array):


#  Fibonacci Sequence
def golden_ratio(iterations):
    current_number = 1
    previous_number = 0
    sum_numbers = 0
    for i in range(iterations):
        print(previous_number)
        sum_numbers = previous_number + current_number
        previous_number = current_number
        current_number = sum_numbers


#  Sum of range of integers up to n
def sum_range(integer):
    print(sum(range(integer + 1)))


#  Caesar Cypher (each letter is replaced by a different letter a set number of letters away
def caesar_cypher(caesar_string, shift_num):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = string.maketrans(letters, mask)
    print(caesar_string.translate(trantab))


# Caesar Cypher without translate()

#  Log parser

#  Change
def make_change(amount_paid, item_cost):
    change = "{:.2f}".format(amount_paid - item_cost)
    split_change = str(change).split('.')
    dollars = int(split_change[0])
    coins = int(split_change[1])
    print("Change: $" + str(change))
    if dollars / 50 >= 1:
        print("$50 Bills: " + str(dollars / 50))
        dollars = dollars - ((dollars / 50) * 50)
    if dollars / 20 >= 1:
        print("$20 Bills: " + str(dollars / 20))
        dollars = dollars - ((dollars / 20) * 20)
    if dollars / 10 >= 1:
        print("$10 Bills: " + str(dollars / 10))
        dollars = dollars - ((dollars / 10) * 10)
    if dollars / 5 >= 1:
        print("$5 Bills: " + str(dollars / 5))
        dollars = dollars - ((dollars / 5) * 5)
    if dollars / 1 >= 1:
        print("$1 Bills: " + str(dollars / 1))
        dollars = dollars - ((dollars / 1) * 1)
    if coins / 25 >= 1:
        print("Quarters: " + str(coins / 25))
        coins = coins - ((coins / 25) * 25)
    if coins / 10 >= 1:
        print("Dimes: " + str(coins / 10))
        coins = coins - ((coins / 10) * 10)
    if coins / 5 >= 1:
        print("Nickels: " + str(coins / 5))
        coins = coins - ((coins / 5) * 5)
    if coins / 1 >= 1:
        print("Pennies: " + str(coins / 1))
        coins = coins - ((coins / 1) * 1)


make_change(100.00, 23.79)
