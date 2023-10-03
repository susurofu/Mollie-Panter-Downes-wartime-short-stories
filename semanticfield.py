import re
import os
import spacy
nlp = spacy.load('en_core_web_sm', disable = ['parser', 'ner']) # Initialize spacy 'en' model, keeping only tagger component needed
from nltk import Text 
from textanalyzer import TextAnalyzer


def war_semantic_field (lemmatized_text):
    with open (f'semantic_field_of_war.txt', encoding = 'utf-8') as f:
        semantic_field_of_war = f.readlines()
    field_and_attributes = []
    fields =[]
    attributes = []

    for line in semantic_field_of_war:
        field_and_attributes = line.split(';')
        fields.append(field_and_attributes[0])
        attributes.append(field_and_attributes[1].split(', ')) # the list of words attributed for this semantic subfield

    for line in attributes:
        line[-1] = re.sub('\n', '', line[-1])

    joined_text = ' '.join(lemmatized_text)


    results_of_search = []
    words_found = []
    for i in range(len(attributes)):
        subresults = []
        for k in range(len(attributes[i])):
            subresults.append(len(re.findall(attributes[i][k],joined_text)))
            if len(re.findall(attributes[i][k],joined_text)) != 0:
                words_found.append(re.findall(attributes[i][k],joined_text))
        results_of_search.append(subresults)

    return results_of_search, words_found