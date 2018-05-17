#Setting up data structures in json files

import os
import json

#TODO: Seperate data structures into different files and folders

def initialize_data():
	data={}
	data['commentID']=[]
	data['submissionID']=[]
	data['subredditID']=[]
	data['commentBody']=[]
	data['submissionMeta']=[]
	data['subredditMeta']=[]
	with open('data.json', 'w+') as file:
		json.dump(data, file)
	file.close()

if not os.path.isfile('data.json'):
	initialize_data()	
