def beforehappy():
  i01.startedGesture()
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("right", 43.0, 43.0, 43.0, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(22.0, 22.0)
  i01.moveHead(84,88)
  i01.moveArm("left",5,82,36,11)
  i01.moveArm("right",74,112,61,29)
  i01.moveHand("left",0,88,135,94,96,90)
  i01.moveHand("right",81,79,118,47,0,90)
  sleep(1)
  i01.finishedGesture()

