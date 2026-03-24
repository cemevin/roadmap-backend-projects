from fastapi import FastAPI
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# FastAPI serves index.html and allows browser requests from a different origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class LengthUnit(str, Enum):
    millimeter = "millimeter"
    centimeter = "centimeter"
    meter = "meter"
    kilometer = "kilometer"
    inch = "inch"
    foot = "foot"
    yard = "yard"
    mile = "mile"

class WeightUnit(str, Enum):
    milligram = "milligram"
    gram = "gram"
    kilogram = "kilogram"
    ounce = "ounce"
    pound = "pound"

class TemperatureUnit(str, Enum):
    celsius = "celsius"
    fahrenheit = "fahrenheit"
    kelvin = "kelvin"

@app.get("/length")
def convert_length(num: float, from_unit: LengthUnit, to_unit: LengthUnit):
    units_per_meter = {
        LengthUnit.kilometer: 0.001,
        LengthUnit.centimeter: 100,
        LengthUnit.millimeter: 1000,
        LengthUnit.meter: 1,
        LengthUnit.inch: 39.3701,
        LengthUnit.foot: 3.28084,
        LengthUnit.yard: 1.09361,
        LengthUnit.mile: 0.000621371
    }

    # convert unit to meter, then to target unit
    num_in_meter = num / units_per_meter[from_unit]
    num_converted = units_per_meter[to_unit] * num_in_meter

    return num_converted

@app.get("/weight")
def convert_weight(num: float, from_unit: WeightUnit, to_unit: WeightUnit):
    units_per_gram = {
        WeightUnit.gram: 1,
        WeightUnit.kilogram: 0.001,
        WeightUnit.milligram: 1000,
        WeightUnit.ounce: 0.035274,
        WeightUnit.pound: 0.0022046
    }

    # convert unit to gram, then to target unit
    num_in_gram = num / units_per_gram[from_unit]
    num_converted = units_per_gram[to_unit] * num_in_gram

    return num_converted


@app.get("/temperature")
def convert_temperature(num: float, from_unit: TemperatureUnit, to_unit: TemperatureUnit):
    if from_unit == to_unit:
        return num

    # convert to celsius
    if from_unit == TemperatureUnit.fahrenheit:
        num = (num - 32) * 5/9
    elif from_unit == TemperatureUnit.kelvin:
        num = num - 273.15

    # convert from celsius to f/k
    if to_unit == TemperatureUnit.fahrenheit:
        return (num * 9/5) + 32
    elif to_unit == TemperatureUnit.kelvin:
        return num + 273.15
    else:
        return num
    

# mount /static folder for root path to serve html files
BASE_DIR = Path(__file__).parent  # directory of main.py
app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")