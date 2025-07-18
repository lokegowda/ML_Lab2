import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('glass.csv')
X = df.drop('Type', axis=1)
y = df['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model_eu = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
model_eu.fit(X_train, y_train)
acc_eu = accuracy_score(y_test, model_eu.predict(X_test))


model_man = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
model_man.fit(X_train, y_train)
acc_man = accuracy_score(y_test, model_man.predict(X_test))

print("Euclidean Accuracy:", acc_eu)
print("Manhattan Accuracy:", acc_man)
