## pdfimageextractor
Very simple tool to extract images from pdf based using coordinates.


### Use

`pdfimageextractor input output coordinates`

Where input and output can be a file (always will be with jpeg) or a folder in both to iterate.

Examples:

```
# pdfimageextractor ./pdfs ./images [1191, 1321, 1478, 1659]
# pdfimageextractor  sample.pdf sample [1191, 1321, 1478, 1659]
```

Coordinates system used is the [**cartesian pixel coordinate system**](https://pillow.readthedocs.io/en/3.3.x/handbook/concepts.html#coordinate-system).


### License
Under GNU CPLv3