# project1
# TriviaFrenzy - A PyQt5 Trivia Game

TriviaFrenzy is a simple trivia game built with PyQt5, where users can answer multiple-choice questions. This README provides an overview of the application and instructions on how to convert it into a standalone Windows application.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Converting to a Standalone Windows Application](#converting-to-a-standalone-windows-application)
- [Documentation](#documentation)

## Features
- Multiple-choice trivia questions with correct answers.
- Keeps track of the user's score.
- Allows users to play again after completing the quiz.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/rufus800/TriviaFrenzy.git
   cd TriviaFrenzy

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Usage
Run the application:
python trivia_game.py

Answer the trivia questions and see your score at the end of the quiz.

Converting to a Standalone Windows Application
To convert this application into a standalone Windows executable, follow these steps:

Create an application icon (.ico) if you don't already have one.

Install the pyinstaller package if you haven't already:
pip install pyinstaller

Navigate to the project directory and run the following command:
pyinstaller --onefile trivia_game.py

After the process completes, find the standalone executable in the dist directory.

Double-click the executable to run the trivia game as a standalone Windows application.

