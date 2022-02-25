# pyqt-search-bar-menu
PyQt QMenu which contains search bar as first item

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-search-bar-menu.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-search-bar.git">pyqt-search-bar</a>

## Examples
Code Sample
```python
from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqt_search_bar_menu import SearchBarMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')

        searchBarMenu = SearchBarMenu('A Bunch of Actions', self)

        for i in range(5):
            action = searchBarMenu.addAction(f'Action{i+1}')

        filemenu.addMenu(searchBarMenu)

        menubar.addMenu(filemenu)
        self.setMenuBar(menubar)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/155634888-eed734ca-978b-484c-91f5-5f2c37669fca.png)

