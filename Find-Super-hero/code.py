# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
print(data)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data.Gender.value_counts()
plt.hist(gender_count)



# --------------
#Code starts here
alignment=data.Alignment.value_counts()
plt.pie(alignment)


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
sc_covariance=np.cov(sc_df.Strength,sc_df.Combat)[0,1]
print(sc_covariance)
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
denominator=sc_strength*sc_combat
sc_pearson=sc_covariance/denominator
print(sc_pearson)
ic_df=data[['Intelligence','Combat']]
ic_covariance=np.cov(ic_df.Intelligence,ic_df.Combat)[0,1]
ic_intelligence=ic_df.Intelligence.std()
ic_combat=ic_df.Combat.std()
den=ic_combat*ic_intelligence
ic_pearson=ic_covariance/den
print(ic_pearson)


# --------------
#Code starts here
total_high=data.Total.quantile(0.99)
print(total_high)
super_best=data[data['Total']>total_high]
#print(super_best)
super_best_names=[]
super_best_names=super_best[['Name']].values.tolist()
print(super_best_names)


# --------------
#Code starts here
#ax_1=plt.subplot()
fig, (ax_1, ax_2, ax_3) = plt.subplots(3, sharex=True, sharey=True)
ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])


