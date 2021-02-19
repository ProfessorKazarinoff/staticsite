import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv', header=0)
colors = sns.color_palette("pastel")

# Four subplots, unpack the axes array immediately
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(9, 3), sharey=True)

# Plot a historgram and kernel density estimate
ax1 = sns.distplot(df.Rectangle[df.Rectangle.notnull()], color=colors[0], ax=ax1)
ax1.set_xlabel('Density Range ($g/cm^3$)')
ax1.set_title('Rectangles')
ax1.set_ylim(0,8)
ax1.set_yticklabels([])

#plt.show()

# Plot a historgram and kernel density estimate
ax2 = sns.distplot(df.Square[df.Square.notnull()], color=colors[1], ax=ax2)
ax2.set_xlabel('Density Range ($g/cm^3$)')
ax2.set_title('Squares')
#plt.show()

# Plot a historgram and kernel density estimate
ax3 = sns.distplot(df.Triangle[df.Triangle.notnull()], color=colors[2], ax=ax3)
ax3.set_xlabel('Density Range ($g/cm^3$)')
ax3.set_title('Triangle')
#plt.show()

# Plot a historgram and kernel density estimate
ax4 = sns.distplot(df.Cylinder[df.Cylinder.notnull()], color=colors[3], ax=ax4)
ax4.set_xlabel('Density Range ($g/cm^3$)')
ax4.set_title('Cylinders')
#plt.show()

plt.tight_layout()
plt.show()