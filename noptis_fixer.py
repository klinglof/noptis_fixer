import pathlib
import tempfile

import click

import download
import fix_file_errors


@click.command()
@click.option('--schema-path',
              type=click.Path(exists=True, file_okay=False, resolve_path=True),
              help=('Folder root path to xml schema files. '
                    'Will download schema from Noptis if omitted.'))
@click.option(
    '--destination',
    default='temp/fixed',
    type=click.Path(exists=False, file_okay=False, resolve_path=True),
    help='Where the fixed schema files will be saved. Example: temp/fixed',
)
@click.option(
    '--destination-lib',
    default='temp.noptis',
    help='Module path to generated python library to. Example: temp.noptis',
)
@click.option(
    '--make-pretty',
    is_flag=True,
    default=False,
    help='If generated code should be formatted.',
)
def cli(schema_path, destination, destination_lib, make_pretty):
    """Generates fixed ROI schema files from Noptis."""
    if schema_path is None:
        with tempfile.TemporaryDirectory() as temp_dir:
            download.download_schema(pathlib.Path(temp_dir))
            fix_file_errors.apply_fixes(
                schema_root_path=pathlib.Path(temp_dir),
                fix_path=pathlib.Path(destination))
    if schema_path:
        fix_file_errors.apply_fixes(schema_root_path=pathlib.Path(schema_path),
                                    fix_path=pathlib.Path(destination))
    fix_file_errors.generate_library(
        fixed_files_path=pathlib.Path(destination),
        package_name=destination_lib,
        make_pretty=make_pretty)


if __name__ == '__main__':
    cli()
