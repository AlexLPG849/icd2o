# problem 1
def word_length_average(word_list):
    if not word_list:
        return 0.0
    total_length = sum(len(word) for word in word_list)
    return total_length / len(word_list)
words = ["apple", "kiwi", "banana", "strawberry", "blueberry"]
average_length = word_length_average(words)
print(f"Average word length in list: {average_length}")

# problem 2
def count_palindromes(word_list):
    palindromes = [word for word in word_list if word == word[::-1]]
    return len(palindromes), palindromes
words = ["level", "python", "radar", "civic", "list"]
count, palindrome_list = count_palindromes(words)
print(f"Number of palindromes: {count}")
print(f"Palindromes: {palindrome_list}")

# problem 3
def concatenate_strings(string_list):
    return ' '.join(string_list)
strings = ["Hello", "world", "of", "Python", "programming"]
result = concatenate_strings(strings)
print(f"Concatenated string: {result}")

# problem 4
def vowel_count(word_list):
    result = {}
    vowels = "aeiouAEIOU"
    for word in word_list:
        result[word] = sum(1 for char in word if char in vowels)
    return result
words = ["apple", "banana", "kiwi", "strawberry", "blueberry"]
vowel_counts = vowel_count(words)
print(f"Vowel counts: {vowel_counts}")

# problem 5
def alternate_case(word):
    result = ""
    for i, char in enumerate(word):
        if i % 2 == 0:
            result += char.lower()
        else:
            result += char.upper()
    return result
 
def alternate_case_in_list(word_list):
    return [alternate_case(word) for word in word_list]
 
word_list = ["python", "programming", "list", "iteration"]
result_list = alternate_case_in_list(word_list)
print(result_list)

# problem 6
def positive_negatives(list):
    positives = [num for num in list if num > 0]
    negatives = [num for num in list if num < 0]
    return positives, negatives
start_list = [2, 5, -8, 10, -3, 7, 1, -6]
positive_list, negative_list = positive_negatives(start_list)
print("Positive Numbers:", positive_list)
print("Negative Numbers:", negative_list)

# problem 7
def is_fibonacci(list):
    for i in range(2, len(list)):
        if list[i-1] + list[i-2] != list[i]:
            return False
    return True
start_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
print("Is Fibonacci:", is_fibonacci(start_list))

# problem 8
import math

def square_roots(list):
    return [round(math.sqrt(num)) for num in list]
start_list = [1, 4, 9, 16, 25]
result_list = square_roots(start_list)
print("Square Roots:", result_list)

# problem 9
def running_average(list):
    result = []
    total = 0
    for i, num in enumerate(list, 1):
        total += num
        result.append(total/i)
    return result
start_list = [5, 10, 15, 20, 25]
averages = running_average(start_list)
print("Running Averages:", averages)

# problem 10
def has_consecutive_pairs(list):
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) == 1:
            return True
    return False
start_list = [3, 5, 7, 9, 10, 11, 15]
print("Has Consecutive Pairs:", has_consecutive_pairs(start_list))