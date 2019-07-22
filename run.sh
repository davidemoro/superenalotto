#!/usr/bin/env bash
python/bin/python superenalotto.py generate --input_path colonne.txt --output_path schedina.pdf
/usr/bin/firefox schedina.pdf &