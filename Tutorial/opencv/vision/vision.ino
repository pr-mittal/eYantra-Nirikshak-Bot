#include<SoftwareSerial.h>
#define Rx 0
#define Tx 1
#define RM_PWM 5
#define LM_PWM 10
#define RM1 7
#define RM2 6
#define LM1 9
#define LM2 8
#define RED 12
#define GREEN 13
char a='S';
SoftwareSerial mySerial(Rx,Tx);
void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(GREEN,OUTPUT);
  pinMode(RM_PWM,OUTPUT);
  pinMode(LM_PWM,OUTPUT);
  pinMode(RM1,OUTPUT);
  pinMode(RM2,OUTPUT);
  pinMode(LM1,OUTPUT);
  pinMode(LM2,OUTPUT);
  pinMode(RED,OUTPUT);
  
  
  digitalWrite(RM1,LOW);
  digitalWrite(LM1,LOW);
  digitalWrite(RM2,LOW);
  digitalWrite(LM2,LOW);
  analogWrite(RM_PWM,60);
  analogWrite(LM_PWM,30);
}
void forward(){ 
    digitalWrite(RM1,HIGH);
    digitalWrite(LM1,HIGH);
    digitalWrite(RM2,LOW);
    digitalWrite(LM2,LOW);
    
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
}
void right(){
      digitalWrite(LM1,LOW);
    digitalWrite(RM1,HIGH);
    digitalWrite(LM2,LOW);
    digitalWrite(RM2,LOW);
    
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
}
void left(){
    digitalWrite(LM1,HIGH);
    digitalWrite(RM1,LOW);
    digitalWrite(LM2,LOW);
    digitalWrite(RM2,LOW);
    
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
}
void backward(){
    digitalWrite(RM1,LOW);
    digitalWrite(LM1,LOW);
    digitalWrite(RM2,HIGH);
    digitalWrite(LM2,HIGH);
    
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
}
void pstop(){
    digitalWrite(RM1,LOW);
    digitalWrite(LM1,LOW);
    digitalWrite(RM2,LOW);
    digitalWrite(LM2,LOW);
}
void loop() {
  if(mySerial.available()){
    a=mySerial.read();}
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
  if(a=='X'){
    digitalWrite(RED,HIGH);
  }
  else if(a=='Z'){
    
    digitalWrite(GREEN,HIGH);
    
  }
  
  else if(a=='F')
  {  
    forward();
  }
  else if(a=='R') 
  { 
    right();
  }
  else if(a=='L')
  { 
    left();
  }
  else if (a=='B')
  {
    backward();
  }
  else{
    a=='S';
    pstop();
  }
  
}
