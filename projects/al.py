from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# Open the desired Image you want to add text on
i = Image.open('recpt.jpg')

# To add 2D graphics in an image call draw Method

Im = ImageDraw.Draw(i)
mf = ImageFont.truetype('Cookiesandcream.ttf', 25)
# Add Text to an image
Im.text((15,15), "Lady watching movie with her dog", (255,255,0), font=mf)

# Display edited image on which we have added the text
# i.show()

# Save the image on which we have added the text
i.save("mm.png")