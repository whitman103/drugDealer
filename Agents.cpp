#include <iostream>
#include <vector>

using namespace std;

#include "Agents.h"


void Agent::walkToNextPoint(vector<tuple<int,int> > listOfWalkingVectors, vector<vector<int> >& streepMap){
	if(xyPosition!=currentWalkingTarget&&xyPosition!=finalTarget){
	}
	else{
		if(xyPosition==finalTarget){
			cout<<"Arrived"<<endl;
		}
		if(xyPosition==currentWalkingTarget){
			auto[xCur,yCur]=xyPosition;
			auto[xTar,yTar]=finalTarget;
			int xDiff(xTar-xCur);
			int yDiff(yTar-yCur);

		}
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

User::~User(){
}

