from mutable_document import Document as MutableDocument
from immutable_document import Document as ImmutableDocument

def test_mutable():
    document = MutableDocument("Старый текст")
    old_document = document

    document.set_text("Новый текст")

    assert document.text == "Новый текст"
    assert old_document.text == "Новый текст"

def test_immutable():
    document = ImmutableDocument("Старый текст")
    new_document = document.with_text("Новый текст")

    assert document.text == "Старый текст"
    assert new_document.text == "Новый текст"