# Line Lengths

*Question:* I think the only thing that really confused me was the
line length limit. I know python to be a language where long one
liners are fairly common, so I'm shocked to see a line limit enforced,
and I still don't really understand why.

*Answer:* Line length limits are programming language agnostic.

Consider this line in C++:

```c++
if (process_vector(sum_vectors(create_new_vector(0, 1, 0), create_new_vector(1, 1, 0))) != 0 && is_valid_input(user_string) && as_int(user_string) > 5 && as_int(user_string) < 20) {
```

This line is simply too long to be legible! It wraps unpleasantly in
IDEs and text editors, or requires scrolling to the right. It should
be broken up simply to make it more legible:

```c++
vector3 up_vector = create_new_vector(0, 1, 0);
vector3 up_right_vector = create_new_vector(1, 1, 0);
vector3 summed_vector = sum_vectors(up_vector, up_right_vector);
int process_result = process_vector(summed_vector);
if (process_result != 0
	&& is_valid_input(user_string)
	&& as_int(user_string) > 5
	&& as_int(user_string) < 20)
{

```

The same applies to Python and to all programming languages and text files.

# Calling Main

*Question:* Something I am still confused about is why we do if
__name__ == "__main__": main() to call main.

*Answer:* Python scripts simply run top-to-bottom when executed _or
imported_. Say you write a python file named lists.py. It contains
useful fuctions like `build_list()` and `sort_list()`. When run, it
uses `build_list()` to get input from the user and `sort_list()` to
send the input to a server for sorting. It looks something like this:

```python
def build_list():
	... code here ...

def sort_list(l):
	... code here ...

print(sort_list(build_list()))
```

Now you want to write another Python file that also wants to deal with
lists. It would be handy to import the `build_list()` and
`sort_list()` functions so you don't have to write them again.
So, you write this import statement at the top of your new file:

```python
import lists
```

When running it, it asks the user for list input and sends it to a
server for sorting. Oops! That's because the `import` statement runs
the entire target file.

To get the best of both worlds, where Python files can be imported
_or_ run and behave appropriately in both situations, we change
`lists.py` slightly:

```python
def build_list():
	... same as before ...

def sort_list(l):
	... same as before ...

if __name__ == '__main__':
	# this code will not run when imported!
	print(sort_list(build_list()))
```

Now executing `lists.py` still does we wanted, but _importing_
`lists.py` only imports the functions without also executing the main
code of the file.

# Docstrings

*Question:* I am a bit confused about why docstrings are the first
statement inside a function/class. In pretty much every other language
I've seen, it seems like the convention is to have it before the
object/function/statement it describes. It seems like a multi-line
docstring would make a function less readable since it splits up the
function name and arguments from the rest of the code.

*Answer:* Docstrings are actually a part of the Python interpreter!
You can use the built-in `help()` function to read the docstring of
any function or module that has one. Putting the docstring after the
function name makes it unambiguous to parse, whereas a docstring
before a function could just be an errant multi-line comment.

# Problems Caused by Defying Style

*Question:* While I know we need to adhere to the style guide for the
labs and assignments, how much of this would cause problems when
trying to run code if we didn't follow the style guide? Are certain
conventions used to prevent problems that only appear sometimes but
not all the time?

*Answer:* This will not cause any compilation errors, but since all
python projects use this style guide, collaboration (which is how
almost all code is written) will become difficult.

The style is meant to reduce bugs, for example by mismatched
indentation causing unexpected behavior.

# Tab vs. Spaces

*"Question":* What I find most "interesting" is the whole tab vs 4
spaces thing, I just find it really convenient to just press tab so
I'm very curious as why they decided to opt for 4 spaces instead.

*Answer:* This isn't really a question but I wanted to address it
anyway -- you don't have to press space 4 times to input 4 spaces! You
can still just press tab! It's a matter of character encoding --
there's a difference between the tab character `'\t'` and the space
character `' '`. Tabs can be configured to render at different
indentation levels, whereas spaces cannot. The use of spaces in Python
is to prevent a tabstop of 8 characters instead of 4 characters from
causing ambiguous rendering. Take this code, written using tabs and
not spaaces:

```python
if x == y:
    if y == z:
        print('x = y = z')
```

With an 8 character tabstop, this code would render like this:

```python
if x == y:
        if y == z:
                print('x = y = z')
```

Since whitespace in Python matters, the shift in indentation on
different screens can cause wrapping to look very different to two
different people working on the same code, which can cause
communication problems.


