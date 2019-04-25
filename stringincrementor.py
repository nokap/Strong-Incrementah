def string_increment(word): #defining function with intake of word
    word = list(word) #turning the string into a list (so that indeces can be accessed individually)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #making array of numbers because depending on the ending number in the input, different actions occur.
    number = '' #empty set for number becaues it is constantly changing
    for x in range(len(word)): #for a variable within the range and length of the input word..
        character = word[x] #character is iterator as access point (index value) of the word
        if character in numbers: #if that specific access point is in numbers...
            number += character #if condition is met.... modify number so that number now is equal itself + character
        if character == '0' and word[x-1] in numbers: #if the character is 0 and the last index value in the word (because -1 is last value) is in numbers...
            number += character #if condition is met... modify number so that number is now equal to itself + character.

    for i in range(len(number)): #for iterator in new number set
        word.remove(number[i]) #remove iterator for the number set from word list.
    if number == "": #stating if a number is the same as an empty set...
        number = 0 #number set becomes 0
    print(number) #print the number set
    number = int(number) #the number is equal to an integer not a string.
    number += 1 # the number is equal to itself plus 1 to meet the condition of foo1 etc.
    print(word) #print the word
    word.append(str(number)) #add the number set as a string to word list.
    word = ''.join(word) 
    return(word)

print(string_increment("foo"))
