from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
   return distance.euclidean(a,b)

class KNN():
    def fit(self,TrainingData,TrainingTarget):
        self.TrainingData=TrainingData
        self.TrainingTarget=TrainingTarget
        
    def predict(self,TestData):	#store closest  distance of k value
       predictions=[]
       for row in TestData:
           lebel=self.closets(row)
           predictions.append(lebel)
       return predictions
 
    def closets(self,row):
        bestdistance=euc(row,self.TrainingData[0])
        bestindex=0
        for i in range(1,len(self.TrainingData)):	#yamule k chi minimum value  milel and tyatl distance
             dist=euc(row,self.TrainingData[i])
             if dist<bestdistance:
                bestdistance=dist
                bestindex=i
        return self.TrainingTarget[bestindex]
    
def KNeighbor():
    border="-"*60

    iris=load_iris()
    
    data=iris.data
    target=iris.target
    
    print(border)
    print("Actual data set")
    print(border)
    
    for i in range (len(iris.target)):
        print("ID:%d Label %s,FeatureL:%s"%(i,iris.data[i],iris.target[i]))
    print("Size of Actual data set %d"%(i+1))

    data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.5)
    
    print(border)
    print("Train data sets")
    print(border)
    for i in range (len(data_train)):
        print("ID:%d Label %s,FeatureL:%s"%(i,data_train[i],target_train[i]))
    print("Size of Actual data set %d"%(i+1))
    
    print(border)
    print("Test data sets")
    print(border)
    for i in range (len(data_test)):
        print("ID:%d Label %s,FeatureL:%s"%(i,data_test[i],target_test[i]))
    print("Size of Actual data set %d"%(i+1))
    print(border)
    
    classifier=KNN()
    
    classifier.fit(data_train,target_train)
    
    predictions=classifier.predict(data_test)
    
    Accuracy=accuracy_score(target_test,predictions)

    return Accuracy        
     



  
def main():
  Accuracy=KNeighbor()
  print("Accurcy of classification algorithm with K Neighbor classifier is",Accuracy*100,"%")


if __name__=="__main__":
   main();
