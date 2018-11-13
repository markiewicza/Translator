import os
import re
import pandas as pd

from collections import OrderedDict


def compile_lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = [x.strip('\n') for x in file.readlines()]
        lines = []
        for i, line in enumerate(content):
            if (not line.lstrip().startswith('#')) and (len(line.strip()) != 0):
                if content[i-1][-1:] == '\\':
                    lines[-1] += line
                    continue
            lines.append(line)

    return lines


def gather_english_phrases(file_path):
    english_phrases = []
    lines = compile_lines_from_file(file_path)
    for line in lines:
        if (not line.lstrip().startswith('#')) and (len(line.strip()) != 0):
            phrase = '='.join(line.split('=')[1:]).strip('\n')
            phrase = swap_aliases(phrase)
            english_phrases.append(phrase)
    return english_phrases


def gather_english_phrases_from_files(directory):
    phrases = []
    for filename in os.listdir(directory):
        if '_pl' not in filename:
            print(filename)
            phrases += gather_english_phrases(directory + '/' + filename)
    phrases = list(OrderedDict.fromkeys(phrases))

    with open('english_phrases_new.csv', 'a', encoding='utf-8') as file:
        for phrase in phrases:
            file.write(phrase + '\n')


def swap_aliases(phrase):
    aliases = re.findall(r'\$\[(.*?)\]', phrase)
    for alias in aliases:
        swap = search_for_alias(alias)
        if swap:
            phrase = phrase.replace(f'$[{alias}]', swap)
    return phrase


def search_for_alias(alias):
    directory = 'translations'
    files = os.listdir(directory)
    move_element_to_front('TitaniumEntityNamingConfigurations_en.properties', files)
    for filename in files:
        if '_pl' not in filename:
            lines = compile_lines_from_file(directory + '/' + filename)
            for line in lines:
                if (not line.lstrip().startswith('#')) and (len(line.strip()) != 0):
                    phrase = line.split('=')
                    label = phrase[0]
                    value = "=".join(phrase[1:])
                    if label == alias:
                        return value.strip('\n')


def move_element_to_front(elem, my_list):
    my_list.insert(0, my_list.pop(my_list.index(elem)))


def create_dictionary_from_file(file_path_from, file_path_to, trans_from, trans_to):
    df1 = pd.read_csv(file_path_from, encoding='utf-8', header=None, names=[trans_from], sep=';')
    df2 = pd.read_csv(file_path_to, encoding='utf-8', header=None, names=[trans_to], sep=';')
    df = pd.concat([df1, df2], axis=1, sort=False)
    #print(df)
    return df


def translate_file(file_path, translated_file_path, dictionary, trans_from, trans_to):
    with open(translated_file_path, 'w', encoding='utf-8') as new_file:
        lines = compile_lines_from_file(file_path)
        for line in lines:
            if (not line.lstrip().startswith('#')) and (len(line.strip()) != 0):
                phrase = list(map(lambda x: x.replace('\n', ''), line.split("=")))
                label = phrase[0]
                value = "=".join(phrase[1:])
                swap = swap_aliases(value).strip()
                translations = dictionary[dictionary[trans_from] == swap][trans_to].values
                if value:
                    if len(translations) != 0:
                        #print(swap, translations)
                        translation_to_print = translations[0].replace("\\ ", "\\\n").replace("\\\t", "\\\n\t")
                        new_file.write(f'{label}={translation_to_print}\n')
                    else:
                        swap_to_print = swap.replace("\\ ", "\\\n").replace("\\\t", "\\\n\t")
                        new_file.write(f'{label}={swap_to_print}\n')
                else:
                    new_file.write(f'{label}=\n')
            else:
                new_file.write(f'{line}\n')


def translate_files(directory, dictionary, trans_from, trans_to):
    for filename in os.listdir(directory):
        if '_pl' not in filename:
            file_path_from = directory + '/' + filename
            new_filename = '.'.join(filename.split('.')[:-1]).split('_')
            new_filename = '_'.join(new_filename) if filename[-1] != 'en' else '_'.join(new_filename[:-1])
            new_filename += '_pl.properties'
            print(new_filename)
            file_path_to = directory + '/' + new_filename
            translate_file(file_path_from, file_path_to, dictionary, trans_from, trans_to)


