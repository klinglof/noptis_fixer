import pathlib
import tempfile
import zipfile

import requests
import tqdm
import werkzeug.http


def download_schema(destination: pathlib.Path):
    real_time_output_interface_3_0_url = (
        'https://www.noptis.com/download/real-time-output-interface-3-0/'
        '?wpdmdl=297&refresh=651ba7ab4d9851696311211')
    response = requests.get(real_time_output_interface_3_0_url, stream=True)
    _, options = werkzeug.http.parse_options_header(
        response.headers['content-disposition'])
    with tempfile.TemporaryDirectory() as temp_dir, tqdm.tqdm.wrapattr(
            open(pathlib.Path(temp_dir, options['filename']), "wb"),
            "write",
            miniters=1,
            desc='Real-time Output Interface 3.0',
            total=int(response.headers.get('content-length', 0))) as file:
        for chunk in response.iter_content(chunk_size=4096):
            file.write(chunk)
        file.close()
        unzip_file(pathlib.Path(temp_dir, options['filename']), destination)


def unzip_file(target: pathlib.Path, destination=pathlib.Path('temp', 'raw')):
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(file=target, mode='r') as file:
        file.extractall(path=destination)


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as temp:
        download_schema(pathlib.Path(temp))
