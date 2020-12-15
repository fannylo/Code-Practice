#For check node name of TR69
import os
import sys

#Comment is writed in check.sh
cmd1 = "grep '<Name>' sh3-getDevice.20201203.txt | sed 's/^[ \t]*//g' | cut -b 7- | sed 's/........$//' > final.csv"
os.system(cmd1)
cmd2 = "sed s/[[:space:]]//g check_item.csv | sed 's/(.*)//' | sed 's/\[.*\]//' > check_item2.csv"
os.system(cmd2)

with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
   fileone = f1.readlines() #check_item2
   filetwo = f2.readlines() #final

with open(sys.argv[3], 'w') as outfile:
   for line1 in fileone:
      check = 0
      for line2 in filetwo:
         #The Python strip() method is used to remove the specified characters 
         #(space or newline by default) or character sequence at the beginning
         #and end of a string.
         if line1.strip() == line2.strip():
            check = 1
            break
      if check == 1:
         print 'Yes'
         outfile.write('Y'+'\n')
      else:
         print 'No'
         outfile.write('N'+'\n')

f1.close()
f2.close()
outfile.close()
      
