# Weekly Journal
5 December 2025
Rachel Yip

## Selection Sort

> Given the following list, using selection sort, sort the indicated element. Outline the steps you would follow in a way similar to the notes.

```
The List:

-- indicates that this part of the list is already sorted
** indicates the element that you should sort

  --  --  **   3    4   5
[-11,  1, 55, 43, 100, 34]

Setup:
 --  --  **   3    4   5
[-11,  1, 55, 43, 100, 34]
lowest_num = 55
lowest_index = 2

First comparison:
 --  --  **   %%    4   5
[-11,  1, 55, 43, 100, 34]

current_num = 43
lowest_num = 55
lowest_index = 2

"Current number is lower than lowest_num, set lowest_num to 45 and lowest_index to"

New Values: (if variable changes)
lowest_number = 43
lowest_index = 3

Swap!
 --  --   --   **  4   5
[-11, 1, 43,  55, 100, 34]

second comparison:
 --  --   --   **  %%   5
[-11, 1, 43,  55, 100, 34]
current_num = 100
lowest_number = 55
lowest_index = 3
"current number is not smaller than lowest num, go to the next one"

third comparison:
 --  --   --   **  4   %%
[-11, 1, 43,  55, 100, 34]

current_num = 34
lowest_num = 55
lowest_index = 3
"34 is lower than 55. Yay"

Swap!
 --  --   --  --   4   5
[-11, 1, 43,  34, 100, 55]

fourth comparisons?!
lowest_num = 100
lowest_index = 4
 --  --   --  --   **   %%
[-11, 1, 43,  34, 100, 55]

lowest_num = 100
current_num = 55
lowest_index = 4

"Oh wow the current num is lower. switcheroo"
Swap!:
 --  --  --  --   --   **
[-11, 1, 43,  34, 55, 100]
```

## Sorting Algorithms

> Check out https://visualgo.net/en/sorting.

17

## Closing Questions

> How are you feeling?

mildly sick..

> Do you have any food sensitivities or food that you avoid?

Nope. I eat everything

> What's a challenging concept, problem, or idea to understand you remember over the past week in programming?

advant of code. Did not understand how i could program to find the solutions. especially part 2 in day one.

> Happy Friday