import pandas as pd
import matplotlib.pyplot as plt

white = pd.read_csv("c:\git\playground\Keras_tutorial\winequality-white.csv", sep=';')
red=pd.read_csv("c:\git\playground\Keras_tutorial\winequality-red.csv", sep=';')

#fig, ax = plt.subplots(1, 2)

#ax[0].hist(red.alcohol, 10, facecolor='red', alpha=0.5, label="Red wine")
#ax[1].hist(white.alcohol, 10, facecolor='white', ec="black",lw=0.5, alpha=0.5, label="White wine")

#fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)

#ax[0].set_ylim([0, 1000])
#ax[0].set_xlabel("Alcohol in % Vol")
#ax[0].set_ylabel("Frequency")
#ax[1].set_xlabel("Alcohol in % Vol")
#ax[1].set_ylabel("Frequency")
#ax[0].legend(loc='best')
#ax[1].legend(loc='best')
#fig.suptitle("Distribution of alcohol in % vol")

#plt.show()


fig, ax = plt.subplots(1, 2, figsize=(8, 4))

ax[0].scatter(red['quality'], red["sulphates"], color="red")
ax[1].scatter(white['quality'], white['sulphates'], color="white", edgecolors="black", lw=0.5)

ax[0].set_title("Red Wine")
ax[1].set_title("White Wine")
ax[0].set_xlabel("Quality")
ax[1].set_xlabel("Quality")
ax[0].set_ylabel("Sulphates")
ax[1].set_ylabel("Sulphates")
ax[0].set_xlim([0,10])
ax[1].set_xlim([0,10])
ax[0].set_ylim([0,2.5])
ax[1].set_ylim([0,2.5])
fig.subplots_adjust(wspace=0.5)
fig.suptitle("Wine Quality by Amount of Sulphates")

plt.show()