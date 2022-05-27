#markscheme-and-workings-pillow-generation4
#Create A4 page

import private.import_or_install as ioi

from PIL import Image


def create_A4_page():
    #https://forums.techguy.org/threads/pixel-size-of-a-single-a4-word-document.447822/
    #"2480 x 3508 pixels would give you the equivalent to an A4 sheet at 300 dots-per-inch. This would match the typical draft output from an inkjet printer."
    #2480x3508 at 300 dpi

    img  = Image.new( mode = "RGB", size = (2480, 3508) )
    
    return img


def main():
    print("main function")
    #import_or_install("Pillow") #Works but then the import name is different from the install name
    ioi.import_or_install("Pillow", "PIL")

    page = create_A4_page()
    page.show()



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
