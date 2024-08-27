# if/else
a = 42
if a < 10:
  print ('the number is less than 10')
else:
  print ('the number is greater or equal to 10')
# colon and proceeding indent

a = 2
b = 2
if a + b == 4:
  print ('printed when a + b equals four')
print ('always printed')

# use while to repeat actions
greetings = 1
while greetings <= 3:
  print ('Hello! ' * greetings)
  greetings = greetings + 1
# output is Hello!/ Hello! Hello!/ Hello! Hello! Hello!
# stops due to satisfying while command (3 greetings)
# !!!! infinite loops --> program freeze
# ^ doesn't freeze as 'greetings = greetings + 1' increases the no of greetings so that while comm is reached

# use for to carry out fxn /item in list
names = ['Alice', 'Bob', 'Charley']
for name in names:
  print ('Hello, ' + name)
# use n to repeat actions n times
n = 10
for i in range(n):
  print (i)
# output is 1/ 2/ 3/ 4/ 5/ 6/ 7/ 8/ 9
# range() lists integers between 0 and n
print (range(5, 12))
# guess: output is 0/1/2/3/4, 0/1/2/3/4/5/6/7/8/9/10/11/12
# output is range(5,12)
for p in range(5,12):
  print (p)
# output is 5/6/7/8/9/10/11 :)
