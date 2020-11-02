#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#include "Agents.h"
#include "MapFunctions.h"

Agent::Agent(){
	stepSize=3;
}

Agent::Agent(tuple<double,double> initialSpot){
	stepSize=3;
	xyPosition=initialSpot;
}

int Agent::walk(Node* inTarget){
	if(r2Distance(get<0>(xyPosition),get<1>(xyPosition),get<0>((*inTarget).nodePos),get<1>((*inTarget).nodePos))<stepSize){
		return 1;
	}
	else{
		double xDiff(get<0>((*inTarget).nodePos)-get<0>(xyPosition));
		double yDiff(get<1>((*inTarget).nodePos)-get<1>(xyPosition));
		double angle=atan2(yDiff,xDiff);
		get<0>(xyPosition)+=stepSize*cos(angle);
		get<1>(xyPosition)+=stepSize*sin(angle);
		return 0;
	}
}

Enforcer::Enforcer(int dealer){
	favoredDealer=4;
}

Enforcer::~Enforcer(){
}

User::User(int testIndex){
	favoredTarget=testIndex;
}
User::User(tuple<double,double> input){
	stepSize=3;
	xyPosition=input;
}

User::~User(){
}

