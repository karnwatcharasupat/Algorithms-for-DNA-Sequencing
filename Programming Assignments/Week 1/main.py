from naive_with_rc import *
from naive_2mm import *
from utils import readGenome, readFastq
from process_quality import *

filename = r"D:\Dropbox\NTU Modules\Algorithms for DNA Sequencing\Programming Assignments\Week 1\lambda_virus.fa"
t = readGenome(filename)
# print(t)
p = str(input('Enter string to be searched: '))
print(f'p: {p}')

# p_occ, q_occ = naive_with_rc(p, t)
# print(f'Total {len(p_occ)} + {len(q_occ)} = {len(p_occ)+len(q_occ)} occurences.')
# print(f'{min(p_occ)}, {min(q_occ)} offset.')

occ = naive_2mm(p, t)
print(f'# of occ {len(occ)}, offset {min(occ)}')

# fastqfile = r"ERR037900_1.first1000.fastq"

# s, q = readFastq(fastqfile)
# fault = process_quality(q)
# print(fault)
