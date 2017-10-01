## SETUP
With JIVE, register:
- IA_VentilationDeviceServer_01 as epfl/vds/1
- IA_VentilationDeviceServer_02 as epfl/vds/2
- IA_HungaryDatacenter as epfl/vds3


## RUNNING
Execute "./start.sh start" to start all device servers, the simulation script and the HMI.
Execute "./start.sh stop" to stop everything.

## FILES
The sensors values for the Hungarian data center are all managed with the Python class.

The following files store the sensors/actuators' values for the Swiss data center. Each line corresponds to a different sensor/actuator:

`tmp/datacenter_temp.sensors`
| Line   | Sensor     |
|:------:|:-----------|
|   0    | temp_00    |
|   1    | temp_01    |
|   2    | temp_02    |
|   3    | temp_03    |
|   4    | temp_04    |
|   5    | temp_05    |
|   6    | temp_06    |
|   7    | temp_07    |
|   8    | temp_08    |
|   9    | temp_09    |
|   10   | temp_10    |
|   11   | temp_11    |
|   12   | temp_alarm |

`/tmp/datacenter_hum.sensors`
| Line   | Sensor    |
|:------:|:----------|
|    0   | hum_00    |
|    1   | hum_01    |
|    2   | hum_02    |
|    3   | hum_03    |
|    4   | hum_04    |
|    5   | hum_05    |
|    6   | hum_06    |
|    7   | hum_07    |
|    8   | hum_08    |
|    9   | hum_09    |
|    10  | hum_10    |
|    11  | hum_11    |
|    12  | hum_alarm |

`/tmp/datacenter_fire.sensors`:
| Line   | Sensor     |
|:------:|:-----------|
|   0    | fire_00    |
|   1    | fire_01    |
|   2    | fire_02    |
|   3    | fire_03    |
|   4    | fire_alarm |

`/tmp/datacenter_air.sensors`:
| Line   | Sensor         |
|:------:|:---------------|
|    0   | air_flow_00    |
|    1   | air_flow_01    |
|    2   | air_flow_02    |
|    3   | fan_00         |
|    4   | fan_01         |
|    5   | fan_02         |
|    6   | air_flow_alarm |

`/tmp/datacenter.actuators`:
| Line   | Actuator   |
|:------:|:-----------|
|    0   | fan_00     |
|    1   | fan_01     |
|    2   | fan_02     |
