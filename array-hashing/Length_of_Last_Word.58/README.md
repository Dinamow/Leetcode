# Length of Last Word

Given a string `s` consists of some words separated by spaces, return the ~length of the *last* word in the string~.
A *word* is a maximal substring consisting of non-space characters only
If the last word does not exist, return 0.

### Example 1:
**Input**: s = "Hello World"
**Output**: 5
**Explanation**: The last word is "World" with length 5.

### Example 2:
**Input**: s = "    fly me   to   the moon  "
**Output**: 4
**Explanation**: The last word is "moon" with length 4.

### Example 3:
**Input**: s = "luffy is still joyboy"
**Output**: 6
**Explanation**: The last word is "joyboy" with length 6.

### Constraints:
`1 <= s.length <= 10^4`
`s` consists of only English letters and spaces `' '`. It is guaranteed that there is at least one word in `s`.

