import click

from superenalotto import print_file


@click.group()
def cli():
    pass


@cli.command()
@click.option('--input_path')
@click.option('--output_path')
def generate(input_path, output_path):
    print_file(filepath=input_path, outputpath=output_path)


cli = click.CommandCollection(sources=[cli])

if __name__ == '__main__':
    cli()
