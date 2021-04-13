#!/usr/bin/env python3
import os
import pathlib

PATH = pathlib.Path().absolute()

class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def main():
    # Listar todos los directorios y subdirectorios desde donde se ejecuta 
    files = list_files()
    # Crear carpeta con los tipos de archivos a organizar
    create_organized_directory()
    # Copiar archivos en la carpeta organizada

    for file in files:
        print(file)


def list_files():
    files_list = []

    for path, _, files in os.walk(PATH): 
        for file in files:
            files_list.append(File(file, path))

    return files_list


def create_organized_directory():
    os.mkdir(os.path.join(PATH,"organized"))


if __name__ == '__main__':
    main()
    