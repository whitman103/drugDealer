#ifndef MapFunctionsH
#define MapFunctionsH

#include <iostream>
#include <vector>
#include <string>
#include <tuple>

using namespace std;

typedef struct {
    tuple<int,int> nodePos;
    vector<int> connections;
} Node;

using namespace std;
void loadMap(string inFile, vector<vector<int> >& outMap);
vector<Node> loadNodes(string inFile,string edgeConnectionPath);
double r2Distance(double x1, double y1, double x2, double y2);

#endif