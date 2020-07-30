from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import json
import random

textBarSize = 100

with open('setting.json', 'r') as f:
    settings = json.load(f)
    text = random.choice(settings['words'])
    deepfry = settings['deepfry']
    emojiB = settings['emojiB']

files = os.listdir('images')
d = random.choice(files)

im = Image.open('images/'+d).convert('RGB')
bIm = Image.open('forMemes/bEmoji.png').convert('RGB')
imMain = Image.new("RGB", (im.width, im.height + textBarSize), (255, 255, 255, 0))
if deepfry:
    e = ImageEnhance.Sharpness(im)
    img = e.enhance(100)
    e = ImageEnhance.Contrast(img)
    im = img
if emojiB:
    funny = im.copy()
    for i in range(6):
        funny = funny.copy()
        funny.paste(bIm, (random.randint(0, imMain.width-50), random.randint(0, imMain.height-50)))
    im = funny
imDone = imMain.copy()
imDone.paste(im, (0, textBarSize))
imText = ImageDraw.Draw(imDone)
imText.multiline_text((im.width/2 - len(text) * 9, 30), text, (0, 0, 0), ImageFont.truetype("arial.ttf", 35), align="center")
funnyName = d.replace('.png', '')
imDone.save('memes/' + funnyName + '_memed' + str(random.randint(0, 100)) + '.png', 'PNG')
