import numpy as np
import os.path as op
import random
import sys
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="""

    python matrix_storage_benchmark.py matrix_tsv
""")

    parser.add_argument('matrix_tsv', nargs=1)
    parser.add_argument('-r', '--resolution', default=5000,
                                        help="The resolution of the data", type=int)
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
    array = np.loadtxt(args.matrix_tsv[0])

    print "Time loading structure: {:.2f} seconds".format(time.time() - t1)
    min_x = min(array[:,0])
    min_y = min(array[:,1])

    max_x = max(array[:,0])
    max_y = max(array[:,1])

    resolution = args.resolution
    square_size = args.square

    t2 = time.time()

    for i in range(args.iterations):
        point1 = (random.randint(min_x, max_x) / resolution) * resolution
        point2 = (random.randint(min_y, max_y) / resolution) * resolution
        selected_points = []
        
        for j in xrange(len(array)):
            if (array[j][0] >= point1 and array[j][0] < point1 + resolution * square_size and
                array[j][1] >= point2 and array[j][1] < point2 + resolution * square_size):
                selected_points += [array[j]]
        print "range1: [", point1, point1 + resolution * square_size,  "] range2: [", point2, point2 + resolution * square_size, "] selected:", len(selected_points)

    t3 = time.time()
    print "Time performing range queries: {:.2f} seconds (per query): {:.2f} seconds".format(t3 - t2, (t3 - t2) / args.iterations)
    print "Size of index: {} bytes".format(op.getsize(args.matrix_tsv[0]))



if __name__ == '__main__':
    main()
