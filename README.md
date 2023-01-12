# Homework 1

## Reminders

### Git & GitHub

If you haven't already gotten set up with GitHub, you'll want to look at [Git Basics](https://uchicago-cs.github.io/student-resource-guide/tutorials/git-basics.html) from the UChicago CS Student Resource Guide.

### Environment

For this entire course, we are assuming you are running your code on the CS department Linux environment.
This environment already has Python 3.8 installed, as well as relevant packages such as `pytest`.

You are free to develop in a setup of your choosing, but due to the infinite possible variations stemming from different operating systems, versions of Python, etc. we will not be able to provide support for issues you may run into specific to your local environment.

You may want to look at [Using VS Code and SSH](https://uchicago-cs.github.io/student-resource-guide/vscode/ssh.html) if you want to edit files on your machine and run them on the department's Linux servers.

### Style Guide

We expect you to follow the department [style guide](https://uchicago-cs.github.io/student-resource-guide/style-guide/python.html).

This counts towards 10-20% of your grade. This is not just to be picky, following code style guidelines is important in a professional setting, where you will find that reading code is just as important as writing it.

### Running `pytest`

Each problem comes with some helpful tests.  These are not guaranteed to be comprehensive, it may benefit you to consider other cases as well.

You can run `pytest` from this directory to run all tests for the homework.

It is likely more useful to either run `pytest` from within a subdirectory (e.g. `problem1/`) or, alternatively, `pytest problem1` from the main directory.

If you'd like `pytest` to stop after a single failure, add the `-x` flag.

It can also be useful to add the `-v` tag sometimes to get more verbose output.


### Code Design

You may find it useful to implement helper functions along the way,  you are always free to do so as you see fit.

Be sure to include docstrings for these helper functions.

### Submitting the Homework
After running the tests and verifying your work, you can submit the homework on [Gradescope](https://www.gradescope.com/courses/484505). Ensure that your code is clean and ready to be reviewed by the grader. You may submit as many times as you like before the deadline. 


## Problems

### Problem 1

Open `problem1/find_twos.py`, and implement the `find_twos`` function according to the specifications provided.

### Problem 2

We can represent a grid as a list of lists.  You can think of this as a two-dimensional matrix.


|   | 0 | 1 | 2 |
|---|---|---|---|
| 0 | A | B | C |
| 1 | D | E | F |
| 2 | G | H | I |

In our code, this grid would be represented as a list of lists:

```python
grid = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"]
]
```

The item at `grid[0][1]` has a value of `"B"`, whereas
`grid[1][0]` is `"D"`.

Open `problem2/grid.py`, and implement the `get_sector`` function according to the specifications provided.

### Problem 3

For this problem, we're going to deal with some real-world data.

`problem3/divvy.csv` is a comma-separated value (CSV) file [downloaded from Divvy](https://ride.divvybikes.com/system-data) with a 5000-ride sample of real-world data on bike rides for August 2022. The data has been cleaned and formatted for this homework.
**Note**: See [file-io.md](file-io.md) for details on how to open & read text from a file.

We are going to implement two functions to generate reports from this data.

`top_days(n)` should return an ordered list of the top `n` days of bike rides, ordered by `start_date`.

Each item in the list should be a tuple of the date and the number of vehicles towed.

So `top_days(3)` might return:

```python
[
  ('06/26/2022', 227),
  ('06/18/2022', 218), 
  ('06/11/2022', 207)
]
```

And `day_summary` should return a similar list of tuples, except the ordering should be by `start_date`.

```python
[
  ('06/01/2022', 155),
  ('06/02/2022', 146),
  ... # truncated
  ('06/30/2022', 149),
]
```

Open `problem3/divvy.py` & implement `top_days` and `day_summary`.

Tip #1: You may want to implement other helper functions, as always, you are free to do so however you wish.

Tip #2: You may find it useful to convert dates from strings to the `datetime` type for the purposes of comparison.

`datetime.strptime` Example:
```python
import datetime

date_str = "06/15/2022"
date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
```

### Problem 4

Nowadays we take word completion for granted. Our phones, text editors, and word processing programs all give us suggestions for how to complete words as we type based on the letters typed so far. These hints help speed up user input and eliminate common typographical mistakes (but can also be frustrating when the tool insists on completing a word that you don’t want to be completed).

You will implement two functions that such tools might use to provide command completion. The first function, `fill_completions`, will construct a dictionary designed to permit easy calculation of possible word completions. A problem for any such function is what vocabulary, or set of words, to allow completion on. Because the vocabulary you want may depend on the domain a tool is used in, you will provide `fill_completions` with a representative sample of documents from which it will build the completions dictionary. The second function, `find_completions`, will return the set of possible completions for the start of any word in the vocabulary (or the empty set if there are none). In addition to these two functions, you will implement a simple main program to use for testing your functions.

#### Specifications

`fill_completions(fd)` takes an opened file as input and returns a dictionary.

The function loops through each word in a file and builds a dictionary:

- The keys of the dictionary are tuples of the form `(n, letter)` where `n` is an integer and `letter` is a lowercase letter `a-z`.
- The value associated with the key `(n, letter)` is the set of words that contain `letter` at position `n`.  All words should be converted to lowercase for simplicity.  If the file contained the word `Python`, then `d[0, "p"]`, `d[1, "y"]`, `d[2, "t"]`, `d[4, "h"]`, `d[5, "o"]`, and `d[6, "n"]` would all contain the word `python`.
- Words must be stripped of leading & trailing punctuation.
- Words containing non-alphabetic characters are ignored, as are words of length 1.

`find_completions(prefix, comp_dict)` takes a prefix string and `comp_dict` (the result of `fill_completions`) as input.  It returns a set of strings that complete the prefix. If no words match, it returns an empty set.

`main()` is a function used to test your code. It should:

1. Open a file named `"articles.txt"`.  This file contains the text of recent news articles.
2. Calls `fill_completions` to fill out a completion dictionary.
3. Repeatedly prompts the user for a prefix to complete.
4. Prints out each word that can complete the given prefix (one per line). If no completions are possible it should print `"No completions."`.
5. Quit if the user enters the word `quit`.

At the end of your file add the lines:

```python
if __name__ == "__main__":
    main()
```

This makes it possible to call your program from the command line.

Example session:

```
$ python3 problem4.py
Enter prefix: lum
  lumley
  lump
  luminated
Enter prefix: ap
  apple
  appropriation
  ape
  aperture
Enter prefix: zz
  No completions.
Enter prefix: quit
```

**Note: the output order does not matter for this assignment.**

Write your solution in `problem4/problem4.py`.  This file does not exist yet and you will need to create it, remember to follow all style guidelines.
