#markscheme-and-workings-pillow-generation3
#
import private.import_or_install as ioi

from PIL import Image


def create_A4_page():
    print("WIP")


def main():
    print("main function")
    #import_or_install("Pillow") #Works but then the import name is different from the install name
    ioi.import_or_install("Pillow", "PIL")


    #For checking if it is installed
    '''   
    #https://pythonexamples.org/python-pillow-create-image/
    width = 400
    height = 300

    img  = Image.new( mode = "RGB", size = (width, height) )
    img.show()
    '''
    

if __name__ == "__main__":
    main()
