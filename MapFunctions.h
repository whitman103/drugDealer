#ifndef MapFunctionsH
#define MapFunctionsH

#include <iostream>
#include <vector>
#include <string>

using namespace std;
void loadMap(string inFile, vector<vector<int> >& outMap);
vector<tuple<int,int> > identifyWalkingPoints(vector<vector<int> >& streepMap);
vector<vector<tuple<int,int> > > identifyWalkingVectors(vector<tuple<int,int> >& walkingPoints);

#endif