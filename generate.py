from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# ---- LOAD IMAGE ----
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# ---- SETTINGS ----
start_date = datetime(2026, 2, 6)
today = datetime.now()

days_passed = (today - start_date).days % 40
# days_passed = 15


rows = 4
cols = 10

start_x = 120
start_y = 900
spacing_x = 85
spacing_y = 85
radius = 20

# ---- TEXT ----
text = "TIME"
font = ImageFont.load_default()

grid_width = (cols - 1) * spacing_x
text_x = start_x + grid_width // 2
text_y = start_y - 120

bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]

draw.text(
    (text_x - text_width // 2, text_y),
    text,
    fill=(255, 255, 255),
    font=font
)

# ---- DOTS ----
count = 0

for r in range(rows):
    for c in range(cols):

        x = start_x + c * spacing_x
        y = start_y + r * spacing_y

        if count == days_passed - 1:
            color = (255, 120, 255)   # today's dot
        elif count < days_passed:
            color = (255, 255, 255)   # completed
        else:
            color = (80, 80, 80)      # future

        draw.ellipse(
            (x-radius, y-radius, x+radius, y+radius),
            fill=color
        )

        count += 1

draw.text(
    (10, 10),
    str(datetime.now()),
    fill=(0, 0, 0),
    font=ImageFont.load_default()
)
        

# ---- SAVE OUTPUT ----
today_str = today.strftime("%Y-%m-%d")
filename = f"output-{today_str}.jpg"
img.save(filename)


print("Wallpaper generated: output.jpg")
