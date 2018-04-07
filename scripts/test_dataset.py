# Import All Libraries to be used

import pandas as pd
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.externals import joblib
from train_script import lemmatise

if __name__ == '__main__':
	try:
		dataset = input("Enter name of Dataset in 'xyz.csv' format {Make Sure it is available in the same folder as this script} :- ")
		posts = pd.read_csv('/data/'+dataset, encoding='latin-1')
		
	except:
		print("\nFile Name Incorrect or File Not Found!!\nExiting...\n")
		exit(0)
		
	try:
		desc = input("Enter column name of Data Descriptions :- ")
		test_data = posts[desc][:]
	except:
		print("\nColumn Name error!!\nExiting.....")
		exit(0)
	try:
		labels = input("Enter column name of Labels :- ")
		test_label = posts[labels][:]
	except:
		print("\nColumn Name error!!\nExiting.....")
		exit(0)
	
	
				
	posts.drop( posts[pd.isnull( posts[labels])].index, inplace=True)			
	
	clf = joblib.load('/model/Trained-Model.pkl')			# Loading Model, Do not Change Here

	test_data = posts[desc][:]	
	test_label = posts[labels][:]	
	
	print("\nRunning........")
	predictions = clf.predict(test_data)
	print("Reports :- \n")
	print('Confusion Matrix :-\n{}\n'.format(confusion_matrix(test_label, predictions)))
	print('Classification Report :-\n{}'.format(classification_report(test_label,predictions)))
	print('Accuracy Score :- {}\n'.format(accuracy_score(test_label, predictions)))
	
	
