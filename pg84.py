import csv
with open('abc.txt') as inf:
 content = csv.DictReader(inf)

 print("name")

 for row in content:
   print(row["Name"])
    
