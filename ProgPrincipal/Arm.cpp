#include "Arm.h"


Arm::Arm(){

}

void Arm::SetArm(){

  SetupRobot.SetElevator();
  SetupRobot.SetPomp();
  
}

void Arm::InitArm(){
  ElevatorRobot.LedON();
  delay(500);
  ElevatorRobot.LedOFF();
  SetArm();
  delay(500);
  ElevatorRobot.InitialPosition();
  Parking();

}

void Arm::Parking(){
  ElevatorRobot.Transport();
  ForeArmAction.InitDynamixel();
}

void Arm::Transport(){
    ElevatorRobot.Transport();
    delay(500);
    ForeArmAction.Transport();
    
}

void Arm::GetGobelet(int coordo, int couleur){
    ElevatorRobot.GetGobelet();
    delay(500);
    ForeArmAction.MoveAndWait(coordo);

    
}
