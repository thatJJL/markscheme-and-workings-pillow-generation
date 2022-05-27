#markscheme-and-workings-pillow-generation.py1
#Checking import_or_install works or how I get it to work again.

def import_or_install(package): #From my "2021-11-09 Screenshot save\3 timings PRODUCT. WORKING.py"
    import pip
    import importlib #https://stackoverflow.com/questions/26743012/python-cant-find-importlib
    try:
        return __import__(package)
    except ImportError:
        print(f"'{package}' not loaded")
        #return None
        #pip.main(['install', package])

        pip.main(['install', '--user', package]) #Does do something. ###

        #import_or_install(package) #Could probably just use the import function too.
        #^^^ Loops

        #return __import__(package)


        #https://stackoverflow.com/questions/9806963/how-to-use-the-import-function-to-import-a-name-from-a-submodule
        importlib.import_module(package)



def main():
    print("main function")
    #import_or_install("Pillow") #Works but then the import name is different from the install name
    import_or_install("Pillow")


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
