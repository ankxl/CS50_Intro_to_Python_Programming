import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if (not (sys.argv[1].strip().lower().endswith(".jpg") or
        sys.argv[1].strip().lower().endswith(".jpeg") or
        sys.argv[1].strip().lower().endswith(".png"))):
        sys.exit("Invalid input")

    if (not (sys.argv[2].strip().lower().endswith(".jpg") or
        sys.argv[2].strip().lower().endswith(".jpeg") or
        sys.argv[2].strip().lower().endswith(".png"))):
        sys.exit("Invalid output")

    if not ((sys.argv[1].strip().lower().endswith(".jpg") and sys.argv[2].strip().lower().endswith(".jpg")) or
        (sys.argv[1].strip().lower().endswith(".jpeg") and sys.argv[2].strip().lower().endswith(".jpeg"))or
        (sys.argv[1].strip().lower().endswith(".png") and sys.argv[2].strip().lower().endswith(".png"))
        ):
        sys.exit("Input and output have different extensions")

    get_file(sys.argv[1],sys.argv[2])

def get_file(fileread,filewrite):
    try:
        imread = Image.open(fileread)
        imshirt = Image.open("shirt.png")
        # imwrite = Image.open(filewrite)
        size = imshirt.size
        imwrite = ImageOps.fit(imread,size)
        imwrite.paste(imshirt,(0,0),mask=imshirt)
        # imwrite.paste(ImageOps.fit(imread,size),imshirt)
        imwrite.save(filewrite)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

