import matplotlib.pyplot as plt

#A list of the dancibility of the top 20 songs in the database
danceability = [0.8, 0.71, 0.51, 0.55, 0.65, 0.92, 0.67, 0.67, 0.85, 0.81,
                0.57, 0.78, 0.71, 0.51, 0.52, 0.64, 0.78, 0.44, 0.86, 0.63]

#A list of the streams of 20 different songs, corresponding with the danciblity list                
streams = [141000000, 134000000, 140000000, 801000000, 303000000, 184000000, 726000000, 58149378, 95217315, 554000000,
           506000000, 58255150, 1320000000, 388000000, 2510000000, 1160000000, 497000000, 30546883, 335000000, 363000000]

#Creating the scatter plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(danceability, streams, color='magenta', marker='D', linestyle = ':', edgecolors = 'black')

#Setting the labels and the title
ax.set_title("A graph to show the amount of streams against the dancibility of the song", fontsize =20)
ax.set_xlabel("Dancibility", fontsize = 12)
ax.set_ylabel("Streams", fontsize = 12)

#Adding grid lines
ax.xaxis.grid(True)
ax.yaxis.grid(True)

#Setting the y-axis to display the correct intervals
ax.ticklabel_format(style='plain', axis ='y')

#Show plot
plt.show()