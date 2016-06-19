from dropbox.client import DropboxClient
from collections import defaultdict

class FolderSize:

    def __init__(self, dropbox_token):
        self.token = dropbox_token
        self.client = DropboxClient(self.token)

    def get_sizes(self):
        sizes = {}
        cursor = None
        while cursor is None or result['has_more']:
            result = self.client.delta(cursor)
            for path, metadata in result['entries']:
                sizes[path] = metadata['bytes'] if metadata else 0
            cursor = result['cursor']

        foldersizes = defaultdict(lambda: 0)
        for path, size in sizes.items():
            segments = path.split('/')
            for i in range(1, len(segments)):
                folder = '/'.join(segments[:i])
                if folder == '': folder = '/'
                foldersizes[folder] += size

        return foldersizes
