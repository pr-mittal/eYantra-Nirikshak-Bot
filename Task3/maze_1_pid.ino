#include <QTRSensors.h>
QTRSensors qtr;
const uint8_t SensorCount = 6;
uint16_t sensorValues[SensorCount];
/////////////////////////////////////////////////////////////////////////////////////////////
#define rightMaxSpeed 120
#define leftMaxSpeed 120
#define rightBaseSpeed 80
#define leftBaseSpeed 80
#define turnSpeed 65
float Kp = 0.014;
float Kd = 0.140;
int blk = 600; //Black Line threshold(sensor value)
int wht = 400;
int KpSent = 0, KdSent = 0;
#define r1 4
#define r2 5
#define l1 6
#define l2 7
#define rt 3
#define lt 8
int error, prop, derv, motorSpeed, leftMotorSpeed, rightMotorSpeed, lastError = 0;
int switchOfBot = 1;

void setup()
{ qtr.setTypeAnalog();
  qtr.setSensorPins((const uint8_t[]){A0, A1, A2, A3, A4, A5}, SensorCount);
  qtr.setEmitterPin(2);
  delay(500);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH); 
  for (uint16_t i = 0; i < 400; i++){qtr.calibrate();}
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(9600);
  for (uint8_t i = 0; i < SensorCount; i++)
  { Serial.print(qtr.calibrationOn.minimum[i]);Serial.print(' ');
  }Serial.println();
  
  for (uint8_t i = 0; i < SensorCount; i++)
  { Serial.print(qtr.calibrationOn.maximum[i]);
    Serial.print(' ');}
  Serial.println();
  Serial.println();
  delay(1000);
}

void loop()
{ sensor_read();
  pid();
}
void pid(){
  uint16_t position = qtr.readLineBlack(sensorValues);
  error = position - 2500;
  prop = Kp * error;
  derv = Kd * (error - lastError);
  lastError = error;
  motorSpeed = prop + derv;
  rightMotorSpeed = rightBaseSpeed - motorSpeed;
  leftMotorSpeed = leftBaseSpeed + motorSpeed;
  if (rightMotorSpeed > rightMaxSpeed ) rightMotorSpeed = rightMaxSpeed; // prevent the motor from going beyond max speed
  if (leftMotorSpeed > leftMaxSpeed ) leftMotorSpeed = leftMaxSpeed; // prevent the motor from going beyond max speed
  if (rightMotorSpeed < 0) rightMotorSpeed = 0; // keep the motor speed positive
  if (leftMotorSpeed < 0) leftMotorSpeed = 0; // keep the motor speed positive
  digitalWrite(r1, HIGH); 
  digitalWrite(r2, LOW);
  digitalWrite(l1, HIGH); 
  digitalWrite(l2, LOW);
  analogWrite(rt, rightMotorSpeed);
  analogWrite(lt, leftMotorSpeed);}
void sensor_read(){
  uint16_t position = qtr.readLineBlack(sensorValues);
  for (uint8_t i = 0; i < SensorCount; i++){ Serial.print(sensorValues[i]);Serial.print('\t');}Serial.println(position);
  }
