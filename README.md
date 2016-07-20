## Matrix storage formats benchmark

Test how well each contact matrix storage format performs.

**Data Example:**

```
[peter@dbmipkedjievmbp matrix_storage_benchmark] [master]$ gzcat test/data/chrX_5KB_bins.tsv.gz | head -n 3
12      12      294.0
12      13      3.0
13      13      6.0
```

**Usage Example:**

```
python scripts/matrix_storage.py test/data/test.gz
```

This tiny example yields the following output:

```
[peter@dbmipkedjievmbp matrix_storage_benchmark] [master]$ python scripts/matrix_storage.py test/data/test.gz
Time loading structure: 0.07 seconds
max_x: 183.0
max_y: 184.0
Time performing range queries (256x256): 0.82 seconds (per query): 0.01 seconds
Time performing range queries (2048 x 2048): 0.80 seconds (per query): 0.01 seconds
Time slicing across first dimension: 0.32 seconds (per query): 0.00 seconds
Time slicing across second dimension: 0.32 seconds (per query): 0.00 seconds
Time slicing across the diagonal: 0.25 seconds (per query): 0.00 seconds
Size of index: 28937 bytes
```

If we use a larger contact map (5K resolution contact map of chromosomes 21 and 22) the 
performance degrades significantly. But that's ok, because the implementation
here is but a naïve toy example. Other solutions will hopefully do better.

```
[peter@dbmipkedjievmbp matrix_storage_benchmark] [master]$ python scripts/matrix_storage.py test/data/chrX_5KB_bins.tsv.gz -i 10
Time loading structure: 323.72 seconds
max_x: 31047.0
max_y: 31051.0
Time performing range queries (256x256): 145.52 seconds (per query): 14.55 seconds
Time performing range queries (2048 x 2048): 136.39 seconds (per query): 13.64 seconds
Time slicing across first dimension: 82.92 seconds (per query): 8.29 seconds
Time slicing across second dimension: 82.74 seconds (per query): 8.27 seconds
Time slicing across the diagonal: 64.85 seconds (per query): 6.49 seconds
Size of index: 69279301 bytes
```
