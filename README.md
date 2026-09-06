# AI Recommendation System

A simple AI Recommendation System that recommends items based on user interests using similarity logic.

## Features

- Takes user interests as input
- Matches user preferences with available items
- Calculates similarity score
- Displays recommended items
- Simple web interface

## Technologies Used

- Python
- Flask
- HTML
- CSS

## How It Works

The system compares the user's interests with the interests associated with each item.

The number of matching interests is calculated as the similarity score. Items with higher scores are shown first.

## How to Run

1. Install dependencies:

   py -m pip install -r requirements.txt

2. Run the application:

   py app.py

3. Open the application in your browser:

   http://127.0.0.1:5000

## Example

Input:

python, ai

The system recommends items related to Python and Artificial Intelligence.
