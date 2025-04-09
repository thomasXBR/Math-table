# Brief explanation
This Python program prints the multiplication table for a number entered by the user.

## Breakdown:
It asks the user to input an integer:
```n = int(input(...))```
<br>
<br>
If the number is 0, it prints a message that the multiplication table of 0 is always 0 and exits.
<br>
<br>
Otherwise, it uses a while loop and a for loop together to generate and print the multiplication table from 1 to 10.
<br>
<br>
The for loop goes from ```n``` to ```n*10``` + ```n``` with step ```n```, effectively generating:
```n, 2n, 3n, ..., 10n```
<br>
<br>
At the same time, ```i``` (the multiplier) goes from 1 to 10.
<br>
<br>
It prints each line in the format:
```n * i = result```
