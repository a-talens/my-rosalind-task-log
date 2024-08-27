# files contain datasets
# open('file_name') opens files
# open('file_name', 'r/w/a')
    # read/write/append
    # write: erases same named files; append: adds to existing file
# store actions to file via variable assignment

# obtaining data from files
# v_a.read(n) return n bytes of data as string; if no n entire files is read+returned
# v_a.readline(n) returns specific line; see .strip() to remove endline \n
# v_a.readlines(n)
    #.readlines(n)[1/2/3/etc...] returns 1+1/2/3/etc... line

# to print every line in file object
# for line in v_a:
    # print line

# line.split() to make a string into a list of items
# 'Beautiful is better than ugly.\n'.split() returns ['Beautiful', 'is', 'better', 'than', 'ugly.']
    # split() returns line with whitespace as separator
# 'Explicit, is better, than implicit.'.split(",") returns ['Explicit', ' is better', ' than implicit.']
    # split(',') returns line with , as separator
# 'Simple is\nbetter than\ncomplex.\n'.splitlines() returns ['Simple is', 'better than', 'complex.']
    # splitlines() returns line with line\n boundaries

# saving files with 'w'
# .write('data you want written into file')
# .write(string) adds string contents to file
    # converting into strings uses str(variable)

# inscription = ['Rosalind Elsie Franklin ', 1920, 1958]
    # convert inscription variable's items into a string
# s = str(inscription)
# f.write(s)

# for i in inscription:
    # f.write(str(i)) + '\n')
# to give every item its own line: + '\n'

# f.close() closes file


# open rosalind 5 file, assign variable(f) to open file
# f = open('rosalind_ini5', 'r')
f = open('/Users/giel/Desktop/rosalind task logs/rosalind-task-log/rosalind_ini5')
# read all rosalind 5 lines
f.readlines(n)
# set fxn to be carried out on every line
for line in f:
   # separate line into string that separates each line
   f_sl = f.splitlines()
   if f_sl(n) % 2 == 1:
    print (f_sl)