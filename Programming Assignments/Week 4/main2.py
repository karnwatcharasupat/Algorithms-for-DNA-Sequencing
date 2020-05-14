from utils import readFastq
from w4 import scs

seq, _ = readFastq('ads1_week4_reads.fq')

combined = scs(seq)
print(len(combined))
print(combined.count('A'))
print(combined.count('T'))