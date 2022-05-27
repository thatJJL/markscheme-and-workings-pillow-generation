#markscheme-and-workings-pillow-generation2
#Importing import_or_install function
import private.import_or_install as ioi



def main():
    print("main function")
    #import_or_install("Pillow") #Works but then the import name is different from the install name
    ioi.import_or_install("Pillow", "PIL")


    #For checking if it is installed
    from PIL import Image
    #https://pythonexamples.org/python-pillow-create-image/

    width = 400
    height = 300

    img  = Image.new( mode = "RGB", size = (width, height) )
    img.show()
    
    input()

if __name__ == "__main__":
    main()
