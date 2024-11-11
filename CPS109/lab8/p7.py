# Attached to this lab is a file representing a DNA sequence. The first line starts with '>' and is
# a comment, and the lines after that hold the sequence. The sequence has letters 'A', 'C', 'T',
# and 'G'. In your program for this question, read the sequence using the statements:
# # -----------------------------------------------------
# # Reading from a file
# # -----------------------------------------------------
# f = open('kdpF.txt') # opens a file for reading
# line = f.readline() # reads a single line
# print(line)
# seq = ''
# for line in f : # reading the rest of the lines
# seq = seq + line
# seq = seq.replace('\n', '') # removing the newline characters
# seq = seq.upper()
# print(seq)
# def gcContent(sequence):
# # You do the rest
# pass
# Also write a function gcContent(sequence), which returns the percent of the sequence
# which is either 'G' or 'C'. Use your function on the input sequence and print the results.

# f = open('kdpF.txt')
# line = f.readline()
# print(line)

f = open('kdpF.txt')
line = f.readline()
print(line)

seq = ''
for line in f :
  seq = seq + line

seq = seq.replace('\n', '')
seq = seq.upper()
print(seq)

def gcContent(sequence):
  count_gc = 0
  for s in sequence:
    if s == 'G' or s == 'C':
      count_gc += 1

  percentage = (count_gc / len(sequence)) * 100
  return percentage

result = gcContent(seq)
print("Percentage of GC = {:0.2f}".format(result))
