## Differential Drive implemented on Husky 

import pybullet as p
import pybullet_data
p.connect(p.GUI)  #or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)
carpos = [0, 0, 0.1]

car = p.loadURDF("husky/husky.urdf", carpos[0], carpos[1], carpos[2])
numJoints = p.getNumJoints(car)
for joint in range(numJoints):
  print(p.getJointInfo(car, joint))
targetVel = 10    #rad/s
maxForce = 100    #Newton

## These Values can be changed to modify the turning radius
targetVel_max = 3
targetVel_max_reverse = -3
target_diff_drive = 2
targetVel_stop = 0

while (True):
    keys = p.getKeyboardEvents()
    for k, v in keys.items():
        ## Forward
        if (k == p.B3G_UP_ARROW and (v & p.KEY_IS_DOWN)):
            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity = targetVel_max, force = maxForce)
           
            p.stepSimulation()

        if (k == p.B3G_UP_ARROW and (v & p.KEY_WAS_RELEASED)):
            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity = targetVel_stop,force = maxForce)
            
            p.stepSimulation()
          
        ## Reverse
        if (k == p.B3G_DOWN_ARROW and (v & p.KEY_IS_DOWN)):
            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel_max_reverse,force = maxForce)
            
            p.stepSimulation()

        if (k == p.B3G_DOWN_ARROW and (v & p.KEY_WAS_RELEASED)):
            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel_stop,force = maxForce)
            
            p.stepSimulation()

        ## Right Turn
        if (k == p.B3G_RIGHT_ARROW and (v & p.KEY_IS_DOWN)):
            p.setJointMotorControl2(car, 2, p.VELOCITY_CONTROL,targetVelocity = targetVel_max,force = maxForce)
            p.setJointMotorControl2(car, 3, p.VELOCITY_CONTROL,targetVelocity = target_diff_drive,force = maxForce)
            p.setJointMotorControl2(car, 4, p.VELOCITY_CONTROL,targetVelocity = targetVel_max,force = maxForce)
            p.setJointMotorControl2(car, 5, p.VELOCITY_CONTROL,targetVelocity = target_diff_drive,force = maxForce)
            
            p.stepSimulation()

        if (k == p.B3G_RIGHT_ARROW and (v & p.KEY_WAS_RELEASED)):
            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel_stop,force = maxForce)
            
            p.stepSimulation()

        ## Left Turn
        if (k == p.B3G_LEFT_ARROW and (v & p.KEY_IS_DOWN)):
            p.setJointMotorControl2(car, 2, p.VELOCITY_CONTROL,targetVelocity = target_diff_drive,force = maxForce)
            p.setJointMotorControl2(car, 3, p.VELOCITY_CONTROL,targetVelocity = targetVel_max,force = maxForce)
            p.setJointMotorControl2(car, 4, p.VELOCITY_CONTROL,targetVelocity = target_diff_drive,force = maxForce)
            p.setJointMotorControl2(car, 5, p.VELOCITY_CONTROL,targetVelocity = targetVel_max,force = maxForce)
            
            p.stepSimulation()

        if (k == p.B3G_LEFT_ARROW and (v & p.KEY_WAS_RELEASED)):

            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel_stop,force = maxForce)
            
            p.stepSimulation()

        ## On Spot Rotation
        if (k == ord('r') and (v & p.KEY_IS_DOWN)):
            p.setJointMotorControl2(car, 2, p.VELOCITY_CONTROL,targetVelocity = targetVel_max,force = maxForce)
            p.setJointMotorControl2(car, 3, p.VELOCITY_CONTROL,targetVelocity = targetVel_max_reverse,force = maxForce)
            p.setJointMotorControl2(car, 4, p.VELOCITY_CONTROL,targetVelocity = targetVel_max,force = maxForce)
            p.setJointMotorControl2(car, 5, p.VELOCITY_CONTROL,targetVelocity = targetVel_max_reverse,force = maxForce)
            
            p.stepSimulation()

        if (k == ord('r') and (v & p.KEY_WAS_RELEASED)):
            for joint in range(2, 6):
                p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel_stop,force = maxForce)
            
            p.stepSimulation()

p.getContactPoints(car)
p.disconnect()