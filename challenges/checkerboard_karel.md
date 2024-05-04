# Checkerboard Karel

## Instructions

Warning: this is really hard to get perfect!

Get Karel to create a checkerboard pattern of beepers inside an empty rectangular world, as illustrated below:


<img alt="checkerboard karel 6x6" src="https://github.com/mkrdip/codeinplace-2024/assets/3819579/3a6e3a32-536b-4418-a271-787ba9171e7e">


Note: Karel should end up where she starts

As you think about how you will solve the problem, you should make sure that your solution works with checkerboards that are different in size from the standard 6x6 checkerboard shown in the example above. Some examples of such cases are discussed below. Odd-sized checkerboards are tricky, and you should make sure that your program generates the following pattern in a 5x3 world:


<img alt="checkerboard karel 5x3" src="https://github.com/mkrdip/codeinplace-2024/assets/3819579/ac645fe5-1136-4bc6-b97c-73b271a6aff5">


This problem is hard: Try simplifying your solution with decomposition. Can you checker a single row/column? Make the row/column work for different widths/heights? Once you've finished a single row/column, can you make Karel fill two? Three? All of them? Incrementally developing your program in stages helps break it down into simpler parts and is a wise strategy for attacking hard programming problems.

