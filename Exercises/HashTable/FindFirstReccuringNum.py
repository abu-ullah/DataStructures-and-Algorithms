def findFirstReccuringDigit(arrOfInts):
    if type(arrOfInts) != list:
        return 'Invalid Input!'
    
    if len(arrOfInts) == 0:
        return 'Empty array!'
    
    map = {}
    for i in range(len(arrOfInts)):
        if arrOfInts[i] in map:
            return arrOfInts[i]
        map[arrOfInts[i]] = i
    return 'No reccuring digits'

print(findFirstReccuringDigit([2,5,1,2,3,5,1,2,4])) 
print(findFirstReccuringDigit([2,1,1,2,3,5,1,2,4]))
print(findFirstReccuringDigit([2,3,4,5]))  