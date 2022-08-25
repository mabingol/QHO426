#Open file for reading
#f = open("song.txt")
#Printing a line
#print(f.readline())
#print(f.readline())
# #Print full content
#print(f.read())

#Grab content of a text file, and save it as a list
#lista = f.readlines()
#print(lista)
#f.close()

g = open("song.txt", "a")
g.write("\nAnd it's everlasting, infinite\n")
g.writelines(["It goes on and on, you can't measure it\n", "Can't quench your love"])
g.write("\nThis is the final line\n")
g.close()