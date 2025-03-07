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
