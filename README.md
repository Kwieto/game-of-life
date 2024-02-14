# TLDR 
Run `run.sh` if you don't have Python installed to run using Docker

## Game of life

![Game of life screenshot](https://github.com/Kwieto/game-of-life/blob/main/img.png?raw=true)

I wanted to try out some Python so I decided to create a simple Game of life.
These are the rules:

    - Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies, as if by overpopulation.
    - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial generation of the field is randomized. After a few generations the field will regenerate to create some eye-candy.