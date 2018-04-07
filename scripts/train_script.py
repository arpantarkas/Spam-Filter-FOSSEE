# Refer to the Notebook first, before bouncing on this script!!
# The detailed analysis is in the NoteBook, this script is just to train 
# on the final dataset with the best parameters obtained from analysis!



# Import All Libraries to be used

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from textblob import TextBlob
from sklearn.externals import joblib


def clean(data):

	data = re.sub(r"\n", " ", data)
	data = re.sub(r"<[^a].*?>", ' ', data)
	data = re.sub(r"&.*?;", ' ', data)
	data = re.sub(r"{.*?}", " ", data)
	data = re.sub(r"\\r", " ", data)
	data = re.sub(r"\\n", " ", data)
	data = re.sub(r"[0-9]+", " ", data)

	return data

class lemmatise(object):
	def __init__(self, message):
		self.message = message
		
	def process(message):
		#message = self.message
		message = message.lower()
		lemm = WordNetLemmatizer()

		words = TextBlob(message).words                       # Tokenization {Splitting into words}
		stop_words = stopwords.words('english')               # Importing List of Stop Words

		message_new = [word for word in words if word not in stop_words]
		message_new = [lemm.lemmatize(word) for word in message_new]

		return message_new

if __name__ == '__main__':
	posts = pd.read_csv('/data/Data.csv', encoding='latin-1')
	posts.drop( posts[pd.isnull( posts['Label'])].index, inplace=True)
	posts['Data'] = posts.Data.apply(clean)

	# Best Parameters obtained from analysis
	final_pipeline = Pipeline([
		('tfidf', TfidfVectorizer(analyzer=lemmatise.process, stop_words='english')),
		('svc', SVC(kernel='linear', gamma=0.05)),
	])

	predictor = final_pipeline.fit(posts['Data'], posts['Label'])

	joblib.dump(predictor, '/model/Trained-Model.pkl')
		

