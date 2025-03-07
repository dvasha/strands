To create puzzles, we wish to store all possible layouts. 

Lets see some solutions we can try and why we should or shouldn't use them.

### Naive Approach 1#
Backtracking on grid and wordlist. 
It's dead easy to implement, but the computation is pretty heavy, and we'd like to minimize our computation time. Let's say that our program for the word lists [BIG, BAD, WOLF, PIGGIE] and [POTATO, FRY, OIL, SALT] we got the following layouts:

|big bad wolf|chips|
|--|--|
|<table><tr>    <td>B</td>  <td>L</td>   <td>F</td>   <td>W</td>   </tr>                   <tr>    <td>P</td>   <td>I</td>   <td>O</td>  <td>B</td>   </tr>               <tr>    <td>I</td>   <td>G</td>   <td>A</td>   <td>D</td>  </tr>       <tr>    <td>G</td>   <td>G</td>   <td>I</td>   <td>E</td>  </tr></table>       |       <table><tr>    <td>F</td>  <td>L</td>   <td>T</td>   <td>S</td>   </tr>                   <tr>    <td>P</td>   <td>R</td>   <td>A</td>  <td>O</td>   </tr>               <tr>    <td>O</td>   <td>Y</td>   <td>I</td>   <td>L</td>  </tr>       <tr>    <td>T</td>   <td>A</td>   <td>T</td>   <td>O</td>  </tr></table>|

Can you notice how they have the same shapes inside? Lets write each word as it's length and the index of the letter. For example "BIG" is now (3a,3b,3c)

<table><tr>    <td>3a</td>  <td>4c</td>   <td> 4d</td>   <td>4a</td>   </tr>                   <tr>    <td>6a</td>   <td>3b</td>   <td>4b</td>  <td>3a</td>   </tr>               <tr>    <td>6b</td>   <td>3c</td>   <td>3b</td>   <td>3c</td>  </tr>       <tr>    <td>6c</td>   <td>6d</td>   <td>6e</td>   <td>6f</td>  </tr></table>

Okay, so we can solve to that problem instead, and just by doing that we can dramatically reduce computation. All* we need to do is to solve for this layout and then place letters. But can we do better?

\* We will still have to ensure that all ways to write a certain word result in a valid puzzle. We will handle this later.

### Naive Approach 2# Simplified Words

The layout we've jusut seen is better, but we're still wasting some computation power by getting multiples of the same shapes. Because our puzzle validity depends on the words themselves and their letters, we will focus on ordering the letters in a later part of the program. Let's see some example of duplication we can avoid:

|Permutation 1|Permutation 2|
|--|--|
|       <table><tr>    <td>F</td>  <td>L</td>   <td>T</td>   <td>S</td>   </tr>                   <tr>    <td>P</td>   <td>R</td>   <td>A</td>  <td>O</td>   </tr>               <tr>    <td>O</td>   <td>Y</td>   <td>I</td>   <td>L</td>  </tr>       <tr>    <td>T</td>   <td>A</td>   <td>T</td>   <td>O</td>  </tr></table>|       <table><tr>    <td>F</td>  <td>L</td>   <td>T</td>   <td>S</td>   </tr>                   <tr>    <td>P</td>   <td>R</td>   <td>A</td>  <td>O</td>   </tr>               <tr>    <td>O</td>   <td>Y</td>   <td>L</td>   <td>I</td>  </tr>       <tr>    <td>T</td>   <td>A</td>   <td>T</td>   <td>O</td>  </tr></table>|

Can you see the difference? We permutated OIL. This is the simplified layout:

|Permutation 1|Permutation 2|
|--|--|
|<table><tr>    <td>3a</td>  <td>4c</td>   <td> 4d</td>   <td>4a</td>   </tr>                   <tr>    <td>6a</td>   <td>3b</td>   <td>4b</td>  <td>3a</td>   </tr>               <tr>    <td>6b</td>   <td>3c</td>   <td>3b</td>   <td>3c</td>  </tr>       <tr>    <td>6c</td>   <td>6d</td>   <td>6e</td>   <td>6f</td>  </tr></table>| <table><tr>    <td>3a</td>  <td>4c</td>   <td> 4d</td>   <td>4a</td>   </tr>                   <tr>    <td>6a</td>   <td>3b</td>   <td>4b</td>  <td>3a</td>   </tr>               <tr>    <td>6b</td>   <td>3c</td>   <td>3c</td>   <td>3b</td>  </tr>       <tr>    <td>6c</td>   <td>6d</td>   <td>6e</td>   <td>6f</td>  </tr></table>|

Pretty similar, and considering we will have to place letters last anyway we can further simplify!

<table><tr>    <td>3</td>  <td>4</td>   <td> 4</td>   <td>4</td>   </tr>                   <tr>    <td>6</td>   <td>3</td>   <td>4</td>  <td>3</td>   </tr>               <tr>    <td>6</td>   <td>3</td>   <td>3</td>   <td>3</td>  </tr>       <tr>    <td>6</td>   <td>6</td>   <td>6</td>   <td>6</td>  </tr></table>

This reminds me of a different puzzle game, can you guess which? It's tetris!
Instead of comfortable tetrominoes, we need to tile our layout with polykings.


### Polyking tiling
Polykings, to put it simply, are 2D shapes formed by attaching squares in chess king's steps.
The last reduction took us from a list of strings [POTATO, SALT, FRY, OIL] to a list of polykings [6,4,3,3]. We're almost done! But we wish to improve even more because once again, we will have some duplicate results we'd like to prune.

If we can get one of the puzzles in the set, by flipping or rotating, we can get the others:

|base|reflection on y axis|reflection on x axis|90 degree rotation clockwise|180 degree rotation||||
|--|--|--|--|--|--|--|--|
|<table><tr>    <td>3</td>  <td>4</td>   <td> 4</td>   <td>4</td>   </tr>                   <tr>    <td>6</td>   <td>3</td>   <td>4</td>  <td>3</td>   </tr>               <tr>    <td>6</td>   <td>3</td>   <td>3</td>   <td>3</td>  </tr>       <tr>    <td>6</td>   <td>6</td>   <td>6</td>   <td>6</td>  </tr></table>|<table><tr>    <td>4</td>  <td>4</td>   <td> 4</td>   <td>3</td>   </tr>                   <tr>    <td>3</td>   <td>4</td>   <td>3</td>  <td>6</td>   </tr>               <tr>    <td>3</td>   <td>3</td>   <td>3</td>   <td>6</td>  </tr>       <tr>    <td>6</td>   <td>6</td>   <td>6</td>   <td>6</td>  </tr></table>|           <table>   <tr>    <td>6</td>   <td>6</td>   <td>6</td>   <td>6</td>  </tr>   <tr>    <td>6</td>   <td>3</td>   <td>3</td>   <td>3</td>  </tr> <tr>    <td>6</td>   <td>3</td>   <td>4</td>  <td>3</td>   </tr>     <tr>    <td>3</td>  <td>4</td>   <td> 4</td>   <td>4</td>   </tr> </table>|      |||||



