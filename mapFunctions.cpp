#include <string>
#include <vector>
#include <fstream>

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

    vector<vector<int> > buildMat(cols, vector<int> (rows,0));

    for(int i=0;i<(int)buildMat.size();i++){
        for(int j=0;j<(int)buildMat[i].size();j++){
            inMap>>buildMat[i][j];
        }
    }

    inMap.close();

    mapOut=buildMat;
}

vector<tuple<int,int> > identifyWalkingPoints(vector<vector<int> >& streetMap){
	vector<tuple<int,int> > outCorners;
	for(int i=1;i<(int)streetMap.size()-1;i++){
		for(int j=1;j<(int)streetMap[i].size()-1;j++){
			if(streetMap[i][j]==0){//check currentspot is in street
				int count(0);
				count+=(streetMap[i-1][j]+streetMap[i+1][j]+streetMap[i][j-1]+streetMap[i][j+1]);
				if(count==2){
					outCorners.push_back(make_tuple(i,j));
				}
			}
		}
	}
	return outCorners;
}

vector<vector<tuple<int,int> > > identifyWalkingVectors(vector<tuple<int,int> >& walkingPoint){
    int maxNumberOfConnections(3);
    vector<vector<tuple<int,int> > > outList;
    for(int i=0;i<(int)walkingPoint.size();i++){
        auto[curX,curY]=walkingPoint[i];
        vector<tuple<int,int> > testDistances(maxNumberOfConnections,make_tuple(20000,0));
        for(int j=0;j<(int)walkingPoint.size();j++){
            auto[toX,toY]=walkingPoint[j];
            int d1Amount(abs(toX-curX)+abs(toY-curY));
            bool inserted(false);
            for(int k=0;k<(int)testDistances.size();k++){
                if(d1Amount<get<0>(testDistances[k]) && !inserted){
                    testDistances[k]=make_tuple(d1Amount,j);
                    inserted=true;
                }
            }
        }
        outList.push_back(testDistances);
    }
    for(int i=0;i<(int)outList.size();i++){
        for(int j=0;j<(int)outList[i].size();j++){
            outList[i][j]=walkingPoint[get<1>(outList[i][j])];
        }
    }
    return outList;

}