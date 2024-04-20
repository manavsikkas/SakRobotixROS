#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>

ros::NodeHandle nh;

sensor_msgs::Range range_msg;
ros::Publisher pub("Ultra",&range_msg);

int trig=7;
int echo=6;

long range_time;

void setup() {
  nh.initNode();
  nh.advertise(pub);

  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeated
    range_msg.range=getRange()*0.0343/2;
    pub.publish(&range_msg);
    delay(1000);

  nh.spinOnce();
}

int getRange(){
  long duration;
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  duration=pulseIn(echo,HIGH);
  return duration;
}
