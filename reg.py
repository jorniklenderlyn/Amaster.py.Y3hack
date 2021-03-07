from PyQt5 import QtWidgets
import sqlite3
import sys


con = sqlite3.connect('db.db3')
cur = con.cursor()


def add_user(name, fname):
    file = open(fname, 'rb')
    cur.execute('INSERT INTO users (name, photo, score) VALUES (?, ?, 0)',
                (name, file.read()))
    con.commit()


def get_users():
    return list(cur.execute('SELECT id, name FROM users'))


def name_is_used(name):
    cur = con.execute('SELECT * FROM users WHERE name = ?', (name, ))
    row = cur.fetchone()
    if row:
        return True
    return False


def update_user_best_score(user_id, game_id, score):
    cur.execute('UPDATE opened_games SET score = ? WHERE user_id = ? AND game_id = ?',
                (score, user_id, game_id))
    con.commit()


def get_user_best_score(user_id):
    score = cur.execute('SELECT game_id, score FROM opened_games WHERE user_id = ?', (user_id, )).fetchall()
    score.sort()
    return score


def get_user_opened_games(user_id):
    games = [x[0] for x in get_user_best_score(user_id)]
    return games


def open_user_game(user_id, game_id):
    if game_id not in get_user_opened_games(user_id):
        cur.execute('INSERT INTO opened_games (user_id, game_id, score) VALUES (?, ?, 0)',
                    (user_id, game_id))
        con.commit()


class RegWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.data = []
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)
        self.lst = QtWidgets.QListWidget(self)
        self.lst.doubleClicked.connect(self.join)
        layout.addWidget(self.lst, 0, 0, 1, 2)
        self.loadList()
        join_btn = QtWidgets.QPushButton('Войти', self)
        join_btn.clicked.connect(self.join)
        layout.addWidget(join_btn, 1, 0, 1, 1)
        add_btn = QtWidgets.QPushButton('Добавить пользователя', self)
        add_btn.clicked.connect(self.add)
        layout.addWidget(add_btn, 1, 1, 1, 1)
        self.app = app

        join_btn.setObjectName('join_but')
        add_btn.setObjectName('add_but')

    def loadList(self):
        self.lst.clear()
        self.data = get_users()
        for i in self.data:
            self.lst.addItem(i[1])

    def join(self, sender):
        global app
        if sender:
            i = sender.row()
            user_data = self.data[i]
        else:
            i = self.lst.selectedIndexes()
            if not i:
                return
            else:
                i = i[0].row()
            user_data = self.data[i]
        self.close()
        # Здесь вызов игры, id пользователя - user_data[0]

    def add(self):
        ui = QtWidgets.QInputDialog()
        name, ok = ui.getText(self, "Новый пользователь", 'Введите ваше имя:')
        name = name.strip()
        if ok and name:
            if not name_is_used(name):
                try:
                    add_user(name, "data/chel.png")
                    cur = con.execute("SELECT id FROM users WHERE name = ?", (name,))
                    user = cur.fetchone()[0]
                    open_user_game(user, 1)
                    update_user_best_score(user, 1, 1)
                    self.loadList()
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(
        """
QPushButton#join_but{
    background: #A2D8AF;
}
QPushButton#add_but{
    background: #E3B3C8;
}
RegWindow {
    background: #E8F2C6;
}
QLineEdit {
    width: 300px;
    font-size: 13px;
    padding: 6px 0 4px 10px;
    border: 1px solid #cecece;
    background: #F6F6f6;
    border-radius: 8px;
}
QPushButton {
    background-color: gainsboro;
    border-style: silver;
    border-width: 4px;
    border-radius: 10px;
    border-color: beige;
    min-width: 10em;
    padding: 6px;
    box-shadow: inset 0 20px 20px red;
}
QPushButton:pressed {
    background-color: darkgrey;
}
QPushButton:hover {
    margin-top: 1px;
	margin-bottom: -1px;
	zoom: 1;
}
%
        """
    )
    ex = RegWindow(app)
    ex.show()
    sys.exit(app.exec_())