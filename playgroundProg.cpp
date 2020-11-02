#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <tuple>
#include <random>

#include "Agents.h"
#include "MapFunctions.h"

using namespace std;


int main(){

	mt19937 generator;
	generator.seed(0);

	vector<vector<int> > streetMap;
	loadMap("streetMatrix",streetMap);
	vector<Node> nodeList=loadNodes("finalNodes","outNodeEdges");
	
	double time(0);
	double maxTime(20);
	double timeIncrement(0.05);

	vector<User> userList(200,User(make_tuple(2.,2.)));
	
	for(int i=0;i<(int)userList.size();i++){
		userList[i].nodeTarget=generator()%nodeList.size();
		userList[i].xyPosition=make_tuple(generator()&800,generator()%800);
	}

	ofstream printProgress;
	int printCount(0);

	do{
		printProgress.open("imageBin//"+to_string(printCount)+".txt");
		printCount+=1;
		for(int i=0;i<(int)userList.size();i++){
			userList[i].walk(&nodeList[userList[i].nodeTarget]);
			auto[x,y]=userList[i].xyPosition;
			printProgress<<x<<" "<<y<<endl;
		}
		printProgress.close();
		

		time+=timeIncrement;
	}while(time<maxTime);

	

	return 0;
}

