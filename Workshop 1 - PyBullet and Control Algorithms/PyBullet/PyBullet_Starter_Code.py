import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally

planeId = p.loadURDF("plane.urdf")

p.setGravity(0,0,-10)

#dabba
cubeStartPos = [0,0,1]
cubeStartOrientation = [0,0,0] # in radian
boxId = p.loadURDF("dabba.urdf",cubeStartPos, p.getQuaternionFromEuler(cubeStartOrientation))

#husky
huskyStartPos = [2,0,0.1]
huskyStartOrientation = [0,0,0] # in radian
huskyId = p.loadURDF("husky/husky.urdf",huskyStartPos, p.getQuaternionFromEuler(huskyStartOrientation))

for i in range (1000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()