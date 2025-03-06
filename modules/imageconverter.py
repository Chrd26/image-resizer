from PIL import Image 
import os

class ImageConverter:
    setSize = 0
    getNumberOfFiles = 0
    getFilePaths = []

    def __new__(cls, *args, **kwargs):
        print("Creating new class")
        getArgLength = len(args)

        instance = super().__new__(cls)
        instance.setSize = args[getArgLength - 1]
        instance.getNumberOfFiles = args[getArgLength - 1]

        for item in args[0]:
            instance.getFilePaths.append(item)

        return instance

    def GetWidth(self):
        return self.setSize

        # Resize image getting value percentages 
        # Fix image name string and save image    
    def ConvertImages(self):
        directoryToSearch = 'Exports'

        if os.path.isdir(directoryToSearch) is False:
            os.mkdir(directoryToSearch)
        else:
            print("Directory already exists")


        for path in self.getFilePaths:
            with Image.open(path) as getImage:
                getPerc = int(self.setSize) / getImage.size[0] 
                setImageWidth = round(getImage.size[0] * getPerc)
                setImageHeight = round(getImage.size[1] * getPerc)

                finalSize = [setImageWidth, setImageHeight]

                resizedImage = getImage.resize(finalSize, Image.Resampling.LANCZOS)

                getFileName = path.replace('./All/', '')
                print(getFileName)

                resizedImage.save('./Exports/' + getFileName, 'JPEG', optimize=True, quality=60)
        print("Operation is completed")


