columns = line.split('  ')
#clean any whitespace off the items
columns = [col.strip() for col in columns]

#ensure the column has at least one value before printing
if columns:
    print "first", columns[0]  # print the first column
    print "last", columns[-1] # print the last column
