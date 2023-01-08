# File I/O Addendum

Problems 3 & 4 require you to read from files for the first time.

We'll be covering File I/O in more detail in class, but here's a quick primer that'll help you with the homework problems.

To open a file for reading in Python we use `open(filename)`, which returns a file object.

Example:

```python
fd = open("towing.csv")

# to read all data from the file into a single string
contents = fd.read()

# -OR- to read the data from the file into a list of strings, one per line:
lines = fd.readlines()

# -OR- You can also iterate over the file handle, which will iterate over lines one at a time:
for line in fd:
    print(line)
```

You can pick whichever of these you prefer for problems 3 and 4.

Once the data is read from the file you can process it using the various string methods we've already covered.

## Note

If you try to call any of the above more than once on the same file descriptor, you'll see that you don't get the data you expect.

Example:

```python

>>> fd = open("towing.csv")

>>> contents = fd.read()
>>> contents2 = fd.read()

# contents2 will be an empty string
>>> contents2 == ""
True
```

This is because once a file has been read, the "cursor" is at the end of the file.

We'll cover this in more detail in class, but for the purposes of this homework you'll only need to read each file once.
