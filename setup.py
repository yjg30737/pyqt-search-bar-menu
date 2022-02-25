from setuptools import setup, find_packages

setup(
    name='pyqt-search-bar-menu',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QMenu which contains search bar as first item',
    url='https://github.com/yjg30737/pyqt-search-bar-menu.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-auto-search-bar @ git+https://git@github.com/yjg30737/pyqt-auto-search-bar.git@main'
    ]
)