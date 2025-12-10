
import base64
import os

png_path = '/Users/andrehassler/Desktop/Projects/Idea/ultimaitech/images/logo.png'
svg_path = '/Users/andrehassler/Desktop/Projects/Idea/ultimaitech/images/logo.svg'

with open(png_path, 'rb') as img_file:
    b64_string = base64.b64encode(img_file.read()).decode('utf-8')

# Assuming standard wide logo dimensions, but let's make it responsive
# We'll set a viewBox. Ideally we would know the image dimensions.
# Let's try to get dimensions if possible, or just set 100% width/height.
# For standard web use, a generic viewBox is often fine if we define width/height in CSS.

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50" preserveAspectRatio="xMidYMid meet">
  <image href="data:image/png;base64,{b64_string}" width="200" height="50" />
</svg>'''

with open(svg_path, 'w') as f:
    f.write(svg_content)

print(f"Created {svg_path}")
