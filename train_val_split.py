"""
(very inefficient) splitting of parallel dataset into training and testing
"""
import sys
import random

y = [*range(399376)]
x = random.sample(y,1250)

with open('ro.tok') as infile1:
    with open('en.tok') as infile2:
        with open('src-train1k_.txt','w') as outfile1:
            with open('src-val1k_.txt','w') as outfile2:
                with open('tgt-train1k_.txt','w') as outfile3:
                    with open('tgt-val1k_.txt','w') as outfile4:
                        for i, line in enumerate(infile1):
                            if i in x[0:1000]:
                                outfile1.write(line)
                            if i in x[1000:]:
                                outfile2.write(line)
                        for i, line in enumerate(infile2):
                            if i in x[0:1000]:
                                outfile3.write(line)
                            if i in x[1000:]:
                                outfile4.write(line)

