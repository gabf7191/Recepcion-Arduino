const int pinLED = 24;
const int Lock = 11;
const int Motor = 12;
int x = 0; 
void setup() 
{
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
   pinMode(Lock, OUTPUT);
   pinMode(Motor, OUTPUT);   
}
 
void loop()
{
   if (x == 0)
   {
    Serial.println("<Arduino is ready>");
    x = 1;
    Serial.println(x);
   }
   if (Serial.available()>0) 
   {
      char option = Serial.read();
      if (option >= '1' && option <= '9')
      {
         option -= '0';
         for (int i = 0;i<option;i++) 
         {
            
            digitalWrite(Lock, HIGH);
            digitalWrite(Motor, LOW);
            delay(100);
            digitalWrite(Motor, HIGH);
            digitalWrite(Lock, LOW);
            delay(200);
            x=0;
         }
      }
   }
}
