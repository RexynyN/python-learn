import argparse
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("Breno", help = "Show Output")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.Breno:
    print("Displaying Output as: % s" % args.Breno)

