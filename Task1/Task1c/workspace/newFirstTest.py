try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim
emptyBuff=bytearray()
if clientID!=-1:
    print ('Connected to remote API server')
    #sim.simxGetObjectHandle
    #time.sleep()
    #sim.simxGetJointPosition--cannot be used with spherical joints
    #simx_opmode_streaming  -- non blocking , runs continously on the server side
    #simx_opmode_buffer -- non blocking mode, this does not send any command sees if t=any orevious reply is left
    #sim.simxSetJointTargetPosition
    #sim.simxAddStatusbarMessage
    #sim.simxAddStatusbarMessage(clientID,'Hello CoppeliaSim!',sim.simx_opmode_oneshot)
    returnCode,outInts, outFloats, outStrings, outBuffer=sim.simxCallScriptFunction(clientID,'Dummy',sim.sim_scripttype_childscript,'myFunction',[],[],[],emptyBuff,sim.simx_opmode_blocking)
    print(returnCode)

    
    
    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
