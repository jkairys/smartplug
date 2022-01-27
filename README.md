# smartplug

This project is a quick test of the meross_iot package for interacting with Meross IOT devices, specifcally smart plugs.
The initial goal is a PoC to retrieve power measurement data from one or more plug devices, with a view to ingest it into a database for basic aggregations and further analysis.

## Setup
Create an python virtual environment and install the project dependencies.
```
virturalenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Install the package in editable mode for local CLI use.
```
pip install --editable .
```

## Usage
Currently there is only one command available `list-devices`. 
To use it