class ImageConverter:
    def __init__(self, filename):
        self.filename = filename

    def imageToBinary(self):
        with open(self.filename, 'rb') as fh:
            self.binaryData = fh.read()
        return self.binaryData

    def binaryToImage(self):
        fh = open('img.png', 'wb')
        fh.write(self.binaryData)
        fh.close()

