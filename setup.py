from setuptools import setup, find_packages
from me7_ba11.__version__ import __version__
from pathlib import Path

packages = \
['me7_ba11',
 'me7_ba11.config',
 'me7_ba11.encrypt',
 'me7_ba11.manage',
 'me7_ba11.structs']

package_data = \
{'': ['*']}
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name                = 'me7_ba11',
    version             = __version__,
    description         = 'light file management lib for line ctf 2022',
    long_description    = long_description,
    long_description_content_type = 'text/markdown',
    author              = 'jiho.park',
    author_email        = 'wulfsek@gmail.com',
    url                 = 'https://github.com/ppkill00/meat_ball',
    download_url        = 'https://github.com/ppkill00/meat_ball/archive/master.zip',
    install_requires    = [],
    license             = 'MIT',
    packages            = packages,
    keywords            = ['pypi me7_ba11'],
    python_requires     = '>=3',
    package_data        = package_data,
    zip_safe            = False,
    classifiers         = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)