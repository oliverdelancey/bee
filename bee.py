#!/usr/bin/env python3
"""bee v0.0.1"""

import argparse
import random
import sys

from nltk.corpus import wordnet as wn


def get_keywords(file_name):
    """get keywords"""
    with open(file_name, "r") as f:
        contents = f.read()
    keywords = contents.split("\n")
    keywords = [i for i in keywords if i]
    return keywords


def get_related(word):
    """get words related to this word"""
    mass_list = []
    print(f"original: {word}")
    definitions = wn.synsets(word)
    original_set = definitions[0]
    for ss in definitions:
        if (original_set.wup_similarity(ss)) == None:
            continue
        elif (original_set.wup_similarity(ss)) <= 0.5:
            continue
        print(f"definition: {ss.name()}")
        # synonyms
        print("    synonyms:")
        for syn in ss.lemma_names():
            print(f"        {syn}")
            mass_list.append(syn)
        # hyponyms
        for hypo in ss.hyponyms():
            hypo_syn = hypo.lemma_names()
            mass_list += hypo_syn
            print(f"    hyponym: {hypo_syn[0]} --synonyms:")
            for syn_syn in hypo_syn:
                print(f"        {syn_syn}")
        for hyper in ss.hypernyms():
            hyper_syn = hyper.lemma_names()
            mass_list += hyper_syn
            print(f"    hypernym: {hyper_syn[0]} --synonyms:")
            for syn_syn in hyper_syn:
                print(f"        {syn_syn}")
    return mass_list


def generate_pool(keywords):
    """generate a 'pool' of keywords"""
    pool = []
    for i in keywords:
        pool.append(get_related(i))
    return pool


def generate_name(pool):
    """generate a random name from the pool"""
    topic_1 = random.choice(pool)
    while True:
        topic_2 = random.choice(pool)
        if topic_2 != topic_1:
            break
    word_1 = random.choice(topic_1)
    word_2 = random.choice(topic_2)
    delimiters = ["", "-", "_", "single_cap", "double_cap"]
    delimiter = random.choice(delimiters)
    if delimiter == "single_cap":
        name = word_1 + word_2.capitalize()
    elif delimiter == "double_cap":
        name = word_1.capitalize() + word_2.capitalize()
    else:
        name = word_1 + delimiter + word_2
    return name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate random project names based on keywords")
    parser.add_argument(
        "file",
        help="input file containing list of keywords")
    parser.add_argument(
        "num_names",
        metavar="N",
        type=int,
        help="number of project names to generate")

    args = parser.parse_args()

    if args.num_names <= 0:
        sys.stderr.write("    Error: N is not >= 0.\n    Aborting program.")
        sys.stderr.flush()
        sys.exit(1)

    keywords = get_keywords(args.file)
    pool = generate_pool(keywords)

    i = 0
    name = ""
    name_prev = " "
    while i < args.num_names:
        name = generate_name(pool)
        if name == name_prev:
            i -= 1
        else:
            i += 1
            print(name)
        name_prev = name
