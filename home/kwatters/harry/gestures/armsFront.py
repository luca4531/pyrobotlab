def armsFront():
  i01.startedGesture()
  i01.moveHead(90,90)
  i01.moveArm("left",13,115,100,50)
  i01.moveArm("right",13,115,100,50)
  i01.moveHand("left",50,24,54,50,82,0)
  i01.moveHand("right",50,24,54,50,82,180)
  i01.moveTorso(90,90,90)
  sleep(1)
  i01.finishedGesture()
