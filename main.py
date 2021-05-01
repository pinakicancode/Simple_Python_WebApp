## My first FastAPI based app
## {
## Author: Pinaki Brahma
## Create Date: May 1, 2021
## Last Modified: May 1, 2021
## }

## pip install fastapi uvicorn

## 1. Load libraries
import uvicorn
from fastapi import FastAPI

## 2. Create app object
app = FastAPI()

## 3. Root route - home page
@app.get('/')
def index():
    return {'message': 'Hello World!'}

## 4. More routes - using user parameters
@app.get('/Welcome')
def getName(name: str, birthdate: str):
	display_text = 'an Original' if name == 'Arijita' else 'a Fake'
	dow = dayOfWeek(birthdate)
	return {f'Dear {name}, You are {display_text} Tuntu! And you were born on a {dow}'}

## 5. Run API with uvicorn
if __name__ == '__main__':
	uvicorn.run(app, host = '127.0.0.1', port = 8000)

# uvicorn main:app --reload

## other functions
import pandas as pd

def dayOfWeek(input_date: str):
	return pd.to_datetime(input_date).day_name()
