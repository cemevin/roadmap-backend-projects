# Unit Converter

A simple web app to convert between units of length, weight, and temperature. Built with FastAPI (backend) and Bootstrap (frontend).

## Features

- **Length** — millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
- **Weight** — milligram, gram, kilogram, ounce, pound
- **Temperature** — Celsius, Fahrenheit, Kelvin

## Project Structure

```
unit_converter/
├── pyproject.toml
└── app/
    ├── main.py        # FastAPI app and conversion logic
    ├── __init__.py
    └── static/
        └── index.html # Frontend (Bootstrap + vanilla JS)
```

## Running the App

**Install dependencies**
```bash
pip install fastapi uvicorn
```

**Start the server**
```bash
fastapi dev app/main.py
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

## API

The frontend communicates with three GET endpoints:

```
GET /length?num=20&from_unit=foot&to_unit=centimeter
GET /weight?num=5&from_unit=kilogram&to_unit=pound
GET /temperature?num=100&from_unit=celsius&to_unit=fahrenheit
```

You can explore and test all endpoints interactively at [http://localhost:8000/docs](http://localhost:8000/docs).