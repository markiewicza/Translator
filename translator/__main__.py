from .translator_class import *
import sys
import argparse


def main():
    args = vars(parse_arguments())
    gather_english_phrases_from_files(args['input_directory'], args['file_path_from'])
    eng_pl = create_dictionary_from_file(file_path_from=args['file_path_from'], file_path_to=args['file_path_to'],
                                         trans_from=args['trans_from'], trans_to=args['trans_to'])
    translate_files(directory=args['input_directory'], dictionary=eng_pl,
                    trans_from=args['trans_from'], trans_to=args['trans_to'])


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_directory", "-i", help="input directory path", type=str)
    parser.add_argument("--file_path_from_trans", "-pf", help="input dictionary path", type=str)
    parser.add_argument("--file_path_to_trans", "-pt", help="output dictionary path", type=str)
    parser.add_argument("--trans_from", "-f", help="language to translate from", type=str)
    parser.add_argument("--trans_to", "-t", help="language to translate to", type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
    gather_english_phrases_from_files('translations', 'english_phrases_new.csv')
    eng_pl = create_dictionary_from_file(file_path_from='english_phrases.csv', file_path_to='polish_phrases.csv',
                                         trans_from='ENG', trans_to='PL')
    translate_files(directory='translations', dictionary=eng_pl, trans_from='ENG', trans_to='PL')
