import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sklearn
from sklearn import linear_model

def train_n_pred(x,y,pred):

	model1 = sklearn.linear_model.LinearRegression()
	x_fin = []
	y_fin = []
	pred_fin = []
	for i in range(len(x)):
		x_fin.append([x[i]])
		y_fin.append([y[i]])
	for i in range(len(pred)):
		pred_fin.append([pred[i]])
	del(x)
	del(y)
	del(pred)
	model1.fit(x_fin,y_fin)
	print ("Intercept is: "+str(model1.coef_))
	print ("Slope is: "+str(model1.intercept_))
	return model1.predict(pred_fin)[0]





def main():
	
	x = []
	y = []
	pred = []
	print("\t\t\tLINEAR REGRESSION WITH ONE VARIABLE\n")
	x = list(map(int,(input("Enter space separated input variable data: ").split(" "))))
	y = list( map (int,(input("Enter space separated output variable data: ").split(" ")) ) )
	pred = list( map (int,(input("Enter space separated data for prediction: ").split(" ")) ) )
	if len(x) != len(y):
		print("Lengths of input and output variables do not match")
	else:
		print("Predicted output for "+str(pred[0])+ " is: "+str(train_n_pred(x,y,pred)))
	

if __name__ == "__main__":
	main()
