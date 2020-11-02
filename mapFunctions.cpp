#include <string>
#include <vector>
#include <fstream>
#include <tuple>
#include <cmath>

#include "MapFunctions.h"
using namespace std;

void loadMap(string inFile, vector<vector<int> >& mapOut){
    ifstream inMap(inFile+".txt");
    if(!inMap.is_open()){
        cout<<"File not Open"<<endl;
    }
    int rows(0);
    inMap>>rows;
    int cols(0);
    inMap>>cols;

    vector<vector<int> > buildMat(rows, vector<int> (cols,0));

    for(int i=0;i<(int)buildMat.size();i++){
        for(int j=0;j<(int)buildMat[i].size();j++){
            inMap>>buildMat[i][j];
        }
    }

    inMap.close();

    mapOut=buildMat;
}

vector<Node> loadNodes(string nodePosFile, string edgeConnectionPath){
    ifstream inNode(nodePosFile+".txt");
    int inData(0);
    inNode>>inData;
    vector<Node> outVector(inData);
    for(int i=0;i<(int)outVector.size();i++){
        int yValue(0), xValue(0);
        inNode>>yValue;
        inNode>>xValue;
        outVector[i].nodePos=make_tuple(xValue,yValue);
    }
    inNode.close();
    inNode.open(edgeConnectionPath+".txt");
    for(int i=0;i<(int)outVector.size();i++){
        int numConnections(0);
        inNode>>numConnections;
        for(int j=0;j<numConnections;j++){
            inNode>>inData;
            outVector[i].connections.push_back(inData);
        }
    }
    inNode.close();

    return outVector;


}

double r2Distance(double x1,double y1,double x2,double y2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}