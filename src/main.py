import os
from dropbox.client import DropboxClient
from collections import defaultdict


def print_sizes(client):
    sizes = {}
    cursor = None
    while cursor is None or result['has_more']:
        result = client.delta(cursor)
        for path, metadata in result['entries']:
            sizes[path] = metadata['bytes'] if metadata else 0
            # print('%s: %d' % (path, sizes[path]))
        cursor = result['cursor']

    foldersizes = defaultdict(lambda: 0)
    for path, size in sizes.items():
        segments = path.split('/')
        for i in range(1, len(segments)):
            folder = '/'.join(segments[:i])
            if folder == '': folder = '/'
            foldersizes[folder] += size

    for folder in reversed(sorted(foldersizes.keys(), key=lambda x: foldersizes[x])):
        print('%s: %d' % (folder, foldersizes[folder]))


if __name__ == '__main__':
    token = os.getenv('DROPBOX_TOKEN')
    client = DropboxClient(token)
    print_sizes(client)
