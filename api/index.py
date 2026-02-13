from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io
import base64

def handler(request):

    img = Image.open("base.jpg")
    draw = ImageDraw.Draw(img)

    # ---- SETTINGS ----
    start_date = datetime(2026, 2, 11)
    today = datetime.now()

    days_passed = (today - start_date).days % 40

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
                color = (255, 120, 255)
            elif count < days_passed:
                color = (255, 255, 255)
            else:
                color = (80, 80, 80)

            draw.ellipse(
                (x-radius, y-radius, x+radius, y+radius),
                fill=color
            )

            count += 1

    # ---- RETURN IMAGE ----
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")

    encoded = base64.b64encode(buffer.getvalue()).decode()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/jpeg",
            "Content-Disposition": "inline"

        },
        "body": encoded,
        "isBase64Encoded": True
    }
