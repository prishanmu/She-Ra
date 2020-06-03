import re
import os
import csv


list_of_lines = []

#####
### for each file in "TV Show Scripts in TXT"
#####

import os
your_path = 'txt_scripts/'
files = os.listdir(your_path)
#keyword = 'your_keyword'
for file in files:
    s = file[0]
    e = file[1]+file[2]
    f = open(os.path.join(your_path+ file), 'r', encoding="utf8")### Open txt file to read as string
    for line in f:
        line = line.strip()
        line = re.sub("[\(\[].*?[\)\]]", "", line) ## delete any words inbetween "[" and "]": re.sub("[\(\[].*?[\)\]]", "", string)
        line = line.split(":") ##split lines by character and dialouge
        line.append(s)
        line.append(e)
        list_of_lines.append(line)


    f.close()
#####
### close txt file
#####
final_list = []
for line in list_of_lines:
    if len(line) ==4:
        final_list.append(line)

print(final_list)


#####
### open CSV file to write
#####

with open('she_ra_dialogue.csv','w', encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(['character','dialouge', 'season', 'episode']) # define CSV header
    writer.writerows(final_list) # feed list_of_lines to CSV file

f.close()
#####
### close CSV file
#####
