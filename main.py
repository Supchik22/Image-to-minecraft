from PIL import Image






f = open('image.mcfunction', "w")

im = Image.open('image.png')
text = ""
for pixel in range(64):
  for line in range(64):
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((line, pixel))
#    print(r, g, b)
    if r <= 100 and g <= 100 and b <= 100:
      text = text + f"setblock ~ ~{line} ~{pixel} stone\n"
    if r >= 100 and g >= 100 and b >= 100:
      text = text + f"setblock ~ ~{line} ~{pixel} iron_block\n"

f.write(text)
f.close()