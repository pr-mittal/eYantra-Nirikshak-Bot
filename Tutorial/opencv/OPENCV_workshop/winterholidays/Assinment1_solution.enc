#include<SoftwareSerial.h>
#define Rx 10
#define Tx 11
#define RM_PWM 6
#define LM_PWM 5
#define RM1 7
#define RM2 8
#define LM1 3
#define LM2 4
char a='S';
SoftwareSerial mySerial(Rx,Tx);
void setup() {
  mySerial.begin(9600);
  pinMode(RM_PWM,OUTPUT);
  pinMode(LM_PWM,OUTPUT);
  pinMode(RM1,OUTPUT);
  pinMode(RM2,OUTPUT);
  pinMode(LM1,OUTPUT);
  pinMode(LM2,OUTPUT);

  
  digitalWrite(RM1,LOW);
  digitalWrite(LM1,LOW);
  digitalWrite(RM2,LOW);
  digitalWrite(LM2,LOW);
  analogWrite(RM_PWM,150);
  analogWrite(LM_PWM,150);
  while(!mySerial.available())
  {}
}
void loop() {
  if(mySerial.available()){
    a=mySerial.read();}
  if(a=='F')
  {  
     digitalWrite(LM1,HIGH);
     digitalWrite(RM1,HIGH);
  }
  else if(a=='R') 
  { 
    digitalWrite(LM1,HIGH);
  }
  else if(a=='L')
  { 
    digitalWrite(RM1,HIGH);
  }
  else if (a=='B')
  {
   digitalWrite(LM2,HIGH);
   digitalWrite(RM2,HIGH);
  }
  else{
    a=='S';
    digitalWrite(RM1,LOW);
    digitalWrite(LM1,LOW);
    digitalWrite(RM2,LOW);
    digitalWrite(LM2,LOW);
  }
  delay(100);
}
