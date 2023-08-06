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


wordToTest = 'Hello, World!'
print(wordToTest)

reversedWord = reverseTheString(wordToTest)
reversedWord2 = reverse_string(wordToTest)
print("1: Looping til middle simultaneously swapping: ", reversedWord)
print("2: Using slice to reverse: ", reversedWord2)