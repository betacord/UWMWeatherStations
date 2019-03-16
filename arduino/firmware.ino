#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <DHT11.h>
#include <stdlib.h>

const int TEMP_SENSOR_ANALOG = 0;
const int HUMIDITY_SENSOR_ANALOG = 1;
const String NETWORK_NAME = "vnet-97920C";
const String NETWORK_PASSWORD = "niePodamTuHaslaXD";

void setup() {
  
  Serial.begin(115200);
  WiFi.begin(NETWORK_NAME, NETWORK_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.println("Waiting for connection");
  }
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {
    StaticJsonBuffer<300> JSONbuffer;
    JsonObject& JSONencoder = JSONbuffer.createObject();
    
    char buffer0[10];
	  char buffer1[10];
    
    float Btemp, Bhumi;
	  dht11.read(Bhumi, Btemp);

    JSONencoder["temp"] = dtostrf(Btemp, 4, 1, buffer);
    JSONencoder["hum"] = dtostrf(Bhumi, 4, 1, buffer1);

    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    Serial.println(JSONmessageBuffer);

    HTTPClient http;

    http.begin("http://192.168.0.15:8000/api/readings/");
    http.addHeader("Content-Type", "application/json");
    http.addHeader("Authorization", "Token 0020dfbab4bc045828ff2eb77d9ff8c035930397");

    int httpCode = http.POST(JSONmessageBuffer);
    String payload = http.getString();

    Serial.println(httpCode);
    Serial.println(payload);

    http.end();
  } else {
    
    Serial.println("Error in WiFi connection");
  }
  
  delay(300000);
}
