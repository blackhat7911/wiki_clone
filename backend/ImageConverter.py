class ImageConverter:
    def __init__(self, filename):
        self.filename = filename

    def imageToBinary(self, value):
        with open(self.filename, 'rb') as fh:
            self.binaryData = fh.read()
            value.set(self.binaryData)
        return self.binaryData

    def binaryToImage(self, uname):
        fh = open("//home//bishal//Desktop//sem2-assignments//algoanddb//wiki_clone//user_img//{}.png".format(uname), 'wb')
        fh.write(self.binaryData)
        fh.close()

