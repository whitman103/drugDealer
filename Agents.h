#include <vector>
#include <tuple>

#include "MapFunctions.h"

using namespace std;

class Agent{
	public:
	Agent();
	Agent(tuple<double,double> initialSpot);
	tuple<double,double> xyPosition;
	int currentState;
	int nodeTarget;
	tuple<double,double> posTarget;
	template <typename T> void setTarget(vector<T>,int);
	int walk(Node* inTarget);
	double stepSize;
	
	private:
};

class Dealer: public Agent{
	public:
	void updatePosition();
	int favoredTarget;
	
	
	private:
};


class User: public Agent{
	public:
	User(int test);
	User(tuple<double,double>);
	~User();
	void updatePosition();
	int favoredTarget;
	
	private:
};


class Enforcer: public Agent{
	public:
	Enforcer(int dealer);
	~Enforcer();
	void updatePosition();
	int favoredDealer;
	
	private:
};


template<typename T> void Agent::setTarget(vector<T> inVector, int targetIndex){
	cout<<inVector[targetIndex].favoredTarget<<endl;
}

