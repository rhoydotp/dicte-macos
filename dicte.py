#!/usr/bin/python

import os
import random
import time

with open('word_list') as f:
	my_lines = f.readlines()
f.close()

random.shuffle(my_lines)

print "Let's begin ..."
os.system("say -v Nicolas Commence")
time.sleep(1)

count=0
for w in my_lines:
        looper=1
        count += 1
        print "\n",count,". ",w
	say_cmd="say -v Amelie "+w
	os.system(say_cmd)
        if count <= len(my_lines):
                while looper == 1:
        		keys=raw_input("Press <Enter> for next word, <R, then ENTER> for repeat: ")
                	if keys.upper() == "R":
				os.system(say_cmd) 
                                looper=1
                        if keys == "":
                                looper=0

print "Done ..."
os.system("say -v Nicolas La Fin")
time.sleep(1)
os.system("say -v Nicolas Correction")

count=0
print "\n===== Word List Correction =====\n"
for w in my_lines:
      count += 1
      print count,". ",w 

