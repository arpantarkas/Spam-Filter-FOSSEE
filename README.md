## Spam Filter for FOSSEE Forums, IIT Bombay

This is my Submission to the Screening Task of FOSSEE Web Development Fellowship, IIT Bombay, in which I was given a Dataset & I had to come up with an Algorithm to classify the FOSSEE Forum Posts as Spam/Not Spam.

* To View the Analysis :-
	
	1. Run ```$ sudo pip install -r requirements.txt``` to Install all the required Libraries
	2. Run ```$ jupyter notebook``` and Open "Spam Filter Notebook.ipynb" to see All the Analysis & Training of Model


* If You have a Test Dataset :-
	1. Copy Your Test Dataset to ```data```.
	2. Run ```$ python3 /scripts/test_dataset.py``` and enter details correctly.
	3. You can get the Report as Output.

***I have also made a Flask API which will respond to requests when called from user. So***, 

* To Test Individual Messages :-
	1. Run ```$ python3 /scripts/api.py```. This will trigger the API & enable it to listen to requests.
	2. Run ```$ python3 /scripts/checker.py```.
	3. Input your data.
	4. Result will be displayed.
	

* ```Trained-Model.pkl``` stores the Trained Model after obtaining best parameters from the Analysis.
* Final script to train the model with best parameters obtained from analysis is ```/scripts/train_script.py```



