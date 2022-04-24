
# optparse_test.py

import optparse

def get_optparse(args=None):
    useage= 'show something helpfull -- for example: how to use this program'
    optParser = optparse.OptionParser(useage)

    optParser.add_option("-f", "--file", dest='filename', 
                        help="read picture from File", metavar="FILE", action="store", type="string")

    optParser.add_option("-s","--save", dest="save_mode", action="store_false",
                        help="save image to file or not", default = True)

    optParser.add_option("-r", "--random", action="store_true",
                         default=False, help="use a random seed to initialize the random number generator")

    options, args = optParser.parse_args(args)
    return options

if __name__ == '__main__':

    options = get_optparse()

    print(options.filename)
    print(options.save_mode)
    print(options.random)
    
    print(options)
