# Simple, given a string of words, return the length of the shortest word(s)



def solution(words):
    astring = words.split('')
    shortest = astring[0]
    for word in astring:
        if len(word) < len(shortest):
            shortest = word
        return len(word)
   
   
   
