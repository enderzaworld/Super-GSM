//***********************************************//
//	        GSM/GPRS CALLUP                  //
//	This sketch is used to test seeeduino    //
//  GPRS_Shield's callUp function.to make it     //
//  work, you should insert SIM card to          //
//  Seeeduino GPRS and replace the               //
//  phoneNumber,enjoy it!                        //
//                                               //
//	create on 2015/05/14, version: 1.0       //
//	by lawliet.zou(lawliet.zou@gmail.com)    //
//                                               //
//	This library was tested in               //
//	e-Gizmo SIM800,900D,900 modules/kits     //
//   Wiring Connection:                          //
//   SIM800/900 modules to UARTPORT/gizDuino MCUs//
//		RXD	-	TX(D3)           //
//		TXD	-	RX(D2)           //
//		GND	-	GND              //
//	by e-Gizmo Mechatronix Central           //
//          http://www.egizmo.com                //
//***********************************************//

//INCLUDE LIBRARIES
#include <GPRS_Shield_Arduino.h>
#include <SoftwareSerial.h>
#include <Wire.h>

//SERIAL PIN ASSIGNMENT, BAUDRATE, PHONE NUMBER
#define PIN_TX    2
#define PIN_RX    3
#define BAUDRATE  9600
#define PHONE_NUMBER  "+63***"

GPRS GSMTEST(PIN_TX,PIN_RX,BAUDRATE);//RX,TX,PWR,BAUDRATE

void setup() {
  Serial.begin(9600);
  while(!GSMTEST.init()) { //GSM INITIALIZATION
      delay(1000);
      Serial.print("INIT ERROR\r\n");
  }
  Serial.println("GSM INIT SUCCESS");
  Serial.println("START TO CALL...");
  GSMTEST.callUp(PHONE_NUMBER);
}

void loop() {
  //NOTHING TO DO
}
