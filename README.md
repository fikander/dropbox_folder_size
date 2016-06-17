# What it is

Simple tool to print sizes of Dropbox folders sorted by size.

# Usage

Create .env file with:

	DROPBOX_TOKEN=[token]

Build Docker image with:

	docker-compose build

Run with:

	docker-compose up

(Note it may take a while for Dropbox accounts with lots of files)

# Development

You may want to add following to map source folder inside container:

    volumes:
        - [HOST_FOLDER]/dropbox-folder-size/src:/home/dropbox-folder-size/src
