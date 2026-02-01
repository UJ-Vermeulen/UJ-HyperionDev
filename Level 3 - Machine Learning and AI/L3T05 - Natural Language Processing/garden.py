# Import Spacy
import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Garden Path Sentences
# Make use of a dictionary to store the garden path sentences
# The keys will be the sentence number and the value will be the sentence
# This simplifies storing and accessing the multiple sentences
gardenpathSentences = {
    1: u'Mary gave the child a Band-Aid.',
    2: u'That Jill is never here hurts.',
    3: u'The cotton clothing is made of grows in Mississippi.',
    4: u'The sour drink from the ocean.',
    5: u'Time flies like an arrow; fruit flies like a banana.'
}

# Tokenisation
# Make a for loop to iterate through the dictionary
# Include stop identification in for loop
print('Tokenisation')
for key, gps_sentence in gardenpathSentences.items():
    doc = nlp(gps_sentence)
    # Print the sentence number and the tokens in the sentence
    print([token.orth_ for token in doc
           if not token.is_punct | token.is_space])
    for word in doc:
        if not word.is_stop:
            print(word.text)

# Lemmatisation to identify the root form of words
print('\nLemmatisation')
for key, gps_sentence in gardenpathSentences.items():
    doc = nlp(gps_sentence)
    print([word.lemma_ for word in doc])

# Named Entity Recognition
# Create an empty list to store the entity identifications
# Use append to add the entity identifications to the list
# As it iterates through the dictionary
print('\nNamed Entity Recognition')
entity_identifications = []
for key, gps_sentence in gardenpathSentences.items():
    nlp_doc = nlp(gps_sentence)
    for ent in nlp_doc.ents:
        entity_identifications.append((ent.text, ent.label_, ent.label))
        print([(i, i.label_, i.label) for i in nlp_doc.ents])

# Get an explanation of an entity and print it
# Make use of the entity_identifications list to
# iterate through the entities and print the explanation
print('\nExplanation of Entities')
for entity in entity_identifications:
    label = entity[1]
    explanation = spacy.explain(label)
    print(f"{label}: {explanation}")


# Choose 2 entities to explain: PERSON and GPE
# PERSON: Refers to people, including fictional
# GPE: Refers to countries, cities, states
# Both of these were correctly identified in the sentences
# and using the explain method, their meanings were confirmed.
# And both of these entities made sense in the context of the sentences.

# However, one entity was erroneously identified, namely 'Time'.
# It was identified as an ORG, or organisation, when it should
# have been identified as a DATE. In this context (A metaphor),
# 'Time' is a temporal entity, not an organisation, as it refers
# To the passing of time.
