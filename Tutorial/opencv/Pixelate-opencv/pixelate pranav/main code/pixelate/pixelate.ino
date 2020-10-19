#include<SoftwareSerial.h>
#include<Servo.h>
#include<Time.h>
#define Rx 0
#define Tx 1 
#define RM_PWM 11
#define LM_PWM 3
#define RM1 7
#define RM2 8
#define LM1 4
#define LM2 5
#define RED 9
#define GREEN 13
#define BLUE 12
#define servo1 10
char a='S';
Servo myservo1;
SoftwareSerial mySerial(Rx,Tx);
void setup() {
  //mySerial.begin(9600);
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
  analogWrite(RM_PWM,65);
  analogWrite(LM_PWM,70);
  myservo1.attach(servo1);
}
void forward(){ 
  
    digitalWrite(RM1,LOW);
    digitalWrite(LM1,HIGH);
    digitalWrite(RM2,HIGH);
    digitalWrite(LM2,LOW);
    
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
  digitalWrite(BLUE,LOW);
  analogWrite(RM_PWM,75);
  analogWrite(LM_PWM,75);
}
void left(){
  
      digitalWrite(LM1,LOW);
    digitalWrite(RM1,LOW);
    digitalWrite(LM2,HIGH);
    digitalWrite(RM2,HIGH);
    analogWrite(RM_PWM,75);
    analogWrite(LM_PWM,80);
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
  digitalWrite(BLUE,LOW);
  
}
void right(){
 
    digitalWrite(LM1,HIGH);
    digitalWrite(RM1,HIGH);
    digitalWrite(LM2,LOW);
    digitalWrite(RM2,LOW);
     analogWrite(RM_PWM,75);
     analogWrite(LM_PWM,80);
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
  digitalWrite(BLUE,LOW);
}
void backward(){
 
    digitalWrite(RM1,HIGH);
    digitalWrite(LM1,LOW);
    digitalWrite(RM2,LOW);
    digitalWrite(LM2,HIGH);
     analogWrite(RM_PWM,70);
     analogWrite(LM_PWM,75);
    
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
  digitalWrite(BLUE,LOW);
}
void pstop(){
    digitalWrite(RM1,LOW);
    digitalWrite(LM1,LOW);
    digitalWrite(RM2,LOW);
    digitalWrite(LM2,LOW);
    digitalWrite(RED,LOW);
    digitalWrite(GREEN,LOW);
    digitalWrite(BLUE,LOW);
}
void grab(){
  int i=0;
  
  while(i!=90)
  {myservo1.write(i);
    i=i+1;
    delay(10);
}
}
void lift(){
int i=0;
while(i!=50)
  {myservo1.write(90-i);
    i=i+1;
    delay(10);
  }
}

void loop() {
  
  if(Serial.available()){
    a=Serial.read();}
  if(a=='O'){
    digitalWrite(RED,HIGH);
    digitalWrite(BLUE,LOW);
  digitalWrite(GREEN,LOW);
  }
  else if(a=='P'){
    
    digitalWrite(GREEN,HIGH);
    digitalWrite(RED,LOW);
  digitalWrite(BLUE,LOW);
    
  }
  else if(a=='Q')
  {
    digitalWrite(BLUE,HIGH);
    digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);
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
  else if(a=='G'){
    grab();
  }
  else if (a=='A'){
  lift();
  }
  else if(a=='S'){
    a=='S';
    pstop();
  }
  
}
