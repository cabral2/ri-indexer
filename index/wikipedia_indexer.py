from index.indexer import *
from index.structure import *

if __name__ == "__main__":
    HTMLIndexer.cleaner = Cleaner(stop_words_file="stopwords.txt",
                        language="portuguese",
                        perform_stop_words_removal=True,
                        perform_accents_removal=True,
                        perform_stemming=False)

    index = FileIndex()
    indexador = HTMLIndexer(index)
    indexador.index_text_dir("C:\Users\savio\Documents\\ri-indexer\\ri-tp-wiki-data-master")
    