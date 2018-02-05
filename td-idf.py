from __future__ import division
import string
import math
import numpy as np

tokenize = lambda doc: doc.lower().split(" ")

document_0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy."
document_1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption."
document_2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people."
document_3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled."
document_4 = "What's the future of Abenomics? We asked Shinzo Abe for his views"
document_5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily."
document_6 = "Vladimir Putin was found to be riding a horse, again, without a shirt on while hunting deer. Vladimir Putin always seems so serious about things - even riding horses."

all_documents = [document_0, document_1, document_2, document_3, document_4, document_5, document_6]

tokenized_documents = [tokenize(d) for d in all_documents] # tokenized docs
all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])

def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

print(all_tokens_set)

from sklearn.feature_extraction.text import TfidfVectorizer

sklearn_tfidf = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)

sklearn_representation = sklearn_tfidf.fit_transform(all_documents)
weights = np.asarray(sklearn_representation.mean(axis=0)).ravel().tolist()
# weights_df = pd.DataFrame({'term': cvec.get_feature_names(), 'weight': weights})
# weights_df.sort_values(by='weight', ascending=False).head(20)
#print sklearn_representation.toarray()[0].tolist()
print weights
print document_0
