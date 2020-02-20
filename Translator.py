def giraffe(word):
    result=""
    for i in word:
        if i in "AEIOUaeiou":
            result+="g"
        else:
            result+=i
    return result
word="dog"
print(giraffe(word))