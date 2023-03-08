#!/usr/bin/env python3
import operator
import re
import sys
import csv
num_errors={}
count_entries={}
c=0
b=0
d=0
with open("example_syslog.txt") as file:
   searchforentry=r"ticky: ([A-Z]*): ([\w ]*)\[?#?[1-9]*?\]? ?\((\w*)\)"
   for line in file:
      result=re.search(searchforentry,line)
      print(result)
      if result[1]=="ERROR":
         if result[2] in num_errors:
            num_errors[result[2]]["Count"]+=1
         else:
            num_errors[result[2]]={"Count":1,"Error":result[2]}
         if result[3] in count_entries:
            count_entries[result[3]]["ERROR"]+=1
         else:
            count_entries[result[3]]={"Username":result[3],"INFO":0,"ERROR":1}   
      if result[1]=="INFO":
        if result[3] in count_entries:
           count_entries[result[3]]["INFO"]+=1
        else:
           count_entries[result[3]]={"Username":result[3],"INFO":1,"ERROR":0}
print(num_errors,count_entries,"\n\n")
entries=sorted(count_entries.items())
errors=sorted(num_errors.items(), key=operator.itemgetter(1),reverse=True)
errors_head=["Error","Count"]
entries_head=["Username","INFO","ERROR"]
print(errors,entries)
a=[]
b=[]
with open("error_message.csv","w") as e:
 writer = csv.DictWriter(e,fieldnames=errors_head)
 writer.writeheader()
 for i,(key,value) in enumerate(errors):
   a.append(value)
 print("\n\n",a,type(a)) 
 writer.writerows(a)
with open("user_statistics.csv","w") as u:
  writer = csv.DictWriter(u,fieldnames=entries_head)
  writer.writeheader()
  for i,(key,value) in enumerate(entries):
    b.append(value)
  writer.writerows(b)

