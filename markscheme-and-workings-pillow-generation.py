#markscheme-and-workings-pillow-generation6
#Added colour to the pages

import private.import_or_install as ioi

from PIL import Image


#def dpi_to_pixels(): #For converting page dimensions to pixels using dpi.

def mark_scored_text():
    print()
    

def create_page(height = 2480, width = 3508, colour = ( 255 , 255 , 255 )):
    #Expecting inegers and tuple
    
    #https://forums.techguy.org/threads/pixel-size-of-a-single-a4-word-document.447822/
    #"2480 x 3508 pixels would give you the equivalent to an A4 sheet at 300 dots-per-inch. This would match the typical draft output from an inkjet printer."
    #2480x3508 at 300 dpi

    #img  = Image.new( mode = "RGB", size = (height, width), color = ( 153 , 153 , 255 ) )
    img  = Image.new( mode = "RGB", size = (height, width),
                      #color = ( 153 , 153 , 255 )
                      color = colour
                      )
    
    
    return img


def main():
    print("main function")
    #import_or_install("Pillow") #Works but then the import name is different from the install name
    ioi.import_or_install("Pillow", "PIL")

    test_page_colour = ( 153 , 153 , 255 )

    page = create_page()
    page.show()

    square = create_page(300, 300)
    square.show()

    page_col = create_page(colour = test_page_colour)
    page_col.show()



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
