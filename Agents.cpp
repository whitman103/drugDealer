#include <iostream>
#include <vector>


#include "Agents.h"

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
