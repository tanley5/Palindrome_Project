"""
Todo List:
1. Remove any special characters from string
2. Reverse the modified input and compare to the non flipped input
3. If the result is the same, then return "Palindrome". If not, return "Not Palindrome"
"""
import re

def palindrome_checker(word_to_check:str):
    clean_word = re.sub(r"[^a-zA-Z0-9]","",word_to_check.lower())
    word_reverse = clean_word[::-1]
    if clean_word == word_reverse:
        print(f"{word_to_check} is a Palidrome.")
    else:
        print(f"{word_to_check} is not a Palidrome.")

if __name__ == '__main__':
    string_list = [
        'Racecar',
        'Solos',
        'Kayak',
        'My gym',
        'Top spot',
        "Banana",
        "Don't nod."
    ]
    for i in string_list:
        palindrome_checker(i)