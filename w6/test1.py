line ="" 
inputFileName = input("Enter name of input file: ")
inputFile = open(inputFileName, "r")
print("Opening file", inputFileName, " for reading.")

for line in inputFile:
    print(line, end="")

inputFile.close()
print("\n Completed reading of file", inputFileName)