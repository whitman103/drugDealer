#include <vector>
#include <tuple>

using namespace std;

class Agent{
	public:
	tuple<int,int> xyPosition;
	int currentState;
	tuple<int,int> finalTarget;
	tuple<int,int> currentWalkingTarget;
	template <typename T> void setTarget(vector<T>,int);
	void walkToNextPoint(vector<tuple<int,int> > listOfWalkingPoints,vector<vector<int> >& streetMap);
	
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

