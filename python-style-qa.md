*Question:* I think the only thing that really confused me was the
line length limit. I know python to be a language where long one
liners are fairly common, so I'm shocked to see a line limit enforced,
and I still don't really understand why.

*Answer:* Line length limits are programming language agnostic.

Consider this line in C++:

`if (process_vector(sum_vectors(create_new_vector(0, 1, 0), create_new_vector(1, 1, 0))) != 0 && is_valid_input(user_string) && as_int(user_string) > 5 && as_int(user_string) < 20) {`

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
