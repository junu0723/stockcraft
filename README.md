# STOCKCRAFT

Quant Programming in Korea stocks

## Description

Two code is implemented. `cbd.py` gathers corporation base data from KRX, and `fts.py` gets full time(2000~) Korean stock data from Yahoo finance.

I'll use these data as base data to make some insights.

## Prerequisite

Linux environment is highly required. Run setup file to install the requirements

## How to Start this Project

``` bash
# to create virtual python environment
make

# to use virtual python environment
source .venv/bin/activate
```
If you want to run existing file, there are two options(1,2)
1. (optional) launch iPython(Jupyter) and copy-paste the codes.
2. (optional) execute file like this command ``` python src/cbd.py >> log/process.log```