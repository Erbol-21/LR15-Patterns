from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    text: str

    def with_text(self, text):
        return Document(text)