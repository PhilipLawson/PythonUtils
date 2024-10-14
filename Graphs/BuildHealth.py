import matplotlib.pyplot as plt

total_pass = 0
total_fail = 0

# Label Information
BUILD_LABEL = 'X64-VS2019'
data = [0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1,1]
x_axis = 0
fig, ax = plt.subplots()

# Plot the lines (remove to hide)
plt.plot(data, color="gray", linestyle="--", alpha=.2)

# For each build (x axis), create a green dot if 1 else create a red dot
for dot in data:
    if dot > 0:
        plt.plot(x_axis, dot, 'go')
        total_pass = total_pass + 1
    else:
        plt.plot(x_axis, dot, 'ro')
        total_fail = total_fail + 1
    x_axis = x_axis + 1

# Set the label names and title
plt.ylabel('Build Health')
plt.xlabel('Build Run')
plt.title(BUILD_LABEL)
# Set custom ticks on the y-axis
ax.set_yticks([0, 1])
ax.set_yticklabels(['Fail', 'Pass'])

# Clear the x axis ticks
ax.set_xticks([])

# Display total pass and total fail below the graph
plt.text(-1.0, -0.15, f'Total Pass: {total_pass}', fontsize=12, color='green', verticalalignment='top')
plt.text(4, -0.15, f'Total Fail: {total_fail}', fontsize=12, color='red', verticalalignment='top')

# Render the image
plt.show()