def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome_word = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
number_of_palindromes = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {number_of_palindromes} times")