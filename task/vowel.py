#Write the function "recur_fibo" to display the Fibonacci sequence.The last term enter by the user?
def removeVowels(string):
    vowel = 'aeiou'
    
    for ch in string.lower():
        if ch in vowel:
            
            string = string.replace(ch, '')

    
    print(string)

string = input('String: ')
removeVowels(string)