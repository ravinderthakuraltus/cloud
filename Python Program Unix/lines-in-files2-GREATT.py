#!/usr/bin/python
import re

reading = open("access_log-20161204")
chek = reading.readlines()
reading.close()

#print chek
########## TO EMPTY THE FILE ######
#with open("data", 'w'): pass
listt = []
for i in chek:
    out = re.search(r'(([2])(\d)([0]))', i)
    if out:
            listt.append(out.group(0))
print listt
print listt.count(out.group(0))
    #print listt
    #for val in i:
    #    out = re.search(r'(([2])(\d)([0]))', i)
    #    if out:

    #out = re.search(r'((^[2])(\d)([0]))', i)
    #print out.group(1)
    #wr = out.group(0)
    #if out:
        #for inp in out:
        #newf = open("data", "a+")
        #newf.write("Repeasted\n")
        #newf.close()

#count = len(open("data").readlines(  ))

#print "Total count", count


#new2 = []
#new2.append(chek)
#print new2[0]

#for i in new2:
#    print "Lines are\n", i
