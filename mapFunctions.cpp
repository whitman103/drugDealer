#include <string>
#include <vector>
#include <fstream>

#include "MapFunctions.h"
using namespace std;

void loadMap(string inFile, vector<vector<int> >& mapOut){
    ifstream inMap(inFile+".txt");
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




}