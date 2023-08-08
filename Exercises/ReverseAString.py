def reverseTheString(word):
    if word is None or len(word) < 2 or type(word) != str:
        return 'Invalid Input'
        
    chars = list(word)
    start = 0
    end = len(chars) - 1
    while start < end:
        temp = chars[start]
        chars[start] = chars[end]
        chars[end] = temp
        
        start += 1
        end -= 1
    
    return "".join(chars)
        

def reverse_string(input_string):
    return input_string[::-1]


def reverse_string_recursion(input_string):
    # Base case: if the string is empty or has only one character, return it
    if len(input_string) <= 1:
        return input_string
    
    # Recursive case: reverse the substring excluding the first and last characters,
    # and then concatenate the first and last characters in reverse order
    return input_string[-1] + reverse_string_recursion(input_string[1:-1]) + input_string[0]


wordToTest = 'Hello, World!'
print(wordToTest)

reversedWord = reverseTheString(wordToTest)
reversedWord2 = reverse_string(wordToTest)
reversedWord3 = reverse_string_recursion(wordToTest)
print("1: Looping til middle simultaneously swapping: ", reversedWord)
print("2: Using slice to reverse: ", reversedWord2)
print("3: Using recursion: ", reversedWord3)