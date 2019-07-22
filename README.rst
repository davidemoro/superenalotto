superenalotto
=============

Dato un file ``colonne.txt`` (per ogni riga i numeri da selezionare in ciascun pannello). Esempio::

    1 2 3 4 5 6
    1 2 3 4 5 7
    1 2 3 4 5 8
    1 2 3 4 5 9
    1 2 3 4 5 10
    1 2 3 4 5 11

genererà un file ``schedina.pdf`` pronto da stampare (una pagina per ogni schedina, quindi 5 colonne per schedina).

Come installare::

    pip install -r requirements.txt

Aiuto in linea::

    python superenalotto.py generate --help

Utilizzo::

    python superenalotto.py generate --input_path colonne.txt --output_path schedina.pdf

Ecco un esempio di schedina stampata:

.. image:: https://raw.githubusercontent.com/davidemoro/superenalotto/master/static/schedina.jpeg
