import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv(r"C:\Users\TRISHA MAITHRI\Documents\Dataset\Dataset\titanic.csv")
age_survived=data[data['survived']==1]['age']
age_not_survived=data[data['survived']==0]['age']
plt.hist(age_survived,color='blue',alpha=0.2,label='survived')
plt.hist(age_not_survived,color='black',alpha=1,label='not survived')
plt.xlabel('age')
plt.ylabel('frequency')
plt.legend()
plt.show()