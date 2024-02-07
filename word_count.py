def word_count(input):
    count = 0
    for letter in input:
        if letter == " ":
             count += 1
    return count
    

input = input("Enter a text: ")
count_new = word_count(input)
print()
print("You have "+str(count_new)+" words in your text")
