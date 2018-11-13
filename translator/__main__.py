from .translator_class import *
import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]


if __name__ == '__main__':
    main()
    """
    with open('translations/TitaniumSystemRuntimeExceptionResource.properties', 'r') as file:
        for line in file:
            print([line])
    """
    gather_english_phrases_from_files('translations')
    eng_pl = create_dictionary_from_file(file_path_from='english_phrases.csv', file_path_to='polish_phrases.csv',
                                         trans_from='ENG', trans_to='PL')
    translate_files(directory='translations', dictionary=eng_pl, trans_from='ENG', trans_to='PL')
