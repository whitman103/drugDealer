# A work in progress C++ agent based model, attempting to model the three-pronged interaction between drug dealers, a user population, and an enforcing population.
The main idea of this model is to intake a map of a real section of a city, currently a set of blocks in downtown Columbus, Ohio, and simulate the interactions amongst a group of drug dealers, drug users/seekers, and the enforcing body. The goal of the model is to understand how physical setup of a city can influence the successful control of a drug dealing enterprise, investigate the spatial effects of the environment, such as public transportation, sprawl, and roadways on drug policy, and other goals which benefit from an explicitly spatial and individual based approach to modeling.
## Model is written in C++, image analysis performed in Python, map generated in qGIS, data from the City of Columbus.
Example of Street corner identification performed in program using OpenCV2 in Python.
[Street Image](https://github.com/whitman103/drugDealer/blob/master/nodeId.PNG)

Basic GUI is being built to show simulation in real-time, and possibly allow interactions.