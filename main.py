import sys
import glob
sys.path.append('./modules/')
import imageconverter

def main():
    n = len(sys.argv)
    
    if n < 2 or n > 2:
        print("Incorrect amount of arguments. The program needs a width value to run.\n Example: python3 ./main.py 1500")
        exit(-1)

    getFiles = glob.glob('./All/*.jpg')
    convCreate = imageconverter.ImageConverter(getFiles, sys.argv[1]) 
    print('Created Image Converter Successfully')
    print(convCreate.GetWidth())
    convCreate.ConvertImages()


main()
