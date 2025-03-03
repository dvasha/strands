## Algotirhms:
In the spirit of Technion Algoritm 1 course:</br>
Let's start with a more casual explanation of our goals and examples to clarify!
We want to have an algorithm to generate a "Strands" puzzle, for our [NYT Strands](https://www.nytimes.com/games/strands) clone.


#### What is Strands?
Strands is a modified wordsearch game. In addition to having a _spanagram_ (word that goes from one side of the table to the opposite side), words can be written in all directions (where each letter is a chess king's step away) and all cells are used in the solution.

#### Some examples:
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

For the word list **[ABC, FAE, DOE]** the puzzle is invalid. There are two ways to write the word ABC, one of them results in a valid solution, the other does not.
|valid solution|invalid solution|
|--|--|
|<table> <tr> <td>**A**</td>   <td>**B**</td>    <td>**C**</td> </tr><tr><td>F</td>   <td>A</td>    <td>E</td></tr><tr><td>_D_</td>   <td>_O_</td>    <td>_E_</td></tr></table>|<table><tr><td>A</td>   <td>**B**</td>    <td>**C**</td></tr><tr><td>F</td>  <td>**A**</td> <td>E</td> </tr> <tr> <td>_D_</td>   <td>_O_</td>    <td>_E_</td></tr></table>|
|| no valid way to get "FAE"|

For the word list **[BIG, FAE, DOE]** the following puzzle is valid since all ways to construct the words exists in a valid solution.
|valid solution 1|valid solution 2|
|--|--|
|<table> <tr> <td>B</td>   <td>I</td>    <td>G</td> </tr><tr><td>**F**</td>   <td>**A**</td>    <td>**E**</td></tr><tr><td>_D_</td>   <td>_O_</td>    <td>_E_</td></tr></table>|<table> <tr> <td>B</td>   <td>I</td>    <td>G</td> </tr><tr><td>**F**</td>   <td>**A**</td>    <td>_E_</td></tr><tr><td>_D_</td>   <td>_O_</td>    <td>**E**</td></tr></table>|

Now that we've seen some examples, we can move forward to getting a formal solution for our problem. 

### Formal Solution
Definitions:
- Puzzle $P\in L(W)$
- Words: set of strings $W=\{w_1, w_2,...\}$
- Layout $L:W\rightarrow M(a,b)$ function that maps a word list to a matrix of a x b, such that for word $w$ all characters are within 1 cell in the matrix. $$c{ _\mathrm{i+1}}.x,c{ _\mathrm{i+1}}.y \in [c_i.x-1,c_i.y-1]\times[c_i.x+1,c_i.y+1] / [c_i.x,c_i.y]$$
- Stranding of word $\tilde{w}$ in puzzle $P$ is a 

A puzzle is valid if for all instances of word, there exists a solution for the puzzle.


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
    

