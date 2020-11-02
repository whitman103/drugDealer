#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <tuple>

#include "Agents.h"
#include "MapFunctions.h"

using namespace std;


int main(){

	vector<vector<int> > streetMap;
	loadMap("streetMatrix",streetMap);
	loadNodes("finalNodes","outNodeEdges");
	
	

	return 0;
}

