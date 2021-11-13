upperLimit = 101
lowerLimit = 1
reverseString = "Hello World!"
reverseInteger = -865
sentenceAverage = "Hello, my name is Joseph, I'm from Knoxville, Tennessee."
number1 = "123"
number2 = "456"
palindrome = "radkar"

#  Print numbers from low to high
def low_to_high(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit):
        print(i)

#  Print numbers from high to low
def high_to_low(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit):
        print(upperLimit - i)

#  Print string in reverse
def reverse_string(string):
    print(string)[::-1]

#  Count by given integer
def count_by_integer(lower_limit, upper_limit, integer):
    for i in range(lower_limit, upper_limit):
        if i == lowerLimit:
            print(i)
            x = i + integer
        if i == x:
            print(i)
            x = i + integer

#  Reverse digits in string of numbers
def reverse_digits(integer):
    string = str(integer)
    if string[0] == "-":
        print("-" + string[:0:-1])
    else:
        print string[::-1]

#  Calculate average word length
def average_word_length(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)

#  Add two strings together without casting
def add_strings(string1, string2):
    sumStrings = eval(string1) + eval(string2)
    print(sumStrings)

#  Determine if word is valid palindrome
#def valid_palindrome(word):

#  Determine the index of the first non-repeating character in string
#def first_unique_character(string):

#  Determine whether array of integers is monotonic or not
#def monotonic_array(array):

#  Move zeroes to end of array
#def move_zeroes(array):

#  Fill in None values in array
#def fill_none(array):

#  Matched and mismatched words
#def match_words(sentence1, sentence2):

#  Prime Numbers Array
#def prime_numbers(array):

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

golden_ratio(10)