import numpy as np
import sys

from numpy.lib.shape_base import tile

def createDataSet():
    feature = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A", "A", "B", "B"]
    
    return feature, labels

# implement KNN classifier the same way described in the textbook
def KNNClassifier0(inX, dataSet: np.ndarray, labels, k):
    dataSetSize = dataSet.shape[0]
    # calculate the distance between samples
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5
    sortedDistIndices = distance.argsort()
    classCount = {}
    # select the k-nearest samples
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key = lambda x: x[1], reverse=True)
    return sortedClassCount[0][0]

def file2Matrix(filename):
    fr = open(filename)
    arrayOflines = fr.readlines()
    numberOfLines = len(arrayOflines)
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOflines:
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index, :] = listFromLine[:3]
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat, classLabelVector

def normalize(data: np.array):
    rows = data.shape[0]
    minimum = data.min(axis=0)
    dataRange = data.max(axis=0) - minimum
    
    minMat = tile(minimum, (rows, 1))
    rangeMat = tile(dataRange, (rows, 1))
    
    normData = (data - minMat) / rangeMat
    
    return normData, minimum, dataRange
 
def datingTest():
    testSize = 0.1
    feature, labels = file2Matrix(sys.path[0] + "\datingTestSet.txt")
    normFeature, minimum, dataRange = normalize(feature)
    numTest = int(testSize * normFeature.shape[0])
    errorCount = 0
    for i in range(numTest):
        result = KNNClassifier0(normFeature[i, :], normFeature[numTest:, :], labels[numTest:], 3)
        print("classification result {}, real answer is {}".format(result, labels[i]))
        if result != labels[i]:
            errorCount += 1
    print("total error rate is {}".format(errorCount / numTest))
    
if __name__ == "__main__":
    
    # feature, labels = createDataSet()
    # pred = KNNClassifier0([0, 0], feature, labels, 3)
    
    datingFeature, datingLabel = file2Matrix(sys.path[0] + "\datingTestSet2.txt")
    datingTest()
    
    
    