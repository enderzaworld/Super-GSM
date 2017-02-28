/*
  SIM800 Test Send Sketch for Arduino
  
  Initializes GSM Module and sends an SMS to recipient

  * for uSD slot AT commands please see the 
    SIM800 Dev kit Manual.
  
  The circuit:
  *Arduino pin 0 (RX) - GSM Module (TX)
  *Arduino pin 1 (TX) - GSM Module (RX)
  
  Created 2010
  by Meann Zabanal
  Modified 
  by John for GSM Shield testing
*/

char Rx_data[50];
unsigned char Rx_index = 0;
int i = 0;
char msg[160];
byte numMsg[1000]= "";
int sig;

void setup() {
  Serial.begin(38400);
  Serial.println("Start");
  
  initGSM();
  Serial.println("Success");
  Serial.println("Begin");
  //Serial.println("222_-_bal");//test
  //send_msg("Type your number here", "Text Message");
}

void loop() {
  	if (Serial.available()) {
       numMsg[0]= Serial.read();
       int i=0;
     for(i=1;Serial.available();i++){
  		  numMsg[i]= Serial.read();
  		}
      char string1[i];
       
      for(int z=0;z<i;z++){
        string1[z]=numMsg[z];
      }
      string1[i] = '\0';
      String string="";
      for(int x=0;x<i;x++){
        string+=string1[x];
      }
      string+= '\0';
      
      String substrings[2] = {"",""};
      int indexof = string.indexOf("_-_");
      if(indexof>0){
        substrings [0]= string.substring(0, indexof);//number
        substrings [1]= string.substring((indexof+3) , string.length());//msg
        int numlen = substrings[0].length();
        int msglen = substrings[1].length();
        char char_number[numlen+1];
        char char_msg[msglen+1];
        int w=0;
        for(w=0;w<numlen;w++){
          char_number[w]=substrings[0].charAt(w);
        }
        char_number[w] = '\0';
        
        int y=0;
        for(y=0;y<msglen;y++){
          char_msg[y]=substrings[1].charAt(y);
        }
        char_msg[y] = '\0';
//        Serial.println(char_number);//test
//        Serial.println(char_msg);//test
//        Serial.println(substrings[0]);//test
//        Serial.println(substrings[1]);//test
//        Serial.println(numlen);//test
//        Serial.println(indexof);//test
    		send_msg(char_number, char_msg);
      }else{//  222_-_rawr 09233333333
        //Serial.println(string);
      }
  //		Serial.println(string);//test
  	}
  	delay(500);
}

void send_msg(char *number, char *msg)
{
  char at_cmgs_cmd[30] = {'\0'};
  char msg1[160] = {'\0'};
  char ctl_z = 0x1A;

  sprintf(msg1, "%s%c", msg, ctl_z);
  sprintf(at_cmgs_cmd, "AT+CMGS=\"%s\"\r\n",number);
  
  sendGSM(at_cmgs_cmd);
  delay(100);
  delay(100);
  delay(100);
  sendGSM(msg1);
  delay(100);
}

void sendGSM(char *string){
  Serial.write(string);
  delay(90);
}

void clearString(char *strArray) {
  int j;
  for (j = 100; j > 0; j--)
    strArray[j] = 0x00;
}

void send_cmd(char const *at_cmd, char clr){
  char *stat = '\0';
  while(!stat){
    sendGSM(at_cmd);
    delay(90);
    readSerialString(Rx_data);
    
    stat = strstr(Rx_data, "OK");
  }
  if (clr){
    clearString(Rx_data);
    delay(200);
    stat = '\0';
  }
}

void initGSM(){
  
  //Serial.println("start");
  //send_cmd("AT\r\n",1);//Turn on GSM Module
  //Serial.println("On");

//  send_cmd("ATE0\r\n",1); // Turn off automatic echo of the GSM Module	
	
  send_cmd("AT+CMGF=1\r\n",1);			// Set message format to text mode
  //Sucess
  
  //Serial.println("Success");
	
  delay(1000);
  delay(1000);
  delay(1000);
}

void readSerialString (char *strArray) {
  
  if(!Serial.available()) {
    return;
  }
  
  while(Serial.available()) {
    strArray[i] = Serial.read();
    i++;
  }
}


