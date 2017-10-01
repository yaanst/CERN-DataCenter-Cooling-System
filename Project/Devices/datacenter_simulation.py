#!/usr/bin/env python

from time import sleep
from random import randrange
from datetime import datetime

MIN_TEMP = 18
MAX_TEMP = 27
MIN_HUM = 20
MAX_HUM = 80
MIN_AIR = 60
MAX_AIR = 100
MIN_FAN = 0
MAX_FAN = 100
SERVER_LOAD = 20
REFRESH_RATE = 1
COM_FILE_TEMP_SENSORS = '/tmp/datacenter_temp.sensors'
COM_FILE_HUM_SENSORS = '/tmp/datacenter_hum.sensors'
COM_FILE_FIRE_SENSORS = '/tmp/datacenter_fire.sensors'
COM_FILE_AIR_SENSORS = '/tmp/datacenter_air.sensors'
COM_FILE_ACTUATORS = '/tmp/datacenter.actuators'
FILE_LOG = '/tmp/datacenter_ch.log'

class Datacenter:
    # Actuators inialization
    fan_00 = 70
    fan_01 = 70
    fan_02 = 70
    fire_alarm = 0 
    # Sensors initialization
    fire_00 = 0
    fire_01 = 0
    fire_02 = 0
    fire_03 = 0
    air_flow_00 = 70
    air_flow_01 = 70
    air_flow_02 = 70
    air_flow_alarm = 0
    temp_00 = 22
    temp_01 = 22
    temp_02 = 22
    temp_03 = 22
    temp_04 = 22
    temp_05 = 22
    temp_06 = 22
    temp_07 = 22
    temp_08 = 22
    temp_09 = 22
    temp_10 = 22
    temp_11 = 22
    temp_alarm = 0
    hum_00 = 50
    hum_01 = 50
    hum_02 = 50
    hum_03 = 50
    hum_04 = 50
    hum_05 = 50
    hum_06 = 50
    hum_07 = 50
    hum_08 = 50
    hum_09 = 50
    hum_10 = 50
    hum_11 = 50
    hum_alarm = 0
    

    def clamp(self, value, offset, MIN, MAX):
        if value + offset > MAX:
            return MAX
        elif value + offset < MIN:
            return MIN
        else:
            return value + offset

    def react_to_alarms(self):
       """
       Function to increase/decrease speed of fans depending
       on the alarms triggered. Actions are taken by order of
       priority
       """
       if self.fire_alarm:
           self.fan_00 = 0
           self.fan_01 = 0
           self.fan_02 = 0

       elif self.temp_alarm :
           # If alarm because temp too high
           if (self.temp_00 > MAX_TEMP
               or self.temp_01 > MAX_TEMP 
               or self.temp_02 > MAX_TEMP
               or self.temp_03 > MAX_TEMP
               or self.temp_04 > MAX_TEMP
               or self.temp_05 > MAX_TEMP
               or self.temp_06 > MAX_TEMP
               or self.temp_07 > MAX_TEMP
               or self.temp_08 > MAX_TEMP
               or self.temp_09 > MAX_TEMP
               or self.temp_10 > MAX_TEMP
               or self.temp_11 > MAX_TEMP):
               self.fan_00 = self.clamp(self.fan_00, 10, MIN_FAN, MAX_FAN)
               self.fan_01 = self.clamp(self.fan_01, 10, MIN_FAN, MAX_FAN)
               self.fan_02 = self.clamp(self.fan_02, 10, MIN_FAN, MAX_FAN)
           else:
               self.fan_00 = self.clamp(self.fan_00, -10, MIN_FAN, MAX_FAN)
               self.fan_01 = self.clamp(self.fan_01, -10, MIN_FAN, MAX_FAN)
               self.fan_02 = self.clamp(self.fan_02, -10, MIN_FAN, MAX_FAN)

       elif self.hum_alarm :
           # If alarm because hum too high
           if (self.hum_00 > MAX_HUM
               or self.hum_01 > MAX_HUM 
               or self.hum_02 > MAX_HUM
               or self.hum_03 > MAX_HUM
               or self.hum_04 > MAX_HUM
               or self.hum_05 > MAX_HUM
               or self.hum_06 > MAX_HUM
               or self.hum_07 > MAX_HUM
               or self.hum_08 > MAX_HUM
               or self.hum_09 > MAX_HUM
               or self.hum_10 > MAX_HUM
               or self.hum_11 > MAX_HUM):
               self.fan_00 = self.clamp(self.fan_00, -10, MIN_FAN, MAX_FAN)
               self.fan_01 = self.clamp(self.fan_01, -10, MIN_FAN, MAX_FAN)
               self.fan_02 = self.clamp(self.fan_02, -10, MIN_FAN, MAX_FAN)
           else:
               self.fan_00 = self.clamp(self.fan_00, 10, MIN_FAN, MAX_FAN)
               self.fan_01 = self.clamp(self.fan_01, 10, MIN_FAN, MAX_FAN)
               self.fan_02 = self.clamp(self.fan_02, 10, MIN_FAN, MAX_FAN)



    def compute_air_flow(self):
        """
        Very simplistic function to compute the air_flow as the mean of
        the fans values
        """

        value = round(((self.fan_00 + self.fan_01 + self.fan_02) / 3.0), 1)
        self.air_flow_00 = self.air_flow_01 = self.air_flow_02 = value

    def compute_temp(self):
        """
        Simple inverse linear conversion from the air_flow [0;100] to the temp [10;60],
        adding
        """
        old_range = 100.0  # air_flow 0 -> 100
        new_range = -40.0   # temp 10 -> 50
        new_min = 50.0

        # Find the air_flow given by at least 2 out of 3 sensors
        air_flow = 0.0
        if not self.air_flow_alarm:
            air_flow = self.fan_00
        else:
            if self.fan_00 == self.fan_01:
                air_flow = self.fan_00
            elif self.fan_00 == self.fan_02:
                air_flow = self.fan_00
            elif self.fan_01 == self.fan_02:
                air_flow = self.fan_01

        print "COMPUTE_TEMP"
        print "air_flow: ", air_flow
        print ""

        new_temp = (((air_flow * new_range) / old_range ) + new_min)
        load_increase = new_temp * (SERVER_LOAD / 100.0)
        new_temp = self.clamp(new_temp, load_increase, 10, 50)

        new_temp = round(new_temp, 1)
        self.temp_00 = self.temp_01 = self.temp_02 = new_temp
        self.temp_03 = self.temp_04 = self.temp_05 = new_temp
        self.temp_06 = self.temp_07 = self.temp_08 = new_temp
        self.temp_09 = self.temp_10 = self.temp_11 = new_temp

    def compute_hum(self):
        """
        Simple computation for the humidity which is proportional to the air_flow and hum_ext
        """
        old_range = 100.0  # air_flow 0 -> 100
        new_range = -80.0   # hum 0 -> 90
        new_min = 90.0

        # Find the air_flow given by at least 2 out of 3 sensors
        air_flow = 0.0
        if not self.air_flow_alarm:
            air_flow = self.fan_00
        else:
            if self.fan_00 == self.fan_01:
                air_flow = self.fan_00
            elif self.fan_00 == self.fan_02:
                air_flow = self.fan_00
            elif self.fan_01 == self.fan_02:
                air_flow = self.fan_01

        new_hum = round(((air_flow * new_range) / old_range ) + new_min, 1)
        self.hum_00 = self.hum_01 = self.hum_02 = new_hum
        self.hum_03 = self.hum_04 = self.hum_05 = new_hum
        self.hum_06 = self.hum_07 = self.hum_08 = new_hum
        self.hum_09 = self.hum_10 = self.hum_11 = new_hum


    def compute_alarms(self):
        if (
            self.fire_00 
            or self.fire_01
            or self.fire_02 
            or self.fire_03) :
            self.fire_alarm = 1
        else:
            self.fire_alarm = 0


        if (
            (self.air_flow_00 < MIN_AIR and self.air_flow_01 < MIN_AIR) # Min
            or (self.air_flow_00 < MIN_AIR and self.air_flow_02 < MIN_AIR)
            or (self.air_flow_01 < MIN_AIR and self.air_flow_02 < MIN_AIR)
            or (self.air_flow_00 > MAX_AIR and self.air_flow_01 > MAX_AIR) # Max
            or (self.air_flow_00 > MAX_AIR and self.air_flow_02 > MAX_AIR)
            or (self.air_flow_01 > MAX_AIR and self.air_flow_02 > MAX_AIR) ):
            self.air_flow_alarm = 1
        else:
            self.air_flow_alarm = 0

        if (self.temp_00 > MAX_TEMP
            or self.temp_01 > MAX_TEMP # Max
            or self.temp_02 > MAX_TEMP
            or self.temp_03 > MAX_TEMP
            or self.temp_04 > MAX_TEMP
            or self.temp_05 > MAX_TEMP
            or self.temp_06 > MAX_TEMP
            or self.temp_07 > MAX_TEMP
            or self.temp_08 > MAX_TEMP
            or self.temp_09 > MAX_TEMP
            or self.temp_10 > MAX_TEMP
            or self.temp_11 > MAX_TEMP
            or self.temp_00 < MIN_TEMP # Min
            or self.temp_01 < MIN_TEMP
            or self.temp_02 < MIN_TEMP
            or self.temp_03 < MIN_TEMP
            or self.temp_04 < MIN_TEMP
            or self.temp_05 < MIN_TEMP
            or self.temp_06 < MIN_TEMP
            or self.temp_07 < MIN_TEMP
            or self.temp_08 < MIN_TEMP
            or self.temp_09 < MIN_TEMP
            or self.temp_10 < MIN_TEMP
            or self.temp_11 < MIN_TEMP) :
            self.temp_alarm = 1
        else:
            self.temp_alarm = 0


        if (self.hum_00 > MAX_HUM
            or self.hum_01 > MAX_HUM # Max
            or self.hum_02 > MAX_HUM
            or self.hum_03 > MAX_HUM
            or self.hum_04 > MAX_HUM
            or self.hum_05 > MAX_HUM
            or self.hum_06 > MAX_HUM
            or self.hum_07 > MAX_HUM
            or self.hum_08 > MAX_HUM
            or self.hum_09 > MAX_HUM
            or self.hum_10 > MAX_HUM
            or self.hum_11 > MAX_HUM
            or self.hum_00 < MIN_HUM # Min
            or self.hum_01 < MIN_HUM
            or self.hum_02 < MIN_HUM
            or self.hum_03 < MIN_HUM
            or self.hum_04 < MIN_HUM
            or self.hum_05 < MIN_HUM
            or self.hum_06 < MIN_HUM
            or self.hum_07 < MIN_HUM
            or self.hum_08 < MIN_HUM
            or self.hum_09 < MIN_HUM
            or self.hum_10 < MIN_HUM
            or self.hum_11 < MIN_HUM) :
            self.hum_alarm = 1
        else:
            self.hum_alarm = 0


    def dump_status(self):
        try:
            with open(COM_FILE_TEMP_SENSORS, 'w') as f:
                f.write(str(self.temp_00) + '\n') 
                f.write(str(self.temp_01) + '\n')
                f.write(str(self.temp_02) + '\n')
                f.write(str(self.temp_03) + '\n')
                f.write(str(self.temp_04) + '\n')
                f.write(str(self.temp_05) + '\n')
                f.write(str(self.temp_06) + '\n')
                f.write(str(self.temp_07) + '\n')
                f.write(str(self.temp_08) + '\n')
                f.write(str(self.temp_09) + '\n')
                f.write(str(self.temp_10) + '\n')
                f.write(str(self.temp_11) + '\n')
                f.write(str(self.temp_alarm) + '\n')
            with open(COM_FILE_HUM_SENSORS, 'w') as f:
                f.write(str(self.hum_00) + '\n') 
                f.write(str(self.hum_01) + '\n')
                f.write(str(self.hum_02) + '\n')
                f.write(str(self.hum_03) + '\n')
                f.write(str(self.hum_04) + '\n')
                f.write(str(self.hum_05) + '\n')
                f.write(str(self.hum_06) + '\n')
                f.write(str(self.hum_07) + '\n')
                f.write(str(self.hum_08) + '\n')
                f.write(str(self.hum_09) + '\n')
                f.write(str(self.hum_10) + '\n')
                f.write(str(self.hum_11) + '\n')
                f.write(str(self.hum_alarm) + '\n')
            with open(COM_FILE_FIRE_SENSORS, 'w') as f:
                f.write(str(self.fire_00) + '\n') 
                f.write(str(self.fire_01) + '\n')
                f.write(str(self.fire_02) + '\n')
                f.write(str(self.fire_03) + '\n')
                f.write(str(self.fire_alarm) + '\n')
            with open(COM_FILE_AIR_SENSORS, 'w') as f:
                f.write(str(self.air_flow_00) + '\n') 
                f.write(str(self.air_flow_01) + '\n') 
                f.write(str(self.air_flow_02) + '\n') 
                f.write(str(self.fan_00) + '\n') 
                f.write(str(self.fan_01) + '\n')
                f.write(str(self.fan_02) + '\n')
                f.write(str(self.air_flow_alarm) + '\n')
            with open(COM_FILE_ACTUATORS, 'w') as f:
                f.write(str(self.fan_00) + '\n')
                f.write(str(self.fan_01) + '\n')
                f.write(str(self.fan_02) + '\n')
        except (IOError, ValueError, IndexError) as e:
            print("\t Unable to store settings to files")
            print("\t", e)


    def get_settings(self):
        try:
            with open(COM_FILE_ACTUATORS, 'r') as f:
                content = f.read().splitlines()
                self.fan_00 = float(content[0])
                self.fan_01 = float(content[1])
                self.fan_02 = float(content[2])
        except (IOError, ValueError, IndexError) as e:
            print("\t Unable to read settings from files")
            print("\t", e)
            print("\t Setting default parameters")
            self.fan_00 = self.fan_01 = self.fan_02 = 70.0
    
    
    
    def print_status(self):
        print '\t temp_00: ', self.temp_00
        print '\t temp_01: ', self.temp_01
        print '\t temp_02: ', self.temp_02
        print '\t temp_03: ', self.temp_03
        print '\t temp_04: ', self.temp_04
        print '\t temp_05: ', self.temp_05
        print '\t temp_06: ', self.temp_06
        print '\t temp_07: ', self.temp_07
        print '\t temp_08: ', self.temp_08
        print '\t temp_09: ', self.temp_09
        print '\t temp_10: ', self.temp_10
        print '\t temp_11: ', self.temp_11
        print '\t temp_alarm', self.temp_alarm
        print '\t hum_00', self.hum_00
        print '\t hum_01', self.hum_01
        print '\t hum_02', self.hum_02
        print '\t hum_03', self.hum_03
        print '\t hum_04', self.hum_04
        print '\t hum_05', self.hum_05
        print '\t hum_06', self.hum_06
        print '\t hum_07', self.hum_07
        print '\t hum_08', self.hum_08
        print '\t hum_09', self.hum_09
        print '\t hum_10', self.hum_10
        print '\t hum_11', self.hum_11
        print '\t hum_alarm', self.hum_alarm
        print '\t fire_00', self.fire_00
        print '\t fire_01', self.fire_01
        print '\t fire_02', self.fire_02
        print '\t fire_03', self.fire_03
        print '\t fire_alarm', self.fire_alarm
        print '\t air_flow_00', self.air_flow_00
        print '\t air_flow_01', self.air_flow_01
        print '\t air_flow_02', self.air_flow_02
        print '\t air_flow_alarm', self.air_flow_alarm
        print '\t fan_00', self.fan_00
        print '\t fan_01', self.fan_01
        print '\t fan_02', self.fan_02

    def log_status(self):
        with open(FILE_LOG, 'a') as f:
            f.write(str(datetime.now()) + '\n')
            f.write('\t temp_00: ' + str(self.temp_00) + '\n')
            f.write('\t temp_01: ' + str(self.temp_01) + '\n')
            f.write('\t temp_02: ' + str(self.temp_02) + '\n')
            f.write('\t temp_03: ' + str(self.temp_03) + '\n')
            f.write('\t temp_04: ' + str(self.temp_04) + '\n')
            f.write('\t temp_05: ' + str(self.temp_05) + '\n')
            f.write('\t temp_06: ' + str(self.temp_06) + '\n')
            f.write('\t temp_07: ' + str(self.temp_07) + '\n')
            f.write('\t temp_08: ' + str(self.temp_08) + '\n')
            f.write('\t temp_09: ' + str(self.temp_09) + '\n')
            f.write('\t temp_10: ' + str(self.temp_10) + '\n')
            f.write('\t temp_11: ' + str(self.temp_11) + '\n')
            f.write('\t temp_alarm: ' + str(self.temp_alarm) + '\n')
            f.write('\t hum_00: ' + str(self.hum_01) + '\n')
            f.write('\t hum_01: ' + str(self.hum_01) + '\n')
            f.write('\t hum_02: ' + str(self.hum_02) + '\n')
            f.write('\t hum_03: ' + str(self.hum_03) + '\n')
            f.write('\t hum_04: ' + str(self.hum_04) + '\n')
            f.write('\t hum_05: ' + str(self.hum_05) + '\n')
            f.write('\t hum_06: ' + str(self.hum_06) + '\n')
            f.write('\t hum_07: ' + str(self.hum_07) + '\n')
            f.write('\t hum_08: ' + str(self.hum_08) + '\n')
            f.write('\t hum_09: ' + str(self.hum_09) + '\n')
            f.write('\t hum_10: ' + str(self.hum_10) + '\n')
            f.write('\t hum_11: ' + str(self.hum_11) + '\n')
            f.write('\t hum_alarm: ' + str(self.hum_alarm) + '\n')
            f.write('\t fire_00: ' + str(self.fire_00) + '\n')
            f.write('\t fire_01: ' + str(self.fire_01) + '\n')
            f.write('\t fire_02: ' + str(self.fire_02) + '\n')
            f.write('\t fire_03: ' + str(self.fire_03) + '\n')
            f.write('\t fire_alarm: ' + str(self.fire_alarm) + '\n')
            f.write('\t air_flow_00: ' + str(self.air_flow_00) + '\n')
            f.write('\t air_flow_01: ' + str(self.air_flow_01) + '\n')
            f.write('\t air_flow_02: ' + str(self.air_flow_02) + '\n')
            f.write('\t air_flow_alarm: ' + str(self.air_flow_alarm) + '\n')
            f.write('\t fan_00: ' + str(self.fan_00) + '\n')
            f.write('\t fan_01: ' + str(self.fan_01) + '\n')
            f.write('\t fan_02: ' + str(self.fan_02) + '\n')
            f.write('\n')

