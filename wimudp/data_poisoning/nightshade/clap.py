from typing import List

import laion_clap


class CLAP:
    def __init__(self):
        self.model = laion_clap.CLAP_Module(enable_fusion=False)
        self.model.load_ckpt(verbose=False)

    def get_text_features(self, texts: List[str]) -> List[str]:
        return self.model.get_text_embedding(texts, use_tensor=True)
