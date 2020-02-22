from sklearn.datasets import load_iris
from sklearn import linear_model
# https://scikit-learn.org/stable/modules/cross_validation.html
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pylab as pl

iris = load_iris()
print("\n-=- load_iris() -=-\n")
print(iris)

classifier = linear_model.LogisticRegression(C=1, random_state=111)
print("\n-=- classifier -=-\n")
print(classifier)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.10, random_state=111)

print("\n-=- X_train -=-\n")
print(X_train)

print("\n-=- X_test -=-\n")
print(X_test)

print("\n-=- y_train -=-\n")
print(y_train)

print("\n-=- y_test -=-\n")
print(y_test)

classifier.fit(X_train, y_train)

pca = PCA(n_components=2).fit(X_train)
print("\n-=- pca -=-\n")
print(pca)

pca_2d = pca.transform(X_train)
print("\n-=- pca2d -=-\n")
print(pca_2d)

for i in range(0, pca_2d.shape[0]):
    if y_train[i] == 0:
        c1 = pl.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif y_train[i] == 1:
        c2 = pl.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif y_train[i] == 2:
        c3 = pl.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

print("\n-=- pl -=-\n")
print(pl)

pl.show()
