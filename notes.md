## Algotirhms:
In the spirit of Technion Algoritm 1 course:</br>
Let's start with a more casual explanation of our goals and examples to clarify!
We want to have an algorithm to generate a "Strands" puzzle, for our [NYT Strands](https://www.nytimes.com/games/strands) clone.

### What is Strands?
Strands is a (cleverly designed) wordsearch game. Player must find the theme words, among them there is a _Spanagram_, a word that goes from one edge of the grid to the opposite edge, often the key theme word. 
- Words can be written in all 8 directions
- When finding a word that isn't part of the goal theme words, user will be granted an award: precentage of a hint. If the word is "on theme" but not part of the solution of the puzzle, the award is higher.
- The puzzle solution leaves no holes
- All ways to write a certain theme word part of a valid puzzle solution.

### Some examples:
Let's see some valid and invalid layouts using this tiny 3x3 example.
<table>
<tr>
<td>A</td>   <td>B</td>    <td>C</td>
</tr>
<tr>
<td>F</td>   <td>A</td>    <td>E</td>
</tr>
<tr>
<td>D</td>   <td>O</td>    <td>E</td>
</tr>
</table>

For the word list **[ABC, FAE, DOE]** the puzzle is invalid. There are two ways to write the word ABC, one of them results in a valid puzzle, the other does not.
<table>
<tr>
<td bgcolor=#b2cdf8 font-color="black" >A</td>   <td bgcolor= #1188aa >B</td>    <td bgcolor= #1188aa >C</td>
</tr>
<tr>
<td bgcolor= >F</td>   <td bgcolor= #88aa11 >A</td>    <td bgcolor=rgb(175, 225, 136) >E</td>
</tr>
<tr>
<td bgcolor=#bb3344 >D</td>   <td = bgcolor=#ffffa>O</td>    <td>E</td>
</tr>
</table>


### Formal
Definitions:
- $Strand$ : Pair of (string, positions).</br>
Positions is a list of coordinates in a grid such that for $ i \in [0, len(S)-1], c_i \in S, dist(position(c_i),position( c_\mathrm{(i+1)}))=1$ 

- 



A strand S is valid in the layout iff for all strands that exist in the layout are part of a valid puzzle.

## Python Porgrams
### Layout.py
**input**: txt file containing a list of strings

**output**: 6 * 8 array

creates a valid layout:
- puzzle has a solution
- no holes

### Checker.py
**input**: 6 * 8 array

**output**: boolean

checks that a layout is "interesting":
- all solutions are valid (that is, all ways to construct a goal word is )


### Gameloop.py

**input**: none

**output**: none

the actual fun game, opens a layout for user to play.

### Word.py
Checks for words the user found:
- invalid word: no hint, not added to list.
- valid word:
    - if word wasn't found before add to list: 
        - if the word is above similarity threshold: 0.75 of a hint
        - else: 0.25 of a hint 
    

