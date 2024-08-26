# assign items to lists via list_name = [item_1, item_2, etc]
# python uses 0-based nu'ing so item_1 is position 0: list_name[0]
# add items to lists via append() fxn: list_name.append()
# list slicing allows for item retrieval
# - e.g. 5 items, [-2:] returns the same items as [3:]

# lists contain sep items
# strings contain sep characters: '' format
# strings can be sliced like lists

# task: return list slice given instructions
# sample: FAIL CODE! not sure why not working
# TypeError: can only concatenate list (not "str") to list
 # list = ['HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.']
 # a = 22
 # b = 27
 # c = 29
 # d = 102
 # print (list[a:b] + ' ' + list[c:d])

# Rosalind explanation
# substrings: specified via slice notation
# strings/slices can be concatenated(=joined) via +
# [a:b+1]: +1 as pyhton doesn't include final index otherwise

string = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
a = 22
b = 27
c = 97
d = 102
print (string[a:b+1] + ' ' + string[c:d+1])
# or assign slice lengths to variable names, to break up slicing(?)
string = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
output1 = string[a:b+1]
output2 = string[c:d+1]
print (output1 + ' ' + output2)
# output is Humpty Dumpty either way (yay!)

# task
string = 'i5uvg3yGFXkgaV3OBM58Q7czjuzR9MXHwR6sqNhN5ydcUcHyHsMargaritifera2qjLmkGEWY5MSnGBRhmutabilisMr9dT8aixm8D0KMReKWThBQRYRzIQGn2yjDT7FamTySMO1U01qTVvZHNwgIpR0QL8rCN62lGa1qP4t7.'
a, b, c, d = 50, 62, 81, 89
print (string[a:b+1] + ' ' + string[c:d+1])
# output is Margaritifera mutabilis
# list variables and assigned values as above to use less lines

#27/8/24