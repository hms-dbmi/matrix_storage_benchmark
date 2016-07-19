import bisect
import csv
import os.path as op

chromInfo = {}
chromSizes = []

for assembly in ['hg19', 'hg38']:
    chromInfo[assembly] = {}
    with open(op.join(op.dirname(__file__), 'data/{}/chromInfo.txt'.format(assembly)), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        totalLength = 0

        for rec in reader:
            chromSizes += [(totalLength, rec[0])]
            totalLength += int(rec[1])

            chromInfo[assembly][rec[0]] = totalLength - int(rec[1])


def chr_pos_to_genome_pos(chromosome, nucleotide, assembly='hg19'):
    '''
    Convert chromsome / nucleotide coordinates to genome coordinates.

    Example: chr1:10 -> 10
    Example: chr2:10 -> 247,249,729 

    Where the length of chromosome 1 is 247,249,719.

    :param chromosome: The name of a chromosome (i.e. chr1)
    :param nucleotide: The nucleotide number within the chromosome
    :param chromInfo: The lengths of all the chromosomes in the genome assembly
    :return: A single integer representing the position of the read if all the chromosomes were
             concatenated
    '''
    return chromInfo[assembly][chromosome] + nucleotide

def genome_pos_to_chr_pos(genome_pos, assembly='hg19'):
    '''
    Convert genome positions to chromosome positions.

    Example: 10001 -> ['chr1', 10001]

    :param genome_pos: Genome coordinate
    :param assembly: The genome assembly we're using
    '''
    i = bisect.bisect_left(chromSizes, (genome_pos, 'x'))
    return (chromSizes[i-1][1], genome_pos - chromSizes[i-1][0])
