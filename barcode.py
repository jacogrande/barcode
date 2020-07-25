# executable file that takes an input file argument
import main as barcode
import sys, getopt


def main(argv):
  inputfile=''
  k=10
  frame_width=1
  frame_height=2000
  grayscale = False
  try:
    opts, args = getopt.getopt(argv,"mi:k:w:h:g",["ifile="])
  except getopt.GetoptError:
    print('barcode.py -i <inputfile> [-k <kmeans>] [-w <frameWidth>] [-h <frameHeight] [-g] [-m]')
    sys.exit(2)
  
  for opt, arg in opts: 
    if opt == '-m':
      print('barcode.py -i <inputfile> [-k <kmeans>] [-w <frameWidth>] [-h <frameHeight] [-g] [-m]')
      sys.exit()
    elif opt in ("-i", "-input"):
      inputfile = arg
    elif opt in ("-k", "-kmeans"):
      k = int(arg)
    elif opt in ("-w", "-width"):
      frame_width = int(arg)
    elif opt in ("-h", "-height"):
      frame_height = int(arg)
    elif opt == "-g":
      grayscale = True
  
  barcode.generate(inputfile, k, frame_width, frame_height, grayscale)

if __name__ == "__main__":
  main(sys.argv[1:])