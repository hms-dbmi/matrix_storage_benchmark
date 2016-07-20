import gzip
import numpy as np
import os.path as op
import random
import sys
import time
import argparse
import negspy.coordinates as nc

def main():
    parser = argparse.ArgumentParser(description="""

    python matrix_storage_benchmark.py matrix_tsv
""")

    parser.add_argument('matrix_tsv', nargs=1)
    parser.add_argument('-s', '--square', default=256,
                                        help="The size of the square within which to return values", type=int)
    parser.add_argument('-i', '--iterations', default=100,
                                        help="The number of times to run the range query", type=int)
    #parser.add_argument('-o', '--options', default='yo',
    #                                    help="Some option", type='str')
    #parser.add_argument('-u', '--useless', action='store_true',
    #                                    help='Another useless option')

    args = parser.parse_args()

    t1 = time.time()
    array = []

    with gzip.open(args.matrix_tsv[0], 'r') as f:
        for line in f:
            # convert each contact to global genomic coordinates by adding the
            # chromosome name to its offset from the start of the genome
            parts = line.split()
            coord1 = nc.chr_pos_to_genome_pos(parts[0], int(parts[1]), 'hg19')
            coord2 = nc.chr_pos_to_genome_pos(parts[2], int(parts[3]), 'hg19')
            count = float(parts[4])
            array += [[coord1, coord2, count]]

    array = np.array(array)
    print "Time creating index: {:.2f} seconds".format(time.time() - t1)

    # the bounds of the contact coordinates
    min_x = min(array[:,0])
    min_y = min(array[:,1])

    max_x = max(array[:,0])
    max_y = max(array[:,1])

    print "max_x:", max_x
    print "max_y:", max_y

    square_size = args.square

    t2 = time.time()

    for i in range(args.iterations):
        point1 = random.randint(min_x, max_x)
        point2 = random.randint(min_y, max_y)
        selected_points = []
        
        # rectangular queries
        for j in xrange(len(array)):
            if (array[j][0] >= point1 and array[j][0] < point1 + square_size and
                array[j][1] >= point2 and array[j][1] < point2 + square_size):
                selected_points += [array[j]]
        #print "range1: [", point1, point1 + square_size,  "] range2: [", point2, point2 + square_size, "] selected:", len(selected_points)

    t25 = time.time()
    print "Time performing range queries (256x256): {:.2f} seconds (per query): {:.2f} seconds".format(t25 - t2, (t25 - t2) / args.iterations)

    for i in range(args.iterations):
        point1 = random.randint(min_x, max_x)
        point2 = random.randint(min_y, max_y)
        selected_points = []
        
        # rectangular queries
        for j in xrange(len(array)):
            if (array[j][0] >= point1 and array[j][0] < point1 + square_size * 8 and
                array[j][1] >= point2 and array[j][1] < point2 + square_size * 8):
                selected_points += [array[j]]
        #print "range1: [", point1, point1 + square_size,  "] range2: [", point2, point2 + square_size, "] selected:", len(selected_points)

    t3 = time.time()
    print "Time performing range queries (2048 x 2048): {:.2f} seconds (per query): {:.2f} seconds".format(t3 - t25, (t3 - t25) / args.iterations)

    for i in range(args.iterations):
        point1 = random.randint(min_x, max_x)
        selected_points = []

        # slice along the x dimension, so grab all points where the all x coordinates equal a certain value
        for j in xrange(len(array)):
            if array[j][0] == point1:
                selected_points += [array[j]]

    t4 = time.time()
    print "Time slicing across first dimension: {:.2f} seconds (per query): {:.2f} seconds".format(t4 - t3, (t4 - t3) / args.iterations)

    for i in range(args.iterations):
        point1 = random.randint(min_x, max_x)
        selected_points = []

        # slice along the y dimension, so grab all points where the all y coordinates equal a certain value
        for j in xrange(len(array)):
            if array[j][1] == point1:
                selected_points += [array[j]]

    t5 = time.time()
    print "Time slicing across second dimension: {:.2f} seconds (per query): {:.2f} seconds".format(t5 - t4, (t5 - t4) / args.iterations)

    for i in range(args.iterations):
        selected_points = [0]

        # slice along the diagonal, where x and y coordinates are equal
        for point in array:
            if point[0] == point[1]:
                selected_points += [point]


    t6 = time.time()
    print "Time slicing across the diagonal: {:.2f} seconds (per query): {:.2f} seconds".format(t6 - t5, (t6 - t5) / args.iterations)

    print "Size of index: {} bytes".format(op.getsize(args.matrix_tsv[0]))

    with gzip.open('/tmp/tmp.tsv', 'w') as f:
        for a in array:
            chr_pos1 = nc.genome_pos_to_chr_pos(a[0])
            chr_pos2 = nc.genome_pos_to_chr_pos(a[1])

            f.write("{}\t{}\t{}\t{}\t{:.1f}".format(chr_pos1[0], chr_pos1[1], chr_pos2[0], chr_pos2[1], a[2]))

    print "Time outputting the index: {:.2f}".format(time.time() - t3)
    print "Size of index: {} bytes".format(op.getsize(args.matrix_tsv[0]))

if __name__ == '__main__':
    main()
