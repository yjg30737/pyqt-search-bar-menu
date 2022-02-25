from PyQt5.QtWidgets import QMenu, QWidgetAction, QAction


class SearchBarMenu(QMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__actions = []
        self.__initUi()

    def __initUi(self):
        searchBar = SearchBar()
        searchLineEdit = searchBar.getSearchBar()
        searchLineEdit.textChanged.connect(self.__searchLineEditTextChanged)
        searchAction = QWidgetAction(self)
        searchAction.setDefaultWidget(searchBar)
        self.addAction(searchAction)

    def addAction(self, action: QAction) -> None:
        super().addAction(action)
        if action in self.__actions:
            pass
        else:
            self.__actions.append(self.actions()[-1])

    def __searchLineEditTextChanged(self, text):
        actions = self.__actions[1:]
        if text.strip() != '':
            for action in actions:
                action_text = action.text()
                if action_text.startswith(text):
                    if action.isVisible():
                        pass
                    else:
                        action.setVisible(True)
                else:
                    action.setVisible(False)
        else:
            for action in actions:
                action.setVisible(True)