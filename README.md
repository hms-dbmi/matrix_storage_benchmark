## Matrix storage formats benchmark

Test how well each contact matrix storage format performs.

Input data format:

```
chr1 pos1 chr2 pos2 count```
```

** Data Example: **

```
chr22   16050000        chr22   16055000        9.0
chr22   16055000        chr22   16060000        1.0
chr22   16060000        chr22   16060000        1.0
chr22   16065000        chr22   16070000        1.0
chr22   16215000        chr22   16215000        1.0
```

** Usage Example: **

```
python scripts/matrix_storage.py test/data/test.gz
```

This tiny example yields the following output:

```
[peter@computer matrix_storage_benchmark] [master]$ python scripts/matrix_storage.py test/data/test.gz
Time creating index: 0.04 seconds
Time performing range queries: 1.17 seconds (per query): 0.01 seconds
Time outputting the index: 0.26
Size of index: 37396 bytes
```

If we use a larger contact map (5K resolution contact map of chromosomes 21 and 22) the 
performance degrades significantly. But that's ok, because the implementation
here is but a naïve toy example. Other solutions will hopefully do better.

```
[peter@computer matrix_storage_benchmark] [master]$ python scripts/matrix_storage.py test/data/chr21_chr22.tsv.gz
Time creating index: 39.26 seconds
Time performing range queries: 396.82 seconds (per query): 3.97 seconds
Time outputting the index: 186.62
Size of index: 28141265 bytes
```
