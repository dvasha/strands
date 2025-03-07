## Strands game clone:
Everyday I look forward to playing the daily [NYT Strands](https://www.nytimes.com/games/strands) puzzle.
[Wordle](https://www.nytimes.com/games/wordle), another NYT puzzle, has many clones available. Strands on the other hand? None I could find.
Let's see if I can change it!

<details>
<summary> <b>What is "Strands"?</b></summary>
Strands is a wordsearch game with a few modifications:
1. The wordlist is to be discoevered by players, they are given a clue as to what it will be through the "theme" phrase.
2. Once a word from the word list is found, it is highlighted.
3. Every puzzle has a _spanagram_. A word that goes across opposite edges of the grid. It also is highlighted in a different colour.
4. Words can be written in all directions, as long as the letters are adjacent in one of the 8 directions.
5. All letters are used exactly once as part of the puzzle. 
6. Hints are available to players, and are given on the following basis:
    - 25% of a hint is given for any word found on the board (that's not part of the wordlist)
    - extra 50% is given if the word is on theme, but not part of the wordlist.
7. If a word from the word list can be written in multiple ways, all ways to write it are a part of a valid solution to the puzzle.
</details>

### Goals:


## Programming the puzzle


Let's see

All wordlists that have the same amount of words of a certain length (for example wordlist of [10,8,7,6,6,5,4] lengths).
We can just find all layout options for a list of a certain word list, and then apply our word list across and check if  the puzzle is good enough.
Additionally, a word takes steps 


take word list and strip it to its tructure (lengths)
then build layout, with trimming places where its the same
for example it doesnt matter if word2 is of 6 and word3 is of 6, all layouts will be the same with them.
maybe just use the marker as 6, but maybe have some differentiation to ease placing into layout. placing word2 and then word2 will lead to the same results as placing word3 and then word2. 
we want to avoid duplication of results.


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
    

