from pdf2image import convert_from_path
from PIL import Image

# with dpi = 500
left = 150  # 0.098 * width
top = 150  # 0.121 * height
right = 1382  # 0.902 * width  <-  width - 150
bottom = 965  # 0.778 * height  <-  height - 275

popplerPath = "C:/Users/danie/Desktop/poppler-24.02.0/Library/bin"

backExpDir = "C:/Users/danie/Desktop/grafiche/GoldBack/"
frontExpDir = "C:/Users/danie/Desktop/grafiche/GoldFront/"

resourcesExpDir = "C:/Users/danie/Desktop/grafiche/Resources/"

backPdfDir = "C:/Users/danie/Desktop/grafiche/CODEX_cards_gold_back.pdf"
frontPdfDir = "C:/Users/danie/Desktop/grafiche/CODEX_cards_gold_front.pdf"
boardPdfDir = "C:/Users/danie/Desktop/grafiche/PLATEAU-SCORE-IMP.pdf"

rawExpBackDir = "RawExpBack/"
rawExpFrontDir = "RawExpFront/"


def convertAndCrop(pdfDir, expDir, rawExpDir, side: str):
    images = convert_from_path(pdf_path=pdfDir, poppler_path=popplerPath, dpi=500)

    for i in range(len(images)):
        images[i].save(rawExpDir + "page" + str(i) + ".png", 'PNG')

    for i in range(len(images)):
        im = Image.open("C:/Users/danie/PycharmProjects/imageExorter/" + rawExpDir + f"page{i}.png")

        im1 = im.crop((left, top, right, bottom))

        # Saves the image
        im1.save(expDir + side + "Card" + str(i) + ".png", "PNG")


def convertAndCropBoard():
    images = convert_from_path(pdf_path=boardPdfDir, poppler_path=popplerPath, dpi=500)

    images[0].save("RawExpBoard/page0.png", 'PNG')

    im = Image.open("C:/Users/danie/PycharmProjects/imageExorter/RawExpBoard/page0.png")

    leftB = 155
    topB = 155
    rightB = im.width - 156
    bottomB = im.height - 155

    im1 = im.crop((leftB, topB, rightB, bottomB))

    im1.save(resourcesExpDir + "Board.png", "PNG")


# convertAndCrop(pdfDir=frontPdfDir, expDir=resourcesExpDir, rawExpDir=rawExpFrontDir, side="front")
# convertAndCrop(pdfDir=backPdfDir, expDir=resourcesExpDir, rawExpDir=rawExpBackDir, side="back")
convertAndCropBoard()
