#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        IA_VentilationDeviceServer_02.py
#
#  Project :     IA_VentilationDeviceServer_02
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

__all__ = ["IA_VentilationDeviceServer_02", "IA_VentilationDeviceServer_02Class", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.additionnal_import

# Device States Description
# No states for this device


class IA_VentilationDeviceServer_02 (PyTango.Device_4Impl):
    """Device server representing PLC 02 managing the datacenter cooling system"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        IA_VentilationDeviceServer_02.init_device(self)
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_air_flow_00_read = 0
        self.attr_fan_02_read = 0.0
        self.attr_fire_01_read = 0
        self.attr_fire_02_read = 0
        self.attr_fire_alarm_read = 0
        self.attr_hum_00_read = 0.0
        self.attr_hum_02_read = 0.0
        self.attr_hum_04_read = 0.0
        self.attr_hum_06_read = 0.0
        self.attr_hum_08_read = 0.0
        self.attr_hum_10_read = 0.0
        self.attr_temp_00_read = 0.0
        self.attr_temp_02_read = 0.0
        self.attr_temp_04_read = 0.0
        self.attr_temp_06_read = 0.0
        self.attr_temp_08_read = 0.0
        self.attr_temp_10_read = 0.0
        self.attr_hum_alarm_read = 0
        self.attr_temp_alarm_read = 0
        self.attr_air_flow_02_read = 0
        self.attr_air_flow_alarm_read = 0
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.always_executed_hook

    # -------------------------------------------------------------------------
    #    IA_VentilationDeviceServer_02 read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_air_flow_00(self, attr):
        self.debug_stream("In read_air_flow_00()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.air_flow_00_read) ENABLED START -----#
        attr.set_value(self.attr_air_flow_00_read)
        COM_FILE_SENSORS = '/tmp/datacenter_air.sensors' 
        print("Reading the air_flow_00 sensor")
        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_air_flow_00_read = float(content[0])
                print("The air_flow_00 is ", self.attr_air_flow_00_read, content[0])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_air_flow_00_read = 0
        attr.set_value(self.attr_air_flow_00_read)
        
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.air_flow_00_read
        
    def read_fan_02(self, attr):
        self.debug_stream("In read_fan_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.fan_02_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_air.sensors' 

        print("Reading the fan_02 sensor")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_fan_02_read = float(content[5])
                print("The fan_02 is ", self.attr_fan_02_read, content[5])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read actuators from file")
            print("\t", e)
            self.attr_fan_02_read = 0

        attr.set_value(self.attr_fan_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.fan_02_read
        
    def write_fan_02(self, attr):
        self.debug_stream("In write_fan_02()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.fan_02_write) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter.actuators' 

        print("Writing to the fan_02 actuator")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.readlines()
                content[2] = str(float(data)) + '\n'
            with open(COM_FILE_SENSORS, 'w') as f:
                for line in content:
                    f.write(line)
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to write fan_02 to file")
            print("\t", e)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.fan_02_write
        
    def read_fire_01(self, attr):
        self.debug_stream("In read_fire_01()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.fire_01_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_fire.sensors' 

        print("Reading the fire_01 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_fire_01_read = int(content[1])
                print("The fire_01 is ", self.attr_fire_01_read, content[1])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_fire_01_read = 0

        attr.set_value(self.attr_fire_01_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.fire_00_read
        
    def read_fire_02(self, attr):
        self.debug_stream("In read_fire_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.fire_02_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_fire.sensors' 

        print("Reading the fire_02 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_fire_02_read = int(content[2])
                print("The fire_02 is ", self.attr_fire_02_read, content[2])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_fire_02_read = 0

        attr.set_value(self.attr_fire_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.fire_02_read
        
    def read_fire_alarm(self, attr):
        self.debug_stream("In read_fire_alarm()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.fire_alarm_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_fire.sensors' 

        print("Reading the fire_alarm actuator")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_fire_alarm_read = int(content[4])
                print("The fire_alarm is ", self.attr_fire_alarm_read, content[4])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read actuators from file")
            print("\t", e)
            self.attr_fire_alarm_read = 0

        attr.set_value(self.attr_fire_alarm_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.fire_alarm_read
        
    def read_hum_00(self, attr):
        self.debug_stream("In read_hum_00()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_00_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_00 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_00_read = float(content[0])
                print("The hum_00 is ", self.attr_hum_00_read, content[0])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_hum_00_read = 0

        attr.set_value(self.attr_hum_00_read)
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_00_read
        
    def read_hum_02(self, attr):
        self.debug_stream("In read_hum_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_02_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_02 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_02_read = float(content[2])
                print("The hum_02 is ", self.attr_hum_02_read, content[2])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_hum_02_read = 0

        attr.set_value(self.attr_hum_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_02_read
        
    def read_hum_04(self, attr):
        self.debug_stream("In read_hum_04()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_04_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_04 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_04_read = float(content[4])
                print("The hum_04 is ", self.attr_hum_04_read, content[4])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_hum_04_read = 0

        attr.set_value(self.attr_hum_04_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_04_read
        
    def read_hum_06(self, attr):
        self.debug_stream("In read_hum_06()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_06_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_06 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_06_read = float(content[6])
                print("The hum_06 is ", self.attr_hum_06_read, content[6])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_hum_06_read = 0

        attr.set_value(self.attr_hum_06_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_06_read
        
    def read_hum_08(self, attr):
        self.debug_stream("In read_hum_08()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_08_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_08 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_08_read = float(content[8])
                print("The hum_08 is ", self.attr_hum_08_read, content[8])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_hum_08_read = 0

        attr.set_value(self.attr_hum_08_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_08_read
        
    def read_hum_10(self, attr):
        self.debug_stream("In read_hum_10()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_10_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_10 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_10_read = float(content[10])
                print("The hum_10 is ", self.attr_hum_10_read, content[10])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_hum_10_read = 0

        attr.set_value(self.attr_hum_10_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_10_read
        
    def read_temp_00(self, attr):
        self.debug_stream("In read_temp_00()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_00_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_00 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_00_read = float(content[0])
                print("The temp_00 is ", self.attr_temp_00_read, content[0])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_temp_00_read = 0

        attr.set_value(self.attr_temp_00_read)
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_00_read
        
    def read_temp_02(self, attr):
        self.debug_stream("In read_temp_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_02_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_02 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_02_read = float(content[2])
                print("The temp_02 is ", self.attr_temp_02_read, content[2])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_temp_02_read = 0

        attr.set_value(self.attr_temp_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_02_read
        
    def read_temp_04(self, attr):
        self.debug_stream("In read_temp_04()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_04_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_04 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_04_read = float(content[4])
                print("The temp_04 is ", self.attr_temp_04_read, content[4])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_temp_04_read = 0

        attr.set_value(self.attr_temp_04_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_04_read
        
    def read_temp_06(self, attr):
        self.debug_stream("In read_temp_06()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_06_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_06 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_06_read = float(content[6])
                print("The temp_06 is ", self.attr_temp_06_read, content[6])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_temp_06_read = 0

        attr.set_value(self.attr_temp_06_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_06_read
        
    def read_temp_08(self, attr):
        self.debug_stream("In read_temp_08()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_08_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_8 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_8_read = float(content[8])
                print("The temp_8 is ", self.attr_temp_8_read, content[8])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_temp_8_read = 0

        attr.set_value(self.attr_temp_8_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_08_read
        
    def read_temp_10(self, attr):
        self.debug_stream("In read_temp_10()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_10_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_10 sensors")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_10_read = float(content[10])
                print("The temp_10 is ", self.attr_temp_10_read, content[10])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_temp_10_read = 0

        attr.set_value(self.attr_temp_10_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_10_read
        
    def read_hum_alarm(self, attr):
        self.debug_stream("In read_hum_alarm()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.hum_alarm_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_hum.sensors' 

        print("Reading the hum_alarm")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_hum_alarm_read = int(content[12])
                print("The hum_alarm is ", self.attr_hum_alarm_read, content[12])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read hum_alarm from file")
            print("\t", e)
            self.attr_hum_alarm_read = 0

        attr.set_value(self.attr_hum_alarm_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.hum_alarm_read
        
    def read_temp_alarm(self, attr):
        self.debug_stream("In read_temp_alarm()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.temp_alarm_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_temp.sensors' 

        print("Reading the temp_alarm")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_temp_alarm_read = int(content[12])
                print("The temp_alarm is ", self.attr_temp_alarm_read, content[12])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to temp_alarm from file")
            print("\t", e)
            self.attr_temp_alarm_read = 0

        attr.set_value(self.attr_temp_alarm_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.temp_alarm_read
        
    def read_air_flow_02(self, attr):
        self.debug_stream("In read_air_flow_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.air_flow_02_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_air.sensors' 

        print("Reading the air_flow_02 sensor")
        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_air_flow_02_read = float(content[2])
                print("The air_flow_02 is ", self.attr_air_flow_02_read, content[2])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read sensors from file")
            print("\t", e)
            self.attr_air_flow_02_read = 0

        attr.set_value(self.attr_air_flow_02_read)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.air_flow_02_read
        
    def read_air_flow_alarm(self, attr):
        self.debug_stream("In read_air_flow_alarm()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.air_flow_alarm_read) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_air.sensors' 

        print("Reading the air_flow_alarm")

        try:
            with open(COM_FILE_SENSORS, 'r') as f:
                content = f.read().splitlines()
                self.attr_air_flow_alarm_read = int(content[6])
                print("The air_flow_alarm is ", self.attr_temp_alarm_read, content[6])
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to read air_flow_alarm from file")
            print("\t", e)
            self.attr_air_alarm_read = 0
        
        attr.set_value(self.attr_air_flow_alarm_read)
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.air_flow_alarm_read
        
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.read_attr_hardware


    # -------------------------------------------------------------------------
    #    IA_VentilationDeviceServer_02 command methods
    # -------------------------------------------------------------------------
    
    def start(self):
        """ Start the fans at speed 100%
        """
        self.debug_stream("In start()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.start) ENABLED START -----#
        COM_FILE_ACTUATORS = '/tmp/datacenter.actuators'
        print("Start all fans")
        try:
            speed = 100.0
            with open(COM_FILE_ACTUATORS, 'r') as f:
                content = f.readlines()
                content[0] = content[1] = content[2] = str(speed) + '\n'
            with open(COM_FILE_ACTUATORS, 'w') as f:
                for line in content:
                    f.write(line)
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to set fan speeds to 100%")
            print("\t", e)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.start
        
    def stop(self):
        """ Stop the fans
        """
        self.debug_stream("In stop()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.stop) ENABLED START -----#
        COM_FILE_ACTUATORS = '/tmp/datacenter.actuators'
        print("Stop all fans")
        try:
            speed = 0.0
            with open(COM_FILE_ACTUATORS, 'r') as f:
                content = f.readlines()
                content[0] = content[1] = content[2] = str(speed) + '\n'
            with open(COM_FILE_ACTUATORS, 'w') as f:
                for line in content:
                    f.write(line)
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to set fan speeds to 0%")
            print("\t", e)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.stop
        
    def increase_speed_fan_02(self):
        """ Increase fan_02`s speed by 10%
        """
        self.debug_stream("In increase_speed_fan_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.increase_speed_fan_02) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_air.sensors'
        COM_FILE_ACTUATORS = '/tmp/datacenter.actuators'
        print("Increase fan_02's speed")
        try:
            speed = 0.0
            with open(COM_FILE_SENSORS, 'r') as f:
                content_sensors = f.read().splitlines()
            with open(COM_FILE_ACTUATORS, 'r') as f:
                content_actuators = f.readlines()

            speed = float(content_sensors[5])
            speed = speed + 10 if speed + 10 <= 100 else 100
            content_actuators[2] = str(speed) + '\n'
            
            with open(COM_FILE_ACTUATORS, 'w') as f:
                for line in content_actuators:
                    f.write(line)
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to increase fan_02's speed")
            print("\t", e)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.increase_speed_fan_02
        
    def decrease_speed_fan_02(self):
        """ Decrease fan_02`s speed by 10%
        """
        self.debug_stream("In decrease_speed_fan_02()")
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.decrease_speed_fan_02) ENABLED START -----#
        COM_FILE_SENSORS = '/tmp/datacenter_air.sensors'
        COM_FILE_ACTUATORS = '/tmp/datacenter.actuators'
        print("Decrease fan_02's speed")
        try:
            speed = 0.0
            with open(COM_FILE_SENSORS, 'r') as f:
                content_sensors = f.read().splitlines()
            with open(COM_FILE_ACTUATORS, 'r') as f:
                content_actuators = f.readlines()

            speed = float(content_sensors[5])
            speed = speed - 10 if speed - 10 >= 0 else 0
            content_actuators[2] = str(speed) + '\n'
            
            with open(COM_FILE_ACTUATORS, 'w') as f:
                for line in content_actuators:
                    f.write(line)
        except (IOError, ValueError, IndexError) as e:
            print("\tUnable to decrease fan_02's speed")
            print("\t", e)
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.decrease_speed_fan_02
        

    #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.programmer_methods

class IA_VentilationDeviceServer_02Class(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        'start':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'stop':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'increase_speed_fan_02':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'decrease_speed_fan_02':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'air_flow_00':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fan_02':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        'fire_01':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fire_02':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'fire_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'hum_00':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'standard unit': "%",
                'display unit': "%",
            } ],
        'hum_02':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'standard unit': "%",
                'display unit': "%",
            } ],
        'hum_04':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'standard unit': "%",
                'display unit': "%",
            } ],
        'hum_06':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'standard unit': "%",
                'display unit': "%",
            } ],
        'hum_08':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'standard unit': "%",
                'display unit': "%",
            } ],
        'hum_10':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'standard unit': "%",
                'display unit': "%",
            } ],
        'temp_00':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'standard unit': "Celsius",
                'display unit': "C",
            } ],
        'temp_02':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'standard unit': "Celsius",
                'display unit': "C",
            } ],
        'temp_04':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'standard unit': "Celsius",
                'display unit': "C",
            } ],
        'temp_06':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'standard unit': "Celsius",
                'display unit': "C",
            } ],
        'temp_08':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'standard unit': "Celsius",
                'display unit': "C",
            } ],
        'temp_10':
            [[PyTango.DevFloat,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'standard unit': "Celsius",
                'display unit': "C",
            } ],
        'hum_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'temp_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'air_flow_02':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
        'air_flow_alarm':
            [[PyTango.DevShort,
            PyTango.SCALAR,
            PyTango.READ]],
            }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(IA_VentilationDeviceServer_02Class, IA_VentilationDeviceServer_02, 'IA_VentilationDeviceServer_02')
        #----- PROTECTED REGION ID(IA_VentilationDeviceServer_02.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	IA_VentilationDeviceServer_02.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
