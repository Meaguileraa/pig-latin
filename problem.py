

# Write a function that translates english to pig latin.
# constant at the end 
# add ay at the end 
# if it already caps then it stays caps 

def pig_latin(string):
    """Given a string change the text to pig latin."""

    vowels = ['a', 'e', 'i', 'o', 'u'] # need to account for caps also 

    for char in string: 
        if char in vowels: 
            print(char)

print(pig_latin("pig")) #igpay 
print(pig_latin("egg")) #eggay
print(pig_latin("Hello")) #Ellohay
print(pig_latin("Orange")) #Orangeay
print(pig_latin("Struck")) #Uckstray - stuck here 
print(pig_latin("Hello world")) #Ellohay orldway - stuck here 
print(pig_latin("Hello, world.")) #Ellohay, orldway - stuck here 


# all constants before the first vowel get placed at the end 
# last two letters are "ay"


#pseudocode: 
# for loop through each letter 
# if statement checking if it is a constant or a vowel 
