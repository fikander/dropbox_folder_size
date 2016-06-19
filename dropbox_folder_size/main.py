import os
from folder_size import FolderSize

if __name__ == '__main__':
    token = os.getenv('DROPBOX_TOKEN')
    fs = FolderSize(token)
    print('scanning folders...')
    foldersizes = fs.get_sizes()
    for folder in reversed(sorted(foldersizes.keys(), key=lambda x: foldersizes[x])):
        print('%s: %d' % (folder, foldersizes[folder]))
