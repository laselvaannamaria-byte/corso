"""Test di esempio: serve solo perché GitHub Actions abbia qualcosa da eseguire.

Sostituiscilo con i test della tua UdA, per esempio:

    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
    from mio_modulo import mia_funzione

    def test_caso_normale():
        assert mia_funzione([1, 2, 3]) == 6
"""


def raddoppia(n):
    return n * 2


def test_esempio():
    assert raddoppia(3) == 6
