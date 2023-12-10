# CS420 AI Project Maze Solver
## Getting Started
### Installing
* Clone the project to your computer. 
```
  git clone https://github.com/vinhhn2210/cs420-ai-project-maze-solver.git
```
* Set up Pygame Library:
```
  python3 -m pip install -U pygame --user
```
* Run the program:
```
  python main.py
```

### Executing program
* Using an IDE to compile this game (Sublime Text 3, Visual Studio Code, ...)
* Remember to add all source codes to project before building and running
* Run file main.py to enjoy the Game

## How To Use
### Adding new maps
* Put new map in .txt format in /Map directory.
* Rename new map file's name to format input**X**-level**Y**.txt (**X**: new map's ordinal number, **Y**: level of new map).



### Solving
1. To automaticly solving all map with all current algorithms:
* python3 Sources/system.py Map auto
2. To solve with specify map-algorithm and guide:
* python3 Sources/system.py Map guide
3. To visualize
* python3 main.py