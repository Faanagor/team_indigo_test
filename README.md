# DataCapture and Stats Python Library

This Python library provides a simple implementation of a data capture system (`DataCapture`) and a set of statistical operations (`Stats`) on the captured data.

## Table of Contents

- [Installation](#Installation)
- [Technologies](#Technologies)
- [Features](#features)

## Installation

### Clone project

Clone the repository to your local machine:

```bash
git clone https://github.com/faanagor/team_indigo_test.git
cd team_indigo_test
```

### Virtual Environment

It's recommended to use a virtual environment to manage your project dependencies. You can create one using `virtualenv`:

````bash
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### Install Requirements
Once the virtual environment is activated, install the project requirements:
pip install -r requirements.txt

### Run Project
Once the requirements.txt has been installed, you need to go to the team_indigo_test directory, again, and go into the src directory. Later, you run main.py module:
```bash
cd team_indigo_test
cd src
python main.py
````

## Technologies

A list of technologies used within the project:

- [python]: Version 3.11.5

* [pytest]: Version 7.4.3
* [virtualenv]: Version 20.24.5
* [pylint]: Version 3.0.2

```

## Features

The project is composed by 2 main classes with a module test for each one:

DataCapture: Class that adds elements to list_capture, calls to Stat Class and return its result
Stats: Initialize an instance of Stats with a given data list.
```
