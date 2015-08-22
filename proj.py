#!/bin/python

f = open("dna2.fasta")

count = 0
with open("dna2.fasta") as f:
    for l in f:
        if l.startswith('>'):
            name = l[1:].rstrip('\n')
            count = count + 1
            sequences =[]

        else:

            sequences += l[:-1]
            my_file = open("out_"+str(count)+"_.txt", "w")
            my_file.write(str(len(sequences)))

print count
f.close
