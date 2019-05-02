# number-pyramid-calculation
Ungolfed solution for: https://codegolf.stackexchange.com/questions/184951/upside-down-pyramid-addition-reversed#184951

Note that the specifications detailed in the link above wanted the input to be the right side diagonal of the pyramid,
from bottom to top, like so:
2 1 1
 3 2
  5
Input: [5, 2, 1]

And the output was to be the top line read left-to-right, like so:
Output: [2, 1, 1]

However, I wrote this program so the input would be, essentially, the left-side diagonal from top to bottom:
1 1 2
 2 3
  5
Input: [1, 2, 5]
Output: [1, 1, 2]

(Output is still left-to-right along the top line, though.)
This can be easily fixed by adding a list(reversed()) around the input and around the output.
However, I feel that doing so muddies the program for no real gain. Since this isn't a proper code golf solution,
I've thus chosen to leave the program as-is, without the list(reversed()) function calls.
