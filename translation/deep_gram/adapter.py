from server.config import DeepGramConfig
from translation.adapter import TranslationAdapter


class DeepGramAdapter(TranslationAdapter):
    def __init__(self, config: DeepGramConfig):
        self.config = config
