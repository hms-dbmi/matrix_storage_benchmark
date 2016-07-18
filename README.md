## Matrix storage formats benchmark

Test how well each contact matrix storage format performs.

Example:

```
python scripts/matrix_storage.py test/data/test.gz
```

This tiny example yields the following output:

```
Time performing range queries: 7.07 seconds (per query): 0.07 seconds
Size of index: 313656 bytes
```

If we use a larger contact map (5K resolution contact map of chromosome X) the 
performance degrades significantly. But that's ok, because the implementation
here is but a naïve toy example. Other solutions will hopefully do better.

```
Time performing range queries: 2829.92 seconds (per query): 28.30 seconds
Size of index: 78334902 bytes
```
