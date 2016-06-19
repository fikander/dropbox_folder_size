# What it is

Simple tool to print sizes of Dropbox folders sorted by size.

# Usage (virtualenv)

First, generate Dropbox access token: https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/

	virtualenv venv
	. venv/bin/activate
	cd dropbox-folder-size
	python setup.py install

To get folder sizes, in command line:

	export DROPBOX_TOKEN=[token] && python dropbox_folder_size/main.py

Or in python console:

	> from dropbox_folder_size import FolderSize
	> f = FolderSize('<DROPBOX_TOKEN>')
	> f.get_sizes()

# Usage (Docker)

Create .env file in dropbox-folder-size directory with:

	echo DROPBOX_TOKEN=[token] > .env

Build Docker image with:

	docker-compose build

Run with:

	docker-compose up

(Note it may take a while for Dropbox accounts with lots of files)

# Development

## Docker

You may want to add following to map source folder inside container:

    volumes:
        - [HOST_FOLDER]/dropbox-folder-size/src:/home/dropbox-folder-size/src

To run container:

	docker-compose up

## virtualenv

Install package in development mode (create symlink to source):

	python setup.py develop

