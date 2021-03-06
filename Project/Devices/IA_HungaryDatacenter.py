#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        IA_HungaryDatacenter.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      a$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["IA_HungaryDatacenter", "IA_HungaryDatacenterClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(IA_HungaryDatacenter.additionnal_import) ENABLED START -----#
from random import randrange

#----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.additionnal_import

# Device States Description
# No states for this device


class IA_HungaryDatacenter (PyTango.Device_4Impl):
    """Device server representing the state of the Hungarian CERN datacenter"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(IA_HungaryDatacenter.global_variables) ENABLED START -----#
    
    global new_temp
    global new_hum
    global new_air_flow
    global new_fan
    global new_fire
    global iteration

    # Default values
    iteration = 0
    new_temp = [22 for _ in range(12)] 
    new_hum = [50 for _ in range(12)]
    new_fan = [70 for _ in range(3)]
    new_air_flow = [70 for _ in range(3)]
    new_fire = [0 for _ in range(4)]
    
    def clamp(self, value, offset, MIN, MAX):
        if value + offset > MAX:
            return MAX
        elif value + offset < MIN:
            return MIN
        else:
            return value + offset

    #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        IA_HungaryDatacenter.init_device(self)
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_temp_00_read = 0.0
        self.attr_temp_01_read = 0.0
        self.attr_temp_02_read = 0.0
        self.attr_temp_03_read = 0.0
        self.attr_temp_04_read = 0.0
        self.attr_temp_05_read = 0.0
        self.attr_temp_06_read = 0.0
        self.attr_temp_07_read = 0.0
        self.attr_temp_08_read = 0.0
        self.attr_temp_09_read = 0.0
        self.attr_temp_10_read = 0.0
        self.attr_temp_11_read = 0.0
        self.attr_hum_00_read = 0.0
        self.attr_hum_01_read = 0.0
        self.attr_hum_02_read = 0.0
        self.attr_hum_03_read = 0.0
        self.attr_hum_04_read = 0.0
        self.attr_hum_05_read = 0.0
        self.attr_hum_06_read = 0.0
        self.attr_hum_07_read = 0.0
        self.attr_hum_08_read = 0.0
        self.attr_hum_09_read = 0.0
        self.attr_hum_10_read = 0.0
        self.attr_hum_11_read = 0.0
        self.attr_air_flow_00_read = 0.0
        self.attr_air_flow_01_read = 0.0
        self.attr_air_flow_02_read = 0.0
        self.attr_fire_00_read = 0
        self.attr_fire_01_read = 0
        self.attr_fire_02_read = 0
        self.attr_fire_03_read = 0
        self.attr_fan_00_read = 0.0
        self.attr_fan_01_read = 0.0
        self.attr_fan_02_read = 0.0
        self.attr_temp_alarm_read = 0
        self.attr_fire_alarm_read = 0
        self.attr_air_flow_alarm_read = 0
        self.attr_hum_alarm_read = 0
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.always_executed_hook

    # -------------------------------------------------------------------------
    #    IA_HungaryDatacenter read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_temp_00(self, attr):
        self.debug_stream("In read_temp_00()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_00_read) ENABLED START -----#
        global new_temp
        self.attr_temp_00_read = new_temp[0]
        attr.set_value(self.attr_temp_00_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_00_read
        
    def read_temp_01(self, attr):
        self.debug_stream("In read_temp_01()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_01_read) ENABLED START -----#
        global new_temp
        self.attr_temp_01_read = new_temp[1]
        attr.set_value(self.attr_temp_01_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_01_read
        
    def read_temp_02(self, attr):
        self.debug_stream("In read_temp_02()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_02_read) ENABLED START -----#
        global new_temp
        self.attr_temp_02_read = new_temp[2]
        attr.set_value(self.attr_temp_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_02_read
        
    def read_temp_03(self, attr):
        self.debug_stream("In read_temp_03()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_03_read) ENABLED START -----#
        global new_temp
        self.attr_temp_03_read = new_temp[3]
        attr.set_value(self.attr_temp_03_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_03_read
        
    def read_temp_04(self, attr):
        self.debug_stream("In read_temp_04()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_04_read) ENABLED START -----#
        global new_temp
        self.attr_temp_04_read = new_temp[4]
        attr.set_value(self.attr_temp_04_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_04_read
        
    def read_temp_05(self, attr):
        self.debug_stream("In read_temp_05()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_05_read) ENABLED START -----#
        global new_temp
        self.attr_temp_05_read = new_temp[5]
        attr.set_value(self.attr_temp_05_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_05_read
        
    def read_temp_06(self, attr):
        self.debug_stream("In read_temp_06()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_06_read) ENABLED START -----#
        global new_temp
        self.attr_temp_06_read = new_temp[6]
        attr.set_value(self.attr_temp_06_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_06_read
        
    def read_temp_07(self, attr):
        self.debug_stream("In read_temp_07()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_07_read) ENABLED START -----#
        global new_temp
        self.attr_temp_07_read = new_temp[7]
        attr.set_value(self.attr_temp_07_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_07_read
        
    def read_temp_08(self, attr):
        self.debug_stream("In read_temp_08()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_08_read) ENABLED START -----#
        global new_temp
        self.attr_temp_08_read = new_temp[8]
        attr.set_value(self.attr_temp_08_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_08_read
        
    def read_temp_09(self, attr):
        self.debug_stream("In read_temp_09()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_09_read) ENABLED START -----#
        global new_temp
        self.attr_temp_09_read = new_temp[9]
        attr.set_value(self.attr_temp_09_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_09_read
        
    def read_temp_10(self, attr):
        self.debug_stream("In read_temp_10()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_10_read) ENABLED START -----#
        global new_temp
        self.attr_temp_10_read = new_temp[10]
        attr.set_value(self.attr_temp_10_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_10_read
        
    def read_temp_11(self, attr):
        self.debug_stream("In read_temp_11()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_11_read) ENABLED START -----#
        global new_temp
        self.attr_temp_11_read = new_temp[11]
        attr.set_value(self.attr_temp_11_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_11_read
        
    def read_hum_00(self, attr):
        self.debug_stream("In read_hum_00()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_00_read) ENABLED START -----#
        global new_hum
        self.attr_hum_00_read = new_hum[0]
        attr.set_value(self.attr_hum_00_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_00_read
        
    def read_hum_01(self, attr):
        self.debug_stream("In read_hum_01()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_01_read) ENABLED START -----#
        global new_hum
        self.attr_hum_01_read = new_hum[1]
        attr.set_value(self.attr_hum_01_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_01_read
        
    def read_hum_02(self, attr):
        self.debug_stream("In read_hum_02()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_02_read) ENABLED START -----#
        global new_hum
        self.attr_hum_02_read = new_hum[2]
        attr.set_value(self.attr_hum_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_02_read
        
    def read_hum_03(self, attr):
        self.debug_stream("In read_hum_03()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_03_read) ENABLED START -----#
        global new_hum
        self.attr_hum_03_read = new_hum[3]
        attr.set_value(self.attr_hum_03_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_03_read
        
    def read_hum_04(self, attr):
        self.debug_stream("In read_hum_04()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_04_read) ENABLED START -----#
        global new_hum
        self.attr_hum_04_read = new_hum[4]
        attr.set_value(self.attr_hum_04_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_04_read
        
    def read_hum_05(self, attr):
        self.debug_stream("In read_hum_05()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_05_read) ENABLED START -----#
        global new_hum
        self.attr_hum_05_read = new_hum[5]
        attr.set_value(self.attr_hum_05_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_05_read
        
    def read_hum_06(self, attr):
        self.debug_stream("In read_hum_06()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_06_read) ENABLED START -----#
        global new_hum
        self.attr_hum_06_read = new_hum[6]
        attr.set_value(self.attr_hum_06_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_06_read
        
    def read_hum_07(self, attr):
        self.debug_stream("In read_hum_07()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_07_read) ENABLED START -----#
        global new_hum
        self.attr_hum_07_read = new_hum[7]
        attr.set_value(self.attr_hum_07_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_07_read
        
    def read_hum_08(self, attr):
        self.debug_stream("In read_hum_08()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_08_read) ENABLED START -----#
        global new_hum
        self.attr_hum_08_read = new_hum[8]
        attr.set_value(self.attr_hum_08_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_08_read
        
    def read_hum_09(self, attr):
        self.debug_stream("In read_hum_09()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_09_read) ENABLED START -----#
        global new_hum
        self.attr_hum_09_read = new_hum[9]
        attr.set_value(self.attr_hum_09_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_09_read
        
    def read_hum_10(self, attr):
        self.debug_stream("In read_hum_10()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_10_read) ENABLED START -----#
        global new_hum
        self.attr_hum_10_read = new_hum[10]
        attr.set_value(self.attr_hum_10_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_10_read
        
    def read_hum_11(self, attr):
        self.debug_stream("In read_hum_11()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_11_read) ENABLED START -----#
        global new_hum
        self.attr_hum_11_read = new_hum[11]
        attr.set_value(self.attr_hum_11_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_11_read
        
    def read_air_flow_00(self, attr):
        self.debug_stream("In read_air_flow_00()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.air_flow_00_read) ENABLED START -----#
        global new_air_flow
        self.attr_air_flow_00_read = new_air_flow[0]
        attr.set_value(self.attr_air_flow_00_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.air_flow_00_read
        
    def read_air_flow_01(self, attr):
        self.debug_stream("In read_air_flow_01()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.air_flow_01_read) ENABLED START -----#
        global new_air_flow
        self.attr_air_flow_01_read = new_air_flow[1]
        attr.set_value(self.attr_air_flow_01_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.air_flow_01_read
        
    def read_air_flow_02(self, attr):
        self.debug_stream("In read_air_flow_02()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.air_flow_02_read) ENABLED START -----#
        global new_air_flow
        self.attr_air_flow_02_read = new_air_flow[2]
        attr.set_value(self.attr_air_flow_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.air_flow_02_read
        
    def read_fire_00(self, attr):
        self.debug_stream("In read_fire_00()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fire_00_read) ENABLED START -----#
        global new_fire
        self.attr_fire_00_read =  new_fire[0]
        attr.set_value(self.attr_fire_00_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fire_00_read
        
    def read_fire_01(self, attr):
        self.debug_stream("In read_fire_01()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fire_01_read) ENABLED START -----#
        global new_fire
        self.attr_fire_01_read = new_fire[1]
        attr.set_value(self.attr_fire_01_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fire_01_read
        
    def read_fire_02(self, attr):
        self.debug_stream("In read_fire_02()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fire_02_read) ENABLED START -----#
        global new_fire
        self.attr_fire_02_read = new_fire[2]
        attr.set_value(self.attr_fire_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fire_02_read
        
    def read_fire_03(self, attr):
        self.debug_stream("In read_fire_03()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fire_03_read) ENABLED START -----#
        global new_fire
        self.attr_fire_03_read = new_fire[3]
        attr.set_value(self.attr_fire_03_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fire_03_read
        
    def read_fan_00(self, attr):
        self.debug_stream("In read_fan_00()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fan_00_read) ENABLED START -----#
        global new_fan
        self.attr_fan_00_read = new_fan[0]
        attr.set_value(self.attr_fan_00_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fan_00_read
        
    def read_fan_01(self, attr):
        self.debug_stream("In read_fan_01()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fan_01_read) ENABLED START -----#
        global new_fan
        self.attr_fan_01_read = new_fan[1]
        attr.set_value(self.attr_fan_01_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fan_01_read
        
    def read_fan_02(self, attr):
        self.debug_stream("In read_fan_02()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fan_02_read) ENABLED START -----#
        global new_fan
        self.attr_fan_02_read = new_fan[2]
        attr.set_value(self.attr_fan_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fan_02_read
        
    def read_temp_alarm(self, attr):
        self.debug_stream("In read_temp_alarm()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.temp_alarm_read) ENABLED START -----#
        print "Read temp alarm"

        global new_temp
        global iteration
        global server_load
        MIN_TEMP = 18
        MAX_TEMP = 27
        
        # Compute the new temperatures
        old_range = 100.0     # air_flow 0 -> 100
        new_range = -40.0     # temp 10 -> 50
        new_min = 50.0

        if iteration % 8 == 0:
            # Generate a new random server_load value
            server_load = randrange(0, 50, 10)
            print "SERVER_LOAD: ", server_load
        iteration += 1

        # Find the air_flow given by at least 2 out of 3 sensors if one is malfunctioning
        air_flow = 0
        if not self.attr_air_flow_alarm_read:
            air_flow = self.attr_fan_00_read
        else:
            if self.attr_fan_00_read == self.attr_fan_01_read:
                air_flow = self.attr_fan_00_read
            elif self.attr_fan_00_read == self.attr_fan_02_read:
                air_flow = self.attr_fan_00_read
            elif self.attr_fan_01_read == self.attr_fan_02_read:
                air_flow = self.attr_fan_01_read

        temp = (((air_flow * new_range) / old_range ) + new_min)
        load_increase = temp * (server_load / 100.0)
        temp = self.clamp(temp, load_increase, 10, 50)
        temp = round(temp, 1)

        new_temp = [temp for _ in range(len(new_temp))]
        
        # Compute the temp alarm
        if (self.attr_temp_00_read > MAX_TEMP
            or self.attr_temp_01_read > MAX_TEMP # Max
            or self.attr_temp_02_read > MAX_TEMP
            or self.attr_temp_03_read > MAX_TEMP
            or self.attr_temp_04_read > MAX_TEMP
            or self.attr_temp_05_read > MAX_TEMP
            or self.attr_temp_06_read > MAX_TEMP
            or self.attr_temp_07_read > MAX_TEMP
            or self.attr_temp_08_read > MAX_TEMP
            or self.attr_temp_09_read > MAX_TEMP
            or self.attr_temp_10_read > MAX_TEMP
            or self.attr_temp_11_read > MAX_TEMP

            or self.attr_temp_00_read < MIN_TEMP # Min
            or self.attr_temp_01_read < MIN_TEMP
            or self.attr_temp_02_read < MIN_TEMP
            or self.attr_temp_03_read < MIN_TEMP
            or self.attr_temp_04_read < MIN_TEMP
            or self.attr_temp_05_read < MIN_TEMP
            or self.attr_temp_06_read < MIN_TEMP
            or self.attr_temp_07_read < MIN_TEMP
            or self.attr_temp_08_read < MIN_TEMP
            or self.attr_temp_09_read < MIN_TEMP
            or self.attr_temp_10_read < MIN_TEMP
            or self.attr_temp_11_read < MIN_TEMP) :
            self.attr_temp_alarm_read = 1
        else:
            self.attr_temp_alarm_read = 0
        attr.set_value(self.attr_temp_alarm_read)
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.temp_alarm_read
        
    def read_fire_alarm(self, attr):
        self.debug_stream("In read_fire_alarm()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.fire_alarm_read) ENABLED START -----#
        global new_fan
        global new_fire
        global iteration
        MIN_TEMP = 18
        MAX_TEMP = 27
        MIN_HUM = 20
        MAX_HUM = 80
        MIN_FAN = 0
        MAX_FAN = 100

        # Trigger a fire sensor from time to time
        if iteration % 6 == 0:
            new_fire[0] = 1
        else:
            new_fire = [0 for _ in range(len(new_fire))]


        # Compute fire alarm
        if (self.attr_fire_00_read
            or self.attr_fire_01_read
            or self.attr_fire_02_read
            or self.attr_fire_03_read):
            self.attr_fire_alarm_read = 1
        else:
            self.attr_fire_alarm_read = 0

        # React to alarms
        print "React to alarm"
        if self.attr_fire_alarm_read:
            new_fan = [0 for _ in range(len(new_fan))]

        elif self.attr_temp_alarm_read :
            # If alarm because temp too high
            if (self.attr_temp_00_read > MAX_TEMP
                or self.attr_temp_01_read > MAX_TEMP 
                or self.attr_temp_02_read > MAX_TEMP
                or self.attr_temp_03_read > MAX_TEMP
                or self.attr_temp_04_read > MAX_TEMP
                or self.attr_temp_05_read > MAX_TEMP
                or self.attr_temp_06_read > MAX_TEMP
                or self.attr_temp_07_read > MAX_TEMP
                or self.attr_temp_08_read > MAX_TEMP
                or self.attr_temp_09_read > MAX_TEMP
                or self.attr_temp_10_read > MAX_TEMP
                or self.attr_temp_11_read > MAX_TEMP):
                new_fan[0] = self.clamp(self.attr_fan_00_read, 10, MIN_FAN, MAX_FAN)
                new_fan[1] = self.clamp(self.attr_fan_01_read, 10, MIN_FAN, MAX_FAN)
                new_fan[2] = self.clamp(self.attr_fan_02_read, 10, MIN_FAN, MAX_FAN)
            else:
                new_fan[0] = self.clamp(self.attr_fan_00_read, -10, MIN_FAN, MAX_FAN)
                new_fan[1] = self.clamp(self.attr_fan_01_read, -10, MIN_FAN, MAX_FAN)
                new_fan[2] = self.clamp(self.attr_fan_02_read, -10, MIN_FAN, MAX_FAN)

        elif self.attr_hum_alarm_read :
            # If alarm because hum too high
            if (self.attr_hum_00_read > MAX_HUM
                or self.attr_hum_01_read > MAX_HUM 
                or self.attr_hum_02_read > MAX_HUM
                or self.attr_hum_03_read > MAX_HUM
                or self.attr_hum_04_read > MAX_HUM
                or self.attr_hum_05_read > MAX_HUM
                or self.attr_hum_06_read > MAX_HUM
                or self.attr_hum_07_read > MAX_HUM
                or self.attr_hum_08_read > MAX_HUM
                or self.attr_hum_09_read > MAX_HUM
                or self.attr_hum_10_read > MAX_HUM
                or self.attr_hum_11_read > MAX_HUM):
                new_fan[0] = self.clamp(self.attr_fan_00_read, -10, MIN_FAN, MAX_FAN)
                new_fan[1] = self.clamp(self.attr_fan_01_read, -10, MIN_FAN, MAX_FAN)
                new_fan[2] = self.clamp(self.attr_fan_02_read, -10, MIN_FAN, MAX_FAN)
            else:
                new_fan[0] = self.clamp(self.attr_fan_00_read, 10, MIN_FAN, MAX_FAN)
                new_fan[1] = self.clamp(self.attr_fan_01_read, 10, MIN_FAN, MAX_FAN)
                new_fan[2] = self.clamp(self.attr_fan_02_read, 10, MIN_FAN, MAX_FAN)


        attr.set_value(self.attr_fire_alarm_read)
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.fire_alarm_read
        
    def read_air_flow_alarm(self, attr):
        self.debug_stream("In read_air_flow_alarm()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.air_flow_alarm_read) ENABLED START -----#
        global new_air_flow

        # Compute new_air_flow
        new_value = self.attr_fan_00_read + self.attr_fan_01_read + self.attr_fan_02_read
        new_value = round((new_value / 3.0), 1)
        new_air_flow = [new_value for _ in range(len(new_air_flow))]

        MIN_AIR = 66
        MAX_AIR = 100
        if (
            (self.attr_air_flow_00_read < MIN_AIR and self.attr_air_flow_01_read < MIN_AIR)
            or (self.attr_air_flow_00_read < MIN_AIR and self.attr_air_flow_02_read < MIN_AIR)
            or (self.attr_air_flow_01_read < MIN_AIR and self.attr_air_flow_02_read < MIN_AIR)

            or (self.attr_air_flow_00_read > MAX_AIR and self.attr_air_flow_01_read > MAX_AIR)
            or (self.attr_air_flow_00_read > MAX_AIR and self.attr_air_flow_02_read > MAX_AIR)
            or (self.attr_air_flow_01_read > MAX_AIR and self.attr_air_flow_02_read > MAX_AIR)
            ):
            self.attr_air_flow_alarm_read = 1
        else:
            self.attr_air_flow_alarm_read = 0

        attr.set_value(self.attr_air_flow_alarm_read)
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.air_flow_alarm_read
        
    def read_hum_alarm(self, attr):
        self.debug_stream("In read_hum_alarm()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.hum_alarm_read) ENABLED START -----#
        global new_hum
        MIN_HUM = 20
        MAX_HUM = 80

        old_range = 100  # air_flow 0 -> 100
        new_range = -60   # hum 20 -> 80
        new_min = 80


        # Find the air_flow given by at least 2 out of 3 sensors
        air_flow = 0
        if not self.attr_air_flow_alarm_read:
            air_flow = self.attr_fan_00_read
        else:
            if self.attr_fan_00_read == self.attr_fan_01_read:
                air_flow = self.attr_fan_00_read
            elif self.attr_fan_00_read == self.attr_fan_02_read:
                air_flow = self.attr_fan_00_read
            elif self.attr_fan_01_read == self.attr_fan_02_read:
                air_flow = self.attr_fan_01_read

        hum = int(round(((air_flow * new_range) / old_range ) + new_min))
        new_hum = [hum for _ in range(len(new_hum))]
        
        # Compute the alarm
        if (self.attr_hum_00_read > MAX_HUM
            or self.attr_hum_01_read > MAX_HUM # Max
            or self.attr_hum_02_read > MAX_HUM
            or self.attr_hum_03_read > MAX_HUM
            or self.attr_hum_04_read > MAX_HUM
            or self.attr_hum_05_read > MAX_HUM
            or self.attr_hum_06_read > MAX_HUM
            or self.attr_hum_07_read > MAX_HUM
            or self.attr_hum_08_read > MAX_HUM
            or self.attr_hum_09_read > MAX_HUM
            or self.attr_hum_10_read > MAX_HUM
            or self.attr_hum_11_read > MAX_HUM

            or self.attr_hum_00_read < MIN_HUM # Min
            or self.attr_hum_01_read < MIN_HUM
            or self.attr_hum_02_read < MIN_HUM
            or self.attr_hum_03_read < MIN_HUM
            or self.attr_hum_04_read < MIN_HUM
            or self.attr_hum_05_read < MIN_HUM
            or self.attr_hum_06_read < MIN_HUM
            or self.attr_hum_07_read < MIN_HUM
            or self.attr_hum_08_read < MIN_HUM
            or self.attr_hum_09_read < MIN_HUM
            or self.attr_hum_10_read < MIN_HUM
            or self.attr_hum_11_read < MIN_HUM) :
            self.attr_hum_alarm_read = 1
        else:
            self.attr_hum_alarm_read = 0
        attr.set_value(self.attr_hum_alarm_read)
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.hum_alarm_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.read_attr_hardware


    # -------------------------------------------------------------------------
    #    IA_HungaryDatacenter command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(IA_HungaryDatacenter.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.programmer_methods

class IA_HungaryDatacenterClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(IA_HungaryDatacenter.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'temp_00':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_01':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_02':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_03':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_04':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_05':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_06':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_07':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_08':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_09':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_10':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_11':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_00':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_01':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_02':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_03':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_04':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_05':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_06':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_07':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_08':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_09':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_10':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_11':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'air_flow_00':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'air_flow_01':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'air_flow_02':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'fire_00':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fire_01':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fire_02':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fire_03':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fan_00':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'fan_01':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'fan_02':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'fire_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'air_flow_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'hum_ext':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(IA_HungaryDatacenterClass, IA_HungaryDatacenter, 'IA_HungaryDatacenter')
        #----- PROTECTED REGION ID(IA_HungaryDatacenter.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_HungaryDatacenter.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
