
filepath = 'C:/Users/pebro/source/repos/StructuredProgramming/StructuredProgramming/1a/LorumIspum.txt'
infile = open(filepath,'r')

TextList = infile.readlines()

infile.close()

infile = open(filepath,'w')

for x in TextList:

    formattedString = x.strip(['\n','\t'])
    infile.write(formattedString)
    pass