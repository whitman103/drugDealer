#include <vector>
#include <tuple>

using namespace std;

class Agent{
	public:
	tuple<double,double> xyPosition;
	int currentState;
	tuple<double,double> currentTarget;
	template <typename T> void setTarget(vector<T>,int);
	
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

