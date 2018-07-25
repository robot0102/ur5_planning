#! /usr/bin/env python

# Import the module
from urdf_parser_py.urdf import URDF
from pykdl_utils.kdl_parser import kdl_tree_from_urdf_model
from pykdl_utils.kdl_kinematics import KDLKinematics

robot = URDF.from_xml_file("/data/ros/ur_ws/src/universal_robot/ur_description/urdf/ur5.urdf")

tree = kdl_tree_from_urdf_model(robot)
print tree.getNrOfSegments()

chain = tree.getChain("base_link", "ee_link")
print chain.getNrOfJoints()

# forwawrd kinematics
kdl_kin = KDLKinematics(robot, "base_link", "ee_link")
q = [0, 0, 1,0,1,0]
#q=[1.47,-2.17,-1.36,1.73,-1.68,1.56]
pose = kdl_kin.forward(q) # forward kinematics (returns homogeneous 4x4 matrix)
print pose

q_ik = kdl_kin.inverse(pose) # inverse kinematics
print "iverse\n",q_ik

if q_ik is not None:
    pose_sol = kdl_kin.forward(q_ik) # should equal pose
    print pose_sol

J = kdl_kin.jacobian(q)
print 'J:', J