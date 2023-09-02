import matplotlib.pyplot as plt

# Data for outer and inner layers
outer_labels = ['A', 'B', 'C']
outer_sizes = [120, 77, 39]

inner_labels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
inner_sizes = [60, 60, 37, 40, 29, 10]

# Define color schemes for each layer
outer_colors = ['#66b3ff', '#99ff99', '#ffcc99']
inner_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a figure and two subplots for the double donut chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Outer layer (larger donut)
wedges_outer, texts_outer, autotexts_outer = ax1.pie(outer_sizes, labels=outer_labels, autopct='%1.1f%%',
                                                      startangle=90, colors=outer_colors)
ax1.axis('equal')  # Equal aspect ratio ensures the chart is circular.
ax1.set_title('Outer Layer')

# Inner layer (smaller donut)
wedges_inner, texts_inner, autotexts_inner = ax2.pie(inner_sizes, labels=inner_labels, autopct='%1.1f%%',
                                                      startangle=90, colors=inner_colors)
ax2.axis('equal')  # Equal aspect ratio ensures the chart is circular.
ax2.set_title('Inner Layer')

# Add legend for the inner layer
ax2.legend(wedges_inner, inner_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))

# Customize labels and font sizes
for text in texts_outer + texts_inner:
    text.set_fontsize(12)
for autotext in autotexts_outer + autotexts_inner:
    autotext.set_fontsize(12)

plt.tight_layout()
plt.show()
