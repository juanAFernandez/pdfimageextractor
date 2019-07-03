from pdf2image import convert_from_path
from PIL import Image


def extract_image(fromfolder, pdfname, to, rectangle):

    pdfpath = fromfolder + pdfname;
    page = convert_from_path(pdfpath)[0]
    page.save('tmp.jpeg', 'JPEG')

    image = Image.open('tmp.jpeg')

    cropped_example = image.crop((
        rectangle[0], rectangle[1],
        rectangle[2], rectangle[3]
    ))

    imagepath = pdfname.replace('pdf', 'jpeg')

    cropped_example.save(imagepath, 'JPEG')



# extract_images(inputfoder, outputfolder, coordinates)

# extract_image('../', '24106440.pdf', '.', [1191, 1321, 1478, 1659])