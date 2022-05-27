#import_or_install1
#Rename the the original as I didn't realise I was editing the orignal until after I'd started. I'd saved a copy of the generator though so it was good.
#Modified from markscheme-and-workings-pillow-generation.py1
#Checking import_or_install works or how I get it to work again.

#Intially from my "2021-11-09 Screenshot save\3 timings PRODUCT. WORKING.py"
#then modifed from from markscheme-and-workings-pillow-generation1
def import_or_install(package):
    import pip
    import importlib
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
    

if __name__ == "__main__":
    main()
