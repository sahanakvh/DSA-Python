# Check if a string is a palindrome
text = "madam"
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break
print("Palindrome:", is_palindrome)
