import zipfile
import pathlib

def make_archive(files, folder):
    folder_path = pathlib.Path(folder, 'archive.zip')
    with zipfile.ZipFile(folder_path, 'w') as archive:
        for file in files:
            path = pathlib.Path(file)
            archive.write(file, arcname=path.name)


if __name__ == "__main__":
    make_archive(files=['017.0_Day17Files/017.0.1_Day17Data.txt'], folder='017.0_Day17Files')