from setuptools import setup

setup(name='dropbox_folder_size',
      version='0.1',
      description='Show Dropbox folder sizes',
      url='https://github.com/fikander/dropbox-folder-size',
      author='Tomasz Kustrzynski',
      author_email='tomasz.kustrzynski@gmail.com',
      license='MIT',
      packages=['dropbox_folder_size'],
      install_requires=[
          'dropbox>=6.4.0',
      ],
      zip_safe=False)
