from jobfilter import *
import sys
from PyQt5 import QtWidgets
import pytestqt


def test_view(qtbot):
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)
    window.view_database_on_click()

    connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
    table_check_exists = "SELECT COUNT(*) FROM sqlite_master WHERE name ='jobs' and type='table';"
    table_check_exists_result = connection.execute(table_check_exists).fetchone()[0]

    if table_check_exists_result != 0:
        text = str(window.database_table.item(0, 1).text())
        if text != " ":
            assert text != ""

    if table_check_exists_result == 0:
        assert BaseException


def test_delete_repopulate():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)

    with pytest.raises(BaseException):
        connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
        last_datetime_pub_before_clear = "SELECT publication_date_modified from jobs " \
                                         "ORDER by publication_date_modified desc LIMIT 1"
        last_datetime_pub_before_clear = connection.execute(
            last_datetime_pub_before_clear).fetchone()
        last_datetime_pub_before_clear = last_datetime_pub_before_clear[0]
        last_datetime_pub_before_clear = datetime.datetime.strptime(
            last_datetime_pub_before_clear, "%Y-%m-%d %H:%M")

        window.clear_database_and_repopulate_on_click()

        first_datetime_pub_after_clear = "SELECT publication_date_modified from jobs " \
                                         "ORDER by publication_date_modified asc LIMIT 1"
        first_datetime_pub_after_clear  = connection.execute(first_datetime_pub_after_clear ).fetchone()
        first_datetime_pub_after_clear  = first_datetime_pub_after_clear [0]
        first_datetime_pub_after_clear  = datetime.datetime.strptime(
            first_datetime_pub_after_clear , "%Y-%m-%d %H:%M")

        assert first_datetime_pub_after_clear > last_datetime_pub_before_clear


def test_update():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)
    with pytest.raises(BaseException):
        connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
        last_datetime_added_db_before_clear = "SELECT date_added_to_db from jobs ORDER by date_added_to_db desc LIMIT 1"
        last_datetime_added_db_before_clear = connection.execute(last_datetime_added_db_before_clear).fetchone()
        last_datetime_added_db_before_clear = last_datetime_added_db_before_clear[0]
        last_datetime_added_db_before_clear = datetime.datetime.strptime(
            last_datetime_added_db_before_clear, "%Y-%m-%d %H:%M")

        window.update_database_on_click()

        first_datetime_added_db_before_clear = "SELECT date_added_to_db from jobs ORDER by date_added_to_db asc LIMIT 1"
        first_datetime_added_db_before_clear = connection.execute(first_datetime_added_db_before_clear).fetchone()
        first_datetime_added_db_before_clear = first_datetime_added_db_before_clear[0]
        first_datetime_added_db_before_clear = datetime.datetime.strptime(
            first_datetime_added_db_before_clear, "%Y-%m-%d %H:%M")

        assert first_datetime_added_db_before_clear > last_datetime_added_db_before_clear


def test_good_search_publication_date():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)

    window.pub_date_input.setCurrentIndex(1)
    window.search_database_clicked()

    # Year-Month-Day Hour:Minute:Second:Mill second
    current_date_time = datetime.now()
    # Year-Month-Day Hour:Minute:Second:Mill second
    date_published_ago = str(current_date_time - timedelta(days=1))
    current_date_time = str(current_date_time + timedelta(days=1))

    # format Year-Month-Day Hour:Minute
    current_date_time = current_date_time[0:16]
    date_published_ago = date_published_ago[0:16]

    if window.database_table.item(0, 0) is not None:
        for row_number in range(window.database_table.rowCount()):
            assert window.database_table.item(row_number, 9).text() >= date_published_ago and \
                   window.database_table.item(row_number, 9).text() <= current_date_time


def test_good_search_remote_table():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)

    window.remote_input.setCurrentIndex(1)

    window.search_database_clicked()
    if window.database_table.item(0, 0) is not None:
        for row_number in range(window.database_table.rowCount()):
            assert window.database_table.item(row_number, 7).text() != "No"

    window.remote_input.setCurrentIndex(0)


def test_good_search_remote_no_table():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)

    window.remote_input.setCurrentIndex(1)

    window.search_database_clicked()
    if window.database_table.item(0, 0) is None:
        assert BaseException

    window.remote_input.setCurrentIndex(0)


def test_bad_search_tags():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)

    window.tags_input.setPlainText("python, sql")
    window.search_database_clicked()
    assert window.database_table.item(0, 0) is None
    window.tags_input.clear()


def test_bad_search_title():
    window = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)

    window.job_title_input.setPlainText("Join                   ")
    window.search_database_clicked()
    assert window.database_table.item(0, 0) is None
    window.job_title_input.clear()




