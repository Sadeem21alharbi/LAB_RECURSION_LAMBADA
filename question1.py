
## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 


def Vowel(sentence):
    sentence = sentence.lower()

    if len(sentence)==0:
        return 0

    if sentence[0] in 'aeiou':
        return 1 + Vowel(sentence[1:])
    else:
        return Vowel(sentence[1:])
    
user_input = input("Enter a sentense! : ")
result = Vowel(user_input)
print ("Number of vowels: ", result)
