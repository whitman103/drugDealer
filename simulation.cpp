#include <iostream>
#include <vector>
#include <fstream>
#include <string>

#include "Agents.h"
#include "MapFunctions.h"

using namespace std;

int main(){

	vector<vector<int> > streetMap;
	loadMap("streetMatrix",streetMap);

	vector<tuple<int,int> > streetCorners=identifyWalkingPoints(streetMap);

	vector<vector<tuple<int,int> > > walkingDirections=identifyWalkingVectors(streetCorners);

	ofstream walkingLines("testLines.txt");
	for(int i=0;i<(int)walkingDirections.size();i++){
		for(int j=0;j<(int)walkingDirections[i].size();j++){
			walkingLines<<get<0>(streetCorners[i])<<" "<<get<1>(streetCorners[i])<<endl;
			walkingLines<<get<0>(walkingDirections[i][j])<<" "<<get<1>(walkingDirections[i][j])<<endl<<endl;
		}
		walkingLines<<endl;
	}
	walkingLines.close();
	

	return 0;
}