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
Time creating index: 0.07 seconds
max_x: 183.0
max_y: 184.0
Time performing range queries (256x256): 0.72 seconds (per query): 0.01 seconds
Time performing range queries (2048 x 2048): 0.87 seconds (per query): 0.01 seconds
Time slicing across first dimension: 0.33 seconds (per query): 0.00 seconds
Time slicing across second dimension: 0.32 seconds (per query): 0.00 seconds
Time slicing across the diagonal: 0.25 seconds (per query): 0.00 seconds
Size of index: 28937 bytes
Time outputting the index: 0.21
Size of index: 28937 bytes
```

If we use a larger contact map (5K resolution contact map of chromosomes 21 and 22) the 
performance degrades significantly. But that's ok, because the implementation
here is but a naïve toy example. Other solutions will hopefully do better.

```
Time creating index: 336.92 seconds
max_x: 31047.0
max_y: 31051.0
Time performing range queries (256x256): 134.70 seconds (per query): 13.47 seconds
Time performing range queries (2048 x 2048): 161.33 seconds (per query): 16.13 seconds
Time slicing across first dimension: 79.64 seconds (per query): 7.96 seconds
Time slicing across second dimension: 86.46 seconds (per query): 8.65 seconds
Time slicing across the diagonal: 70.16 seconds (per query): 7.02 seconds
Size of index: 69279301 bytes
Time outputting the index: 485.33
Size of index: 69279301 bytes
```
