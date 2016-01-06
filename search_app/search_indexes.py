from haystack import indexes
from search_app.models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Document
