import pickle
from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description="My Cool Gooey App!")
    parser.add_argument('DO_API_Key', help="Digital Ocean API Key", widget='TextField')
    args = vars(parser.parse_args())
    DO_API_key = (args['DO_API_Key'])

    API_dict = {'DO_key':DO_API_key}

    pickling_on = open("API_dict.pickle","wb")
    pickle.dump(API_dict, pickling_on)
    pickling_on.close()

    pickle_off = open("API_dict.pickle","rb")
    API_dict_read_in = pickle.load(pickle_off)
    print(API_dict_read_in)
    print(API_dict_read_in['DO_key'])

if __name__ == '__main__':
    main()