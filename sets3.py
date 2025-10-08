# Starting set
colors = {"red", "blue"}

# Two iterables
more_colors_list = ["green", "yellow"]
more_colors_tuple = ("purple", "orange")

# Use update() to add both
colors.update(more_colors_list, more_colors_tuple)
print("After update:", colors)
