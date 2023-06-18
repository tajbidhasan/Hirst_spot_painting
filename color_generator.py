import colorgram

# Specify the path to your image
image_path = "image.jpg"

# Extract colors from the image
colors = colorgram.extract(image_path, 25)  # Extract 25 colors

rgb_colors = []

# Print and store the RGB values of the extracted colors
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r, g, b)
    rgb_colors.append(rgb_tuple)

print(rgb_colors)
