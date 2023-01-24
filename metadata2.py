import argparse
import pyexiv2

def ClearAllMetadata(imgname, preserve):
    metadata = pyexiv2.ImageMetadata(imgname)
    metadata.read()
    metadata.clear()
    metadata.write(preserve)

def ModifyMode(imgname, preserve):
    metadata = pyexiv2.ImageMetadata(imgname)
    metadata.read()
    for key, value in metadata.iteritems():
        print(key + value.raw_value)
    modkey = raw_input("Key to modify (q to quit):")
    while not modkey == 'q':
        print ("Editing:"+str(metadata[modkey].raw_value))
        modvalue = raw_input("New Value: (q to quit):")
        if modvalue == 'q':
            break
        metadata[modkey].raw_value = str(modvalue)
        modkey = raw_input("Key to modify (q to quit):")
    metadata.write(preserve)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help="Image file to manipulate")
    parser.add_argument("--clear", "-c", help="Clear all meta data from the file", action="store_true")
    parser.add_argument("--preserve", "-p", help="Preserve image modified date", action="store_true")
    args = parser.parse_args()
    if args.img:
        if args.clear:
            ClearAllMetadata(args.img, args.preserve)
        else:
            ModifyMode(args.img, args.preserve)
    else:
        print (parser.usage)

if __name__ == '__main__':
    Main()