def simulator():
    try:
        with open(COM_FILE_ACTUATORS, 'w') as f:
            value = 70.0
            for i in range(0, 3):
                f.write(str(value) + '\n')

        with open(FILE_LOG, 'w') as f:
            f.write('\r')

    except (IOError, ValueError, IndexError) as e:
        print("\t Unable to store settings to files")
        print("\t", e)

    datacenter = Datacenter()

    iteration = 0

    try:
        while True:
            print('#######################')
            print('Iteration ', iteration)
            print('#######################')

            # Make the temp vary
            if iteration % 8 == 0:
                SERVER_LOAD = randrange(0, 50, 10)
                print "SERVER_LOAD: ", SERVER_LOAD

            # Trigger a fire sensor
            if iteration % 20 == 0:
                datacenter.fire_00 = 1
            else:
                datacenter.fire_00 = 0

            # Reset air flow to normal
            if iteration % 14 != 0:
                datacenter.air_flow_00 = datacenter.air_flow_02
                datacenter.air_flow_01 = datacenter.air_flow_02
            
            datacenter.get_settings()
            datacenter.react_to_alarms()
            datacenter.compute_air_flow()
            datacenter.compute_temp()
            datacenter.compute_hum()

            # Trigger air flow alarm
            if iteration % 14 == 0:
                datacenter.air_flow_00 = 10
                datacenter.air_flow_01 = 10

            datacenter.compute_alarms()
            datacenter.dump_status()
            datacenter.print_status()
            datacenter.log_status()
                
            iteration += 1
            sleep(REFRESH_RATE)
    except KeyboardInterrupt:
        print("Simulator stopped")

if __name__ == '__main__':
    simulator()
