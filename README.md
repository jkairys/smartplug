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

## Config
You can provide credentials via either a config file like below
```
email: your-email
password: your-password
```

Then use the config file by specifying a path with `--config-file`
```
smartplug --config-file config/config.yaml list-devices
```

You can also provide credentials via environment variables
```
MEROSS_PASSWORD=<your-password>
MEROSS_EMAIL=<your-email>
```

## Usage
Currently there is only one command available `list-devices`. 
To use it, run the following command
```
smartplug --config-file config/config.yaml list-devices
```

Assuming all works as it should, you should see power quality and usage metrics like below:
```2022-01-27 20:28:11.912 | INFO     | smartplug.controllers.monitor:monitor:11 - plug: Pool, metrics: POWER = 0.0 W, VOLTAGE = 236.8 V, CURRENT = 0.0 A
2022-01-27 20:28:12.504 | INFO     | smartplug.controllers.monitor:monitor:11 - plug: EV, metrics: POWER = 2.109 W, VOLTAGE = 240.6 V, CURRENT = 0.036 A
2022-01-27 20:28:17.925 | INFO     | smartplug.controllers.monitor:monitor:11 - plug: Pool, metrics: POWER = 0.0 W, VOLTAGE = 236.8 V, CURRENT = 0.0 A
2022-01-27 20:28:18.609 | INFO     | smartplug.controllers.monitor:monitor:11 - plug: EV, metrics: POWER = 2.051 W, VOLTAGE = 240.6 V, CURRENT = 0.034 A
2022-01-27 20:28:24.215 | INFO     | smartplug.controllers.monitor:monitor:11 - plug: Pool, metrics: POWER = 0.0 W, VOLTAGE = 236.8 V, CURRENT = 0.0 A
2022-01-27 20:28:24.789 | INFO     | smartplug.controllers.monitor:monitor:11 - plug: EV, metrics: POWER = 2.051 W, VOLTAGE = 240.6 V, CURRENT = 0.039 A
```