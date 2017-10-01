#!/bin/bash

case "$1" in
    "start")
        # Start each device server and redirect stdout & stderr to /tmp/vds#.output
        echo "*** Starting device servers..."
        ./Devices/IA_VentilationDeviceServer_01.py vds1 1> /tmp/vds1.output 2>&1 &
        echo "vds1   OK"
        ./Devices/IA_VentilationDeviceServer_02.py vds2 1> /tmp/vds2.output 2>&1 &
        echo "vds2   OK"
        ./Devices/IA_HungaryDatacenter.py vds3 1> /tmp/vds3.output 2>&1 &
        echo "vds3   OK"

        # Wait for them to be correctly 
        # started before getting PIDs
        sleep 1

        # Get PIDs and store them for later use
        VDS1=$(pgrep -f "vds1")
        VDS2=$(pgrep -f "vds2")
        VDS3=$(pgrep -f "vds3")
        echo $VDS1 > /tmp/vds1.pid
        echo $VDS2 > /tmp/vds2.pid
        echo $VDS3 > /tmp/vds3.pid
        


        echo "*** Starting the simulator..."
        python Devices/datacenter_simulation.py 1> /tmp/simulator.output 2>&1 &
        echo " OK"

        sleep 1
        
        SIM=$(pgrep -f "datacenter_simulation")

        echo $SIM > /tmp/simulator.pid

        
        
        echo "*** Starting the HMI..."
        # cd is needed for tango to correctly display images
        cd HMI 
        python HMI.py 1> /tmp/HMI.output 2>&1 &
        cd ..
        echo " OK"
        
        # sleep until HMI is up and has PID
        sleep 2
        
        HMI=$(pgrep -f "HMI")
        
        echo $HMI > /tmp/HMI.pid
        ;;

    "stop")
        # Retrieve all PIDs
        VDS1=$(cat /tmp/vds1.pid)
        VDS2=$(cat /tmp/vds2.pid)
        VDS3=$(cat /tmp/vds3.pid)
        SIM=$(cat /tmp/simulator.pid)
        HMI=$(cat /tmp/HMI.pid)

        echo "*** Stopping device servers..."
        kill $VDS1
        echo "vds1   OK"
        kill $VDS2
        echo "vds2   OK"
        kill $VDS3
        echo "vds3   OK"
        echo " OK"
        
        echo "*** Stopping simualtor..."
        kill $SIM
        echo " OK"

        echo "*** Stopping HMI..."
        kill $HMI
        echo " OK"
        ;;

    
    *)
        echo "Usage: start.sh {start|stop}"
        ;;
esac
