# File Duplications Finder

This is a Python application that helps you find and delete duplicate files in a selected directory. The application presents a user-friendly interface and allows you to interact with the file system conveniently. This application relies solely on built-in Python libraries, meaning there are no third-party dependencies.

## Features

1. Select a folder to scan for duplicate files.
2. Display a list of duplicate files along with their details (hash, creation date, size).
3. Delete selected files from the list.

## Files

The project consists of the following files:

- `app.py`: Contains the main application class `App` which controls the running of the application.

- `file_storage.py`: Defines the `FileStorage` class that is responsible for scanning a provided directory path for files and finding duplicate files.

- `file.py`: Defines the `File` class that represents a file in the file system with various methods for retrieving file information and performing actions on the file.

- `ui.py`: Implements the `UI` class for the graphical user interface of the application using the Tkinter library.

- `utils.py`: Provides utility functions for timing function execution and converting file sizes to a human-readable format.

- `.gitignore`: Specifies the files and directories that Git should ignore.

- `settings.py` and `settings.ex.json`: Used for storing and managing the settings for the application.

## Usage

To run the application, simply execute the `app.py` file:

```sh
python app.py
```

A window will appear, allowing you to select a folder, scan for duplicate files, and delete selected files.

## Dependencies

This application was written in pure Python and uses only built-in libraries. No third-party dependencies are needed.

## Note

This application uses the MD5 hash of file content to identify duplicate files. It is designed to work with the directory structure and does not modify the file system outside the scope of its functionalities.

---


# Поиск Дубликатов Файлов

Это приложение на Python помогает вам находить и удалять дублирующиеся файлы в выбранной директории. Приложение представляет собой удобный интерфейс и позволяет вам удобно взаимодействовать с файловой системой. Это приложение полностью основано на встроенных библиотеках Python, то есть не требует сторонних зависимостей.

## Возможности

1. Выберите папку для сканирования на наличие дубликатов файлов.
2. Отображение списка дубликатов файлов вместе с их деталями (хэш, дата создания, размер).
3. Удалите выбранные файлы из списка.

## Файлы

Проект состоит из следующих файлов:

- `app.py`: Содержит главный класс приложения `App`, который контролирует работу приложения.

- `file_storage.py`: Определяет класс `FileStorage`, который отвечает за сканирование указанного каталога на наличие файлов и поиск дубликатов файлов.

- `file.py`: Определяет класс `File`, который представляет собой файл в файловой системе с различными методами для получения информации о файле и выполнения действий над файлом.

- `ui.py`: Реализует класс `UI` для графического интерфейса приложения с использованием библиотеки Tkinter.

- `utils.py`: Предоставляет вспомогательные функции для измерения времени выполнения функции и преобразования размеров файлов в удобочитаемый формат.

- `.gitignore`: Указывает файлы и директории, которые Git должен игнорировать.

- `settings.py` и `settings.ex.json`: Используется для хранения и управления настройками приложения.

## Использование

Чтобы запустить приложение, просто выполните файл `app.py`:

```sh
python app.py
```

Появится окно, которое позволит вам выбрать папку, просканировать на наличие дубликатов файлов и удалить выбранные файлы.

## Зависимости

Это приложение было написано на чистом Python и использует только встроенные библиотеки. Никаких сторонних зависимостей не требуется.

## Примечание

Это приложение использует хэш MD5 содержимого файла для идентификации дубликатов файлов. Он разработан для работы со структурой каталогов и не изменяет файловую систему за пределами своих функций. 

---

Generated with ChatGPT :)