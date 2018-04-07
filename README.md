All Code is Tested in Python3!


1. To View the Analysis :-
	
	1. Head off straight to "Spam Filter NoteBook.html" & you can see all the analysis.

	OR

	1. Run "sudo pip install -r requirements.txt" in terminal to Install all the required Libraries
	2. Run 'jupyter notebook' in terminal and Open "Spam Filter Notebook.ipynb" to see All the Analysis & Training of Model


** Run "sudo pip install -r requirements.txt" Mandatorily in order to get results from the below processes.


{Optional}

1. If You have a Test Dataset :-
	1. Copy Your Test Dataset to this folder.
	2. Run "python3 test_dataset.py" in terminal, and enter correctly.
	3. You can get the Report as Output.

I have also made a Flask API which will respond to requests when called from user. So, 

2. To Test Individual Messages :-
	1. Open terminal window & run "python3 api.py". This will trigger the API & enable it to listen to requests.
	2. Open another terminal window & run "python3 checker.py".
	3. Input your data.
	4. Result will be displayed.
	

NOTE :- 
1. The "Trained-Model.pkl" stores the Trained Model after obtaining best parameters from the Analysis.
2. Final script to train the model with best parameters obtained from analysis is 'train_script.py'.



