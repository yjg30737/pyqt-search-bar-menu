# pyqt-search-bar-menu
PyQt QMenu which contains auto search bar as first item

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-search-bar-menu`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-auto-search-bar.git">pyqt-instant-search-bar</a> - Search bar at the top

## Feature
* Search bar is at the very top of the menu, let user search `QAction`'s text. At this time menu list works like a completer.   

## Examples
### Simple Code Sample
```python
searchBarMenu = SearchBarMenu('Menu', self)
searchBarMenu.addAction('Action')
```
### Executable Code Sample
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

### Result

![image](https://user-images.githubusercontent.com/55078043/155654071-0569381a-e319-468a-aac9-716307c20821.png)

