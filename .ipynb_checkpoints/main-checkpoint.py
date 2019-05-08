import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#import datasets
data_train = pd.read_csv("train.csv")
data_test =  pd.read_csv("test.csv")


print("Training Dataset\n")
print(data_train.sample(10))

print("Testing Dataset\n")
print(data_test.sample(10))

#dimensions of the data
print ("The shape of the training dataset: "+ str(data_train.shape))
print (data_train.info())

# print ("The shape of the testing dataset:"+ str(data_test.shape))
# print (data_test.info())
print(data_train['Cabin'].head())

fig, ax = plt.subplots(figsize=(16,12),ncols=2)
ax1 = sb.boxplot(x="Embarked", y="Fare", hue="Pclass", data=data_train, ax=ax[0]);
ax2 = sb.boxplot(x="Embarked", y="Fare", hue="Pclass", data=data_test, ax=ax[1]);
ax1.set_title("Training Set", fontsize=18)
ax2.set_title('Test Set',  fontsize=18)
plt.show()