import nltk
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

# Read and format the training data
train = [("he shoots his pistol", "pos"),
("thunder strikes", "pos"),
("he draws his sword", "pos"),
("you hear an eagle overhead", "pos"),
("the sound of dripping water", "pos"),
("you hear a crashing sound", "pos"),
("you hear nothing","neg"),
("overhwelming silence engulfs you", "pos"),
("i feel very good about these beers.", "neg"),
("this is my best work.", "neg"),
("what an awesome view", "neg"),
("i do not like this restaurant", "neg"),
("i am tired of this stuff.", "neg"),
("I can't deal with this", "neg"),
("he is my sworn enemy!", "neg"),
("my boss is horrible.", "neg"),
("hello", "neg"),
("coke", "neg"),
("bells ringing", "pos"),
("you hear birds chirping", "pos"),
("i ate a cheese burger", "neg"),
("china", "neg"),
("you smell the damp dungeon", "neg"),
("donald trump", "neg"),
("i am happy", "neg"),
("i am sad", "neg"),
("i am angry", "neg"),
("the sound of fighting can be heard", "pos"),
("the sound of insects engulfs your ears", "pos"),
("the sound of silence", "neg")]


AI = NaiveBayesClassifier(train)
f = open("output.txt","r")
activation =0
while(1):
	
	text=f.readline()
	
	if AI.classify(text)=="pos":
		activation=activation+1
		if activation==20:
			with open("reader.txt", "a") as g:
				print(text, file=g)
				g.write("\n")
				activation=0
		
		