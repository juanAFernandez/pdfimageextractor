from . import pdfimageextractor as extractor
import argparse

def main():
    # print(ascii_snek)

    parser = argparse.ArgumentParser(description='PDF Image Extractor v1.0')
    # Positional argument
    parser.add_argument(
        'input', metavar='input', type=str, nargs=1,
        help='Input folder or file.'
    )
    parser.add_argument(
        'output', metavar='output', type=str, nargs=1,
        help='Output folder or file.'
    )
    parser.add_argument(
        'coordinates', metavar='coordinates', type=int, nargs=4,
        help='Coordinates to crop the segment.'
    )
    args = parser.parse_args()

    extractor.extract_image(args['input'], args['output'], args['coordinates'])



if __name__ == '__main__':
    main()



