from .translator_class import PropertyTranslator
import argparse


def main():
    args = vars(parse_arguments())
    action = args.pop('action')
    translator = PropertyTranslator(**args)
    if action is None:
        translator.gather_english_phrases_from_files()
        translator.create_dictionary_from_file()
        translator.translate_files()
    elif action == "only translate":
        translator.create_dictionary_from_file()
        translator.translate_files()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", "-a", help="action to take", type=str)
    parser.add_argument("--input_directory", "-i", help="input directory path", type=str)
    parser.add_argument("--file_path_from_trans", "-pf", help="input dictionary path", type=str)
    parser.add_argument("--file_path_to_trans", "-pt", help="output dictionary path", type=str)
    parser.add_argument("--trans_from", "-f", help="language to translate from", type=str)
    parser.add_argument("--trans_to", "-t", help="language to translate to", type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
