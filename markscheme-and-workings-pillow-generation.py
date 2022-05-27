#markscheme-and-workings-pillow-generation9
#Updated marks box function - (its) name, (paste) position, text colour

import private.import_or_install as ioi

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



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

    #Maybe allow fractions to be input so that way marking could have one of two marks scored. That or a blank denominator so it can have the marks achieved written on. 16:41pm 27/May/22 i8. TODO. I'd thought about the blank top fraction when first writing this (function).
    
    
    return img


#def dpi_to_pixels(): #For converting page dimensions to pixels using dpi.


#def mark_scored_text(image_object, text_line, marks): #text line instead of just text as it won't yet do new lines, neccarily.
def paste_mark_box(image_object, marks, posx, posy, text_col = (0,0,0), font_object = None):
    #It edits the image obect directly.

    if font_object == None: #Setting the default text font
        #text_font = ImageFont.truetype('FreeMono.ttf', 65)
        #text_font = ImageFont.load("arial.pil") #https://pillow.readthedocs.io/en/stable/reference/ImageFont.html
        text_font = ImageFont.truetype('arial.ttf', 10)
        print("font defaulted")
    else:
        text_font = font_object

    mark_text = f"[{marks}"
    if marks != 1:
        mark_text += " marks]"
    else:
        mark_text += " mark]"


    #Add validation for if the (paste) position is within the canvas 16:37 i8 27/May/22. TODO.
    
    image_object.text((posx, posy),
                      mark_text,
                      fill = text_col,
                      font = text_font,
                      )
    



def main():
    print("main function")
    #import_or_install("Pillow") #Works but then the import name is different from the install name
    ioi.import_or_install("Pillow", "PIL")

    test_page_colour = ( 153 , 153 , 255 )
    '''
    page = create_page()
    page.show()

    square = create_page(300, 300)
    square.show()
    '''

    page_col = create_page(colour = test_page_colour)
    #page_col.show()
    

    #https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/
    #writing = ImageDraw.Draw(page_col)
    write_on_page = ImageDraw.Draw(page_col)
    #write_on_page.text((28, 36), "nice Car", fill=(255, 0, 0))
    paste_mark_box(write_on_page, 1, 100, 100)
    paste_mark_box(write_on_page, 2, 100, 200, (255, 0, 0))


    #writing_font.truetype('FreeMono.ttf', 20)
    #writing_font = ImageFont.truetype("arial.ttf", 15)
    writing_font = ImageFont.truetype("arial.ttf", 30)
    paste_mark_box(write_on_page, 30, 100, 300, (255, 0, 0), font_object = writing_font)
    paste_mark_box(write_on_page, 30, 100, 350, (0, 255, 0), writing_font)
    page_col.show()
    
    

if __name__ == "__main__":
    main()
