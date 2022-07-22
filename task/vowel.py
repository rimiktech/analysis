def removeVowels(string):
    vowel = 'aeiou'
    
    for ch in string.lower():
        if ch in vowel:
            
            string = string.replace(ch, '')

    
    print(string)

string = input('String: ')
removeVowels(string)