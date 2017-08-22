#import cryspy

infile = open("list", "r")
outfile = open("list_new", "w")

elementname = ""
spheresize = ""
color = ""
iline = 0

outfile.write("colorscheme_table = {\n")
for line in infile:
    iline += 1
    words = line.split()
    if iline % 3 == 1:        
        assert words[0] == "elif", "Error! wrong first word in line %i"%(iline)
        elementname = words[3].replace('"', '').replace(":", "")
    elif iline % 3 == 2:
        assert words[0] == "spheresize", "Error! wrong first word in line %i"%(iline)
        spheresize = words[2]
    elif iline % 3 == 0:
        assert words[0] == "color", "Error! wrong first word in line %i"%(iline)
        color = "%s %s %s"%(words[2], words[3], words[4])
        outfile.write(
            '    %-6s: {"spheresize": %3s, "color": %s},\n'
            %('"%s"'%(elementname), spheresize, color)
        )
        elementname = ""
        spheresize = ""
        color = ""
outfile.write("}")

infile.close()
outfile.close()
