from PyQt5 import QtCore, QtGui, QtWidgets
from database_load import *
from datetime import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.database_table = QtWidgets.QTableWidget(self.centralwidget)
        self.database_table.setGeometry(QtCore.QRect(430, 20, 671, 341))
        self.database_table.setRowCount(10)
        self.database_table.setColumnCount(10)
        self.database_table.setObjectName("database_table")
        self.filter_selections = QtWidgets.QLabel(self.centralwidget)
        self.filter_selections.setGeometry(QtCore.QRect(60, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filter_selections.setFont(font)
        self.filter_selections.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_selections.setObjectName("filter_selections")
        self.title_filter = QtWidgets.QLabel(self.centralwidget)
        self.title_filter.setGeometry(QtCore.QRect(30, 80, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_filter.setFont(font)
        self.title_filter.setObjectName("title_filter")
        self.company_filter = QtWidgets.QLabel(self.centralwidget)
        self.company_filter.setGeometry(QtCore.QRect(30, 120, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.company_filter.setFont(font)
        self.company_filter.setObjectName("company_filter")
        self.tags_filter = QtWidgets.QLabel(self.centralwidget)
        self.tags_filter.setGeometry(QtCore.QRect(30, 240, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tags_filter.setFont(font)
        self.tags_filter.setObjectName("tags_filter")
        self.location_filter = QtWidgets.QLabel(self.centralwidget)
        self.location_filter.setGeometry(QtCore.QRect(30, 200, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.location_filter.setFont(font)
        self.location_filter.setObjectName("location_filter")
        self.description_filter = QtWidgets.QLabel(self.centralwidget)
        self.description_filter.setGeometry(QtCore.QRect(30, 160, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.description_filter.setFont(font)
        self.description_filter.setObjectName("description_filter")
        self.publication_date_filter = QtWidgets.QLabel(self.centralwidget)
        self.publication_date_filter.setGeometry(QtCore.QRect(30, 270, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.publication_date_filter.setFont(font)
        self.publication_date_filter.setObjectName("publication_date_filter")
        self.remote_filter = QtWidgets.QLabel(self.centralwidget)
        self.remote_filter.setGeometry(QtCore.QRect(30, 320, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remote_filter.setFont(font)
        self.remote_filter.setObjectName("remote_filter")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(250, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.date_added_to_db = QtWidgets.QLabel(self.centralwidget)
        self.date_added_to_db.setGeometry(QtCore.QRect(30, 370, 261, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_added_to_db.setFont(font)
        self.date_added_to_db.setObjectName("date_added_to_db")
        self.display_box = QtWidgets.QTextEdit(self.centralwidget)
        self.display_box.setGeometry(QtCore.QRect(10, 400, 1091, 451))
        self.display_box.setObjectName("display_box")
        self.job_title_box = QtWidgets.QLabel(self.centralwidget)
        self.job_title_box.setGeometry(QtCore.QRect(20, 430, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.job_title_box.setFont(font)
        self.job_title_box.setObjectName("job_title_box")
        self.description_box = QtWidgets.QLabel(self.centralwidget)
        self.description_box.setGeometry(QtCore.QRect(720, 410, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.description_box.setFont(font)
        self.description_box.setObjectName("description_box")
        self.company_name_box = QtWidgets.QLabel(self.centralwidget)
        self.company_name_box.setGeometry(QtCore.QRect(20, 480, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.company_name_box.setFont(font)
        self.company_name_box.setObjectName("company_name_box")
        self.location_box = QtWidgets.QLabel(self.centralwidget)
        self.location_box.setGeometry(QtCore.QRect(20, 540, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.location_box.setFont(font)
        self.location_box.setObjectName("location_box")
        self.tags_box = QtWidgets.QLabel(self.centralwidget)
        self.tags_box.setGeometry(QtCore.QRect(20, 600, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tags_box.setFont(font)
        self.tags_box.setObjectName("tags_box")
        self.publication_date_box = QtWidgets.QLabel(self.centralwidget)
        self.publication_date_box.setGeometry(QtCore.QRect(20, 660, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.publication_date_box.setFont(font)
        self.publication_date_box.setObjectName("publication_date_box")
        self.remote_box = QtWidgets.QLabel(self.centralwidget)
        self.remote_box.setGeometry(QtCore.QRect(20, 720, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remote_box.setFont(font)
        self.remote_box.setObjectName("remote_box")
        self.date_added_to_db_box = QtWidgets.QLabel(self.centralwidget)
        self.date_added_to_db_box.setGeometry(QtCore.QRect(20, 780, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_added_to_db_box.setFont(font)
        self.date_added_to_db_box.setObjectName("date_added_to_db_box")
        self.job_title_display = QtWidgets.QTextEdit(self.centralwidget)
        self.job_title_display.setGeometry(QtCore.QRect(120, 410, 291, 41))
        self.job_title_display.setObjectName("job_title_display")
        self.company_name__display = QtWidgets.QTextEdit(self.centralwidget)
        self.company_name__display.setGeometry(QtCore.QRect(120, 470, 291, 41))
        self.company_name__display.setObjectName("company_name__display")
        self.location_display = QtWidgets.QTextEdit(self.centralwidget)
        self.location_display.setGeometry(QtCore.QRect(120, 530, 291, 41))
        self.location_display.setObjectName("location_display")
        self.tags_display = QtWidgets.QTextEdit(self.centralwidget)
        self.tags_display.setGeometry(QtCore.QRect(120, 590, 291, 41))
        self.tags_display.setObjectName("tags_display")
        self.pub_date_display = QtWidgets.QTextEdit(self.centralwidget)
        self.pub_date_display.setGeometry(QtCore.QRect(120, 650, 291, 41))
        self.pub_date_display.setObjectName("pub_date_display")
        self.remote_display = QtWidgets.QTextEdit(self.centralwidget)
        self.remote_display.setGeometry(QtCore.QRect(120, 710, 51, 41))
        self.remote_display.setObjectName("remote_display")
        self.date_added_to_db_display = QtWidgets.QTextEdit(self.centralwidget)
        self.date_added_to_db_display.setGeometry(QtCore.QRect(160, 770, 251, 41))
        self.date_added_to_db_display.setObjectName("date_added_to_db_display")
        self.description_display = QtWidgets.QTextEdit(self.centralwidget)
        self.description_display.setGeometry(QtCore.QRect(420, 430, 671, 411))
        self.description_display.setObjectName("description_display")
        self.pub_date_input = QtWidgets.QComboBox(self.centralwidget)
        self.pub_date_input.setGeometry(QtCore.QRect(260, 280, 111, 22))
        self.pub_date_input.setObjectName("pub_date_input")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.pub_date_input.addItem("")
        self.remote_input = QtWidgets.QComboBox(self.centralwidget)
        self.remote_input.setGeometry(QtCore.QRect(80, 320, 91, 22))
        self.remote_input.setObjectName("remote_input")
        self.remote_input.addItem("")
        self.remote_input.addItem("")
        self.remote_input.addItem("")
        self.job_title_input = QtWidgets.QTextEdit(self.centralwidget)
        self.job_title_input.setGeometry(QtCore.QRect(140, 70, 231, 31))
        self.job_title_input.setObjectName("job_title_input")
        self.company_name_input = QtWidgets.QTextEdit(self.centralwidget)
        self.company_name_input.setGeometry(QtCore.QRect(140, 110, 231, 31))
        self.company_name_input.setObjectName("company_name_input")
        self.description_input = QtWidgets.QTextEdit(self.centralwidget)
        self.description_input.setGeometry(QtCore.QRect(140, 150, 231, 31))
        self.description_input.setObjectName("description_input")
        self.location_input = QtWidgets.QTextEdit(self.centralwidget)
        self.location_input.setGeometry(QtCore.QRect(140, 190, 231, 31))
        self.location_input.setObjectName("location_input")
        self.tags_input = QtWidgets.QTextEdit(self.centralwidget)
        self.tags_input.setGeometry(QtCore.QRect(200, 230, 171, 31))
        self.tags_input.setObjectName("tags_input")
        self.date_added_to_db_input = QtWidgets.QComboBox(self.centralwidget)
        self.date_added_to_db_input.setGeometry(QtCore.QRect(300, 370, 111, 22))
        self.date_added_to_db_input.setObjectName("date_added_to_db_input")
        self.date_added_to_db_input.addItem("")
        self.date_added_to_db_input.addItem("")
        self.date_added_to_db_input.addItem("")
        self.date_added_to_db_input.addItem("")
        self.date_added_to_db_input.addItem("")
        self.date_added_to_db_input.addItem("")
        self.job_id_box = QtWidgets.QLabel(self.centralwidget)
        self.job_id_box.setGeometry(QtCore.QRect(200, 720, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.job_id_box.setFont(font)
        self.job_id_box.setObjectName("job_id_box")
        self.job_id_display = QtWidgets.QTextEdit(self.centralwidget)
        self.job_id_display.setGeometry(QtCore.QRect(250, 710, 161, 41))
        self.job_id_display.setObjectName("job_id_display")
        self.job_id_filter = QtWidgets.QLabel(self.centralwidget)
        self.job_id_filter.setGeometry(QtCore.QRect(190, 320, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.job_id_filter.setFont(font)
        self.job_id_filter.setObjectName("job_id_filter")
        self.job_id_input = QtWidgets.QTextEdit(self.centralwidget)
        self.job_id_input.setGeometry(QtCore.QRect(240, 310, 131, 31))
        self.job_id_input.setObjectName("job_id_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 21))
        self.menubar.setObjectName("menubar")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_Database = QtWidgets.QAction(MainWindow)
        self.actionCreate_Database.setObjectName("actionCreate_Database")
        self.actionView_Database = QtWidgets.QAction(MainWindow)
        self.actionView_Database.setObjectName("actionView_Database")
        self.actionUpdate_Database = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Database.setObjectName("actionUpdate_Database")
        self.actionClear_Database_and_Repopulate = QtWidgets.QAction(MainWindow)
        self.actionClear_Database_and_Repopulate.setObjectName("actionClear_Database_and_Repopulate")
        self.menuActions.addAction(self.actionCreate_Database)
        self.menuActions.addAction(self.actionView_Database)
        self.menuActions.addAction(self.actionUpdate_Database)
        self.menuActions.addAction(self.actionClear_Database_and_Repopulate)
        self.menubar.addAction(self.menuActions.menuAction())

        self.job_title_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.company_name__display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.location_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.tags_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.pub_date_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.remote_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.date_added_to_db_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.description_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.display_box.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.database_table.verticalHeader().setDefaultSectionSize(100)

        self.database_table.setHorizontalHeaderLabels(('job id, title, company, description, location, tags, '
                                                       'publication_date, remote, datetime_added_to_database, '
                                                       'pub_date_modified').split(', '))

        # adds actions to menu buttons
        self.actionCreate_Database.triggered.connect(self.create_database_on_click)
        self.actionView_Database.triggered.connect(self.view_database_on_click)
        self.actionClear_Database_and_Repopulate.triggered.connect(self.clear_database_and_repopulate_on_click)
        self.actionUpdate_Database.triggered.connect(self.update_database_on_click)

        # adds action to search button
        self.search.clicked.connect(self.search_database_clicked)

        self.database_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.database_table.clicked.connect(self.view_row_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filter_selections.setText(_translate("MainWindow", "Job Filter Selections"))
        self.title_filter.setText(_translate("MainWindow", "Job Title"))
        self.company_filter.setText(_translate("MainWindow", "Company Name"))
        self.tags_filter.setText(_translate("MainWindow", "Tags (only allows one word)"))
        self.location_filter.setText(_translate("MainWindow", "Location"))
        self.description_filter.setText(_translate("MainWindow", "Description"))
        self.publication_date_filter.setText(_translate("MainWindow", "Publication Date (how many days ago)"))
        self.remote_filter.setText(_translate("MainWindow", "Remote "))
        self.search.setText(_translate("MainWindow", "Search"))
        self.date_added_to_db.setText(_translate("MainWindow", "Date added to database (how many days ago)"))
        self.job_title_box.setText(_translate("MainWindow", "Job Title"))
        self.description_box.setText(_translate("MainWindow", "Description"))
        self.company_name_box.setText(_translate("MainWindow", "Company Name"))
        self.location_box.setText(_translate("MainWindow", "Location"))
        self.tags_box.setText(_translate("MainWindow", "Tags"))
        self.publication_date_box.setText(_translate("MainWindow", "Publication Date"))
        self.remote_box.setText(_translate("MainWindow", "Remote (yes/no)"))
        self.date_added_to_db_box.setText(_translate("MainWindow", "Date added to database"))
        self.pub_date_input.setItemText(0, _translate("MainWindow", "Include all dates"))
        self.pub_date_input.setItemText(1, _translate("MainWindow", "1"))
        self.pub_date_input.setItemText(2, _translate("MainWindow", "5"))
        self.pub_date_input.setItemText(3, _translate("MainWindow", "10"))
        self.pub_date_input.setItemText(4, _translate("MainWindow", "15"))
        self.pub_date_input.setItemText(5, _translate("MainWindow", "20"))
        self.pub_date_input.setItemText(6, _translate("MainWindow", "30"))
        self.pub_date_input.setItemText(7, _translate("MainWindow", "60"))
        self.remote_input.setItemText(0, _translate("MainWindow", "N/A"))
        self.remote_input.setItemText(1, _translate("MainWindow", "Yes"))
        self.remote_input.setItemText(2, _translate("MainWindow", "No"))
        self.date_added_to_db_input.setItemText(0, _translate("MainWindow", "Include all dates"))
        self.date_added_to_db_input.setItemText(1, _translate("MainWindow", "1"))
        self.date_added_to_db_input.setItemText(2, _translate("MainWindow", "5"))
        self.date_added_to_db_input.setItemText(3, _translate("MainWindow", "10"))
        self.date_added_to_db_input.setItemText(4, _translate("MainWindow", "15"))
        self.date_added_to_db_input.setItemText(5, _translate("MainWindow", "20"))
        self.job_id_box.setText(_translate("MainWindow", "Job ID"))
        self.job_id_filter.setText(_translate("MainWindow", "Job ID"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionCreate_Database.setText(_translate("MainWindow", "Create Database"))
        self.actionView_Database.setText(_translate("MainWindow", "View Database"))
        self.actionUpdate_Database.setText(_translate("MainWindow", "Update Database "))
        self.actionClear_Database_and_Repopulate.setText(_translate("MainWindow", "Clear Database and Repopulate"))
        self.database_table.setColumnHidden(9, True)

# gets the jobs from the feed that were not added to the database since the last update and only shows them in the table
    def update_database_on_click(self):
        try:

            connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
            last_datetime_updated = "SELECT date_added_to_db from jobs ORDER by date_added_to_db desc LIMIT 1"
            last_datetime_updated_result = connection.execute(last_datetime_updated).fetchone()
            last_datetime_updated_result = last_datetime_updated_result[0]

            load_feed()

            current_date_time = datetime.now()
            current_date_time = current_date_time.strftime("%Y-%m-%d %H:%M")
            current_date_time = str(current_date_time)

            jobs_since_last_update = "SELECT * from jobs WHERE date_added_to_db > ? AND date_added_to_db <= ?"
            jobs_since_last_update_result = connection.execute(jobs_since_last_update, [last_datetime_updated_result,
                                                                                        current_date_time])

            self.database_table.setRowCount(0)

            # adds the data from the job table to the table GUI and views the table to the user
            for row_number, row_data in enumerate(jobs_since_last_update_result):
                self.database_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.database_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            connection.close()
        except BaseException as error:
            print(error)

# creates the database and table
    @staticmethod
    def create_database_on_click():
        load_feed()

# allows the user to see the entire job table on the GUI
    def view_database_on_click(self):
        try:
            connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
            query = "SELECT * FROM jobs"
            result = connection.execute(query)

            self.database_table.setRowCount(0)

            # adds the data from the job table to the table GUI and views the table to the user
            for row_number, row_data in enumerate(result):
                self.database_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.database_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            connection.close()
        except BaseException as error:
            print(error)

# clears the job table from the database and repopulates it with new data from the fee
    def clear_database_and_repopulate_on_click(self):
        try:
            connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
            last_publication_date = "SELECT publication_date_modified from jobs " \
                                    "ORDER by publication_date_modified desc LIMIT 1"
            last_publication_date = connection.execute(last_publication_date).fetchone()
            last_publication_date = str(last_publication_date[0])

            query = "DELETE FROM jobs"
            connection.execute(query)
            connection.commit()
            load_feed()
            load_after_delete(last_publication_date)

            query = "SELECT * FROM jobs"
            result = connection.execute(query)

            self.database_table.setRowCount(0)

            # adds the data from the job table to the table GUI and views the table to the user
            for row_number, row_data in enumerate(result):
                self.database_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.database_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            connection.close()
        except BaseException as error:
            print(error)

    def search_database_clicked(self):
        try:
            connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")

            # gets the text from each field of the row clicked and puts it into the correct format to
            # use in a select statement
            location_text = '%' + self.location_input.toPlainText() + '%'
            company_text = '%' + self.company_name_input.toPlainText() + '%'
            title_text = '%' + self.job_title_input.toPlainText() + '%'
            tags_text = '%' + self.tags_input.toPlainText() + '%'
            job_id_number = '%' + self.job_id_input.toPlainText() + '%'
            description_text = '%' + self.description_input.toPlainText() + '%'

            remote_option_selected = self.remote_input.currentIndex()
            if remote_option_selected == 0:
                remote_text = ""
            if remote_option_selected == 1:
                remote_text = "Yes"
            if remote_option_selected == 2:
                remote_text = "No"

            remote_text = '%' + remote_text + '%'

            days_published_index = self.pub_date_input.currentIndex()
            date_added_to_db_index = self.date_added_to_db_input.currentIndex()

            # Year-Month-Day Hour:Minute:Second:Mill second
            current_date_time = datetime.now()

            # calculates the minimum published date based on user input
            if days_published_index == 0:
                date_published_ago = ' '
            elif days_published_index == 1:
                date_published_ago = str(current_date_time - timedelta(days=1))
            elif days_published_index == 2:
                date_published_ago = str(current_date_time - timedelta(days=7))
            elif days_published_index == 3:
                date_published_ago = str(current_date_time - timedelta(days=10))
            elif days_published_index == 4:
                date_published_ago = str(current_date_time - timedelta(days=15))
            elif days_published_index == 5:
                date_published_ago = str(current_date_time - timedelta(days=20))
            elif days_published_index == 6:
                date_published_ago = str(current_date_time - timedelta(days=30))
            elif days_published_index == 7:
                date_published_ago = str(current_date_time - timedelta(days=50))

            # calculates the minimum date time added to db based on user input
            if date_added_to_db_index == 0:
                date_added_to_db_ago = ' '
            elif date_added_to_db_index == 1:
                date_added_to_db_ago = str(current_date_time - timedelta(days=1))
            elif date_added_to_db_index == 2:
                date_added_to_db_ago = str(current_date_time - timedelta(days=5))
            elif date_added_to_db_index == 3:
                date_added_to_db_ago = str(current_date_time - timedelta(days=10))
            elif date_added_to_db_index == 4:
                date_added_to_db_ago = str(current_date_time - timedelta(days=15))
            elif date_added_to_db_index == 5:
                date_added_to_db_ago = str(current_date_time - timedelta(days=20))

            # format Year-Month-Day Hour:Minute
            current_date_time = str(current_date_time + timedelta(days=1))
            current_date_time = current_date_time[0:16]

            # format = "Year-Month-day Hour:Minute"
            date_published_ago = date_published_ago[0:16]

            # format = "Year-Month-day Hour:Minute"
            date_added_to_db_ago = date_added_to_db_ago[0:16]

            query = "SELECT * FROM jobs WHERE location LIKE ? AND company LIKE ? AND title LIKE ? AND " \
                    "tags LIKE ? and remote LIKE ? AND description LIKE ? AND " \
                    "publication_date_modified >= ? AND publication_date_modified <= ? AND " \
                    "date_added_to_db >= ? AND date_added_to_db <= ? AND id LIKE ? "

            query_result = connection.execute(query,
                                              [location_text, company_text, title_text, tags_text, remote_text,
                                               description_text, date_published_ago,
                                               current_date_time, date_added_to_db_ago,
                                               current_date_time, job_id_number])
            self.database_table.setRowCount(0)

            #  adds the data from the job table to the table GUI and views the table to the user
            for row_number, row_data in enumerate(query_result):
                self.database_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.database_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            connection.close()

        except BaseException as error:
            print(error)

# gets the data from the row clicked and displays the results in text boxes at the bottom half of the GUI
    def view_row_clicked(self):
        try:
            row_clicked = self.database_table.currentRow()

            job_id_text = self.database_table.item(row_clicked, 0).text()
            title_of_job_text = self.database_table.item(row_clicked, 1).text()
            company_name_text = self.database_table.item(row_clicked, 2).text()
            description_job_text = self.database_table.item(row_clicked, 3).text()
            location_text = self.database_table.item(row_clicked, 4).text()
            tags_text = self.database_table.item(row_clicked, 5).text()
            publication_date_text = self.database_table.item(row_clicked, 6).text()
            remote_text = self.database_table.item(row_clicked, 7).text()
            date_added_to_db_text = self.database_table.item(row_clicked, 8).text()

            self.job_id_display.setPlainText(job_id_text)
            self.job_title_display.setText(title_of_job_text)
            self.company_name__display.setText(company_name_text)
            self.description_display.setText(description_job_text)
            self.location_display.setText(location_text)
            self.tags_display.setText(tags_text)
            self.pub_date_display.setText(publication_date_text)
            self.remote_display.setText(remote_text)
            self.date_added_to_db_display.setText(date_added_to_db_text)
        except BaseException as error:
            print(error)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
