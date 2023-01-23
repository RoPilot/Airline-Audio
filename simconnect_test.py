from SimConnect import *
import time

try:
    sm = SimConnect()
except:
    print("ERROR | CANNOT CONNECT")
    quit()
else:
    print("CONNECTION SUCCESS")
aq = AircraftRequests(sm, _time=1000)

CONT = "0"
# To find and set timeout of cached data to 200ms:

# Get the aircraft's current altitude
while CONT != "1":
    time.sleep(1)
    PLANE_ALTITUDE = aq.get("PLANE_ALTITUDE")
    AIRSPEED_TRUE = aq.get("AIRSPEED_TRUE")
    MASTER_IGNITION_SWITCH = aq.get("MASTER_IGNITION_SWITCH")
    VERTICAL_SPEED = aq.get("VERTICAL_SPEED")
    print("-----------------------------")
    print("Speed: ", AIRSPEED_TRUE)
    print("Alt: ", PLANE_ALTITUDE)
    print("VS: ", VERTICAL_SPEED)
    print("Test: ", MASTER_IGNITION_SWITCH)
    #altitude = altitude + 1000

    # Set the aircraft's current altitude
    #aq.set("PLANE_ALTITUDE", altitude)
    
    CONT = "0"
    
    

quit()