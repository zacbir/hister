import click


@click.group()
def cli():
    pass


@click.command()
def save():
    pass


@click.command()
@click.argument('term')
def search(term):
    pass


@click.command()
@click.argument('doc_id')
def rm(doc_id):
    pass


@click.command()
@click.argument('date')
def seen(date):
    pass


@click.command()
@click.argument('doc_id')
@click.argument('annotation')
def anno(doc_id, annotation):
    pass


@click.command()
@click.option('--format', default='json', help='Format for history output')
@click.option('--date', default='all', help='Date to export')
def export(format):
    pass


cli.add_command(save)
cli.add_command(search)
cli.add_command(rm)
cli.add_command(seen)
cli.add_command(anno)
cli.add_command(export)

