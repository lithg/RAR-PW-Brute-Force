# Uso: btn.setStyleSheet(style.styleBtn) 

styleCheckRed = "QCheckBox::indicator {width: 30px;height: 30px;border-radius: 7px;}QCheckBox:indicator:checked {background-color:   red;border:   2px solid white;} QCheckBox::indicator:unchecked {image: url(img/red_d.png);border:   2px solid white;}"

styleCheckBlue = "QCheckBox::indicator {width: 30px;height: 30px;border-radius: 7px;}QCheckBox:indicator:checked {background-color:   blue;border:   2px solid white;} QCheckBox::indicator:unchecked {image: url(img/nao.png);border:   2px solid white;}"

styleCheckGreen = "QCheckBox::indicator {width: 30px;height: 30px;border-radius: 7px;}QCheckBox:indicator:checked {image: url(img/sim.png);border:   2px solid white;} QCheckBox::indicator:unchecked {image: url(img/nao.png);border:   2px solid white;}"

styleCheckYellow = "QCheckBox::indicator {width: 10px;height: 10px;border-radius: 7px;}QCheckBox:indicator:checked {background-color:   yellow;border:   2px solid white;} QCheckBox::indicator:unchecked {image: url(img/yellow_d.png);border:   2px solid white;}"

styleBtnDisabled = "font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 8px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A9A9A9, stop: 1 #D3D3D3)}"

styleBtn = "font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 8px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);"

styleOpen = "background-image: url('open.png'); border: none;"

tabStyle = "QTabBar::tab {\nbackground: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\nborder: 2px solid #C4C4C3;\nborder-bottom-color: #C2C7CB; /* same as the pane color */\nborder-top-left-radius: 4px;\nborder-top-right-radius: 4px;\nmin-width: 8ex;\npadding: 2px;\n}\nQTabBar::tab:selected, QTabBar::tab:hover {\nbackground: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n}\nQTabBar::tab:selected {\nborder-color: #9B9B9B;\nborder-bottom-color: #C2C7CB; /* same as pane color */\ncolor: white;\nbackground-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);\n\n}\nQTabBar::tab:!selected {\nmargin-top: 2px; /* make non-selected tabs look smaller */\ncolor: white;\nbackground-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c4daff, stop: 1 #9dbdf2);\n}"
