def test_schedina(tmpdir):
    from superenalotto import print_file
    colonne_file = tmpdir.join('colonne.txt')
    colonne_file.write_text("""1 2 3 4 5 6
1 2 3 4 5 7""", encoding='utf-8')
    output_file = tmpdir.join('output.pdf')
    print_file(filepath=colonne_file.strpath, outputpath=output_file.strpath)
    assert output_file.exists() is True
