from sklearn import tree 
features = [[140, 1],[130, 1],[150, 0],[170, 0]] # 0 is bumpy and 1 is smooth as scikit learn uses integer value features
labels = [0, 0, 1, 1] # 0 for apple and 1 for orange
clf = tree.DecisionTreeClassifier() # Classifier is a box of rules
clf = clf.fit(features, labels)# fit is synonym for find patterns and data. Learning algorithm is the procedure that creates the rules. Fit is the training algorithm.
print (clf.predict([[160,0]]))
