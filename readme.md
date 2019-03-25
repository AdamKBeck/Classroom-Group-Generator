# Classroom Group (no repeats) Generator
## Overview
This tool randomly pairs up students based on a configuration file containing each student and their previous group partners. Once the tool successfully runs, it's guaranteed that students will not be paired with anyone they've been paired with before.

## Installation
Ensure that you have python3 installed. After cloning this repository, create a virtual environment and download this project's dependencies by running:

```bash
make venv
```

```bash
make update 
```

## Configuration
Now, go to the /group_generator/groups.json and edit the file according to any previous groups that have already happened. I've included the following example:

```json
{
    "adam": ["david"],
    "david": ["joe"],
    "bob": ["adam"],
    "joe": ["adam", "david"],
}
```

Looking at the first line, student *adam* has been in a group with *david*.

## Running
To run the program, simply:
```bash
make run
```

If a group is found, it will be printed out to the console.

## Output
A list of pairs will be outputted to the console. The program will make a group of 3 in the event that its input can't be evenly split.

## Assumptions
If (X,Y,Z) is a 3-paired group, there cannot be a group such as (A,X,Y). This is because X and Y worked together before.
