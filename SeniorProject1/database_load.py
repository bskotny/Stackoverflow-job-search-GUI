import pytest
import feedparser
import sqlite3
import re
import datetime
from sqlite3 import Error

# creates the connection to the database
def create_connection(db_file):
    """ create a database connection to a SQLite database specified by db_file
        :param db_file: database file
        return: None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


# creates the table
def create_table(conn, create_table_sql):
    """" create a table fom the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE Statement
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# gets the term within the tag list
def get_tag_name(tag_name):
    start = tag_name.find("'term': ") + 9
    end = tag_name.find("', 'scheme':", start)
    return tag_name[start:end]


# gets the location of the job
def get_location(conn, location_entry_number):
    try:
        location_of_company = conn['entries'][location_entry_number]['location']

    # location_of_company is not listed
    except KeyError:
        print("Location:", location_entry_number, "no location listed")
        location_of_company = "NULL"

    # location_of_company is not a string
    except TypeError as location_type_error:
        print("Location:", location_entry_number, location_type_error)
        location_of_company = "NULL"

    return location_of_company


# gets the id of the job entry
def get_id(conn, id_entry_number):
    try:
        job_id = conn['entries'][id_entry_number]['id']

    except KeyError:
        job_id = "NULL"

    except TypeError:
        job_id = "NULL"

    return job_id


# gets the title from the entry in the feed
def get_title(conn, title_entry_number):
    try:
        title_of_job = conn['entries'][title_entry_number]['title']

    # title_of_job is not listed
    except KeyError:
        print("Title KeyError:", title_entry_number, "title not listed")
        title_of_job = "NULL"

    # title_of_job is not a string
    except TypeError as title_type_error:
        print("Title TypeError:", title_entry_number, title_type_error)
        title_of_job = "NULL"

    return title_of_job


# gets the publication date from the entry in the feed
def get_publication_date(conn, pub_entry_number):
    try:
        publication_date_of_job = conn['entries'][pub_entry_number]['published']

        # removes the "Z" from each entries publication date
        publication_date_of_job = publication_date_of_job.replace("Z", "")

    except KeyError:
        print("Pub Date:", pub_entry_number, "publication date not listed")
        publication_date_of_job = "NULL"

    # publication_date_of_job is not a string
    except TypeError as pub_date_type_error:
        print("Pub Date:", pub_entry_number, pub_date_type_error)
        publication_date_of_job = "NULL"

    return publication_date_of_job


# gets the description of the entry
def get_description(conn, description_entry_number):
    try:
        my_description = conn['entries'][description_entry_number]['description']
        # gets rid of the html tags in the description
        cleaner = re.compile("<.*?>")
        clean_description_of_job = re.sub(cleaner, '', my_description)

    # description is not listed
    except KeyError:
        print("Description: ", description_entry_number, "description not listed")
        clean_description_of_job = "NULL"

    # description is not a string
    except TypeError as description_of_job_type_error:
        print("Description:", description_entry_number, description_of_job_type_error)
        clean_description_of_job = "NULL"

    return clean_description_of_job


# gets the company name of the entry
def get_company(conn, company_entry_number):
    try:
        company_name = conn['entries'][company_entry_number]['author']

    # no company_name listed
    except KeyError:
        print("Company name:", company_entry_number, "company name not listed")
        company_name = "NULL"

    # company_name is not a string
    except TypeError as company_name_type_error:
        print("Company name:", company_entry_number, company_name_type_error)
        company_name = "NULL"

    return company_name


# gets the tags from the entry
def get_tags(conn, tag_entry_number):
    tag_list = []

    try:
        for x in range(len(conn['entries'][tag_entry_number]['tags'])):
            job_tags = str(conn['entries'][tag_entry_number]['tags'][x])
            tag_name = get_tag_name(job_tags)
            tag_list.append(tag_name)

    # no tags found
    except KeyError:
        print("Job tags:", tag_entry_number, "no tags listed")
        job_tags = "NULL"
        tag_list.append(job_tags)

    # tag is not a string
    except TypeError as job_tag_type_error:
        print("Job tags:", tag_entry_number, job_tag_type_error)
        job_tags = "NULL"
        tag_list.append(job_tags)

    final_tag_list = str(tag_list)
    return final_tag_list


# finds out if job is remote
def get_remote(remote):
    remote = remote.find("remote")
    if remote == -1:
        remote = "No"
    else:
        remote = "Yes"
    return remote


def load_feed():
    # url of the website where we are getting the feed
    website_feed = feedparser.parse('https://stackoverflow.com/jobs/feed')

    # where the database is created
    database = r"C:\\sqlite\python_sqlite.db"

    # creates table names jobs
    sql_create_jobs_table = "CREATE TABLE IF NOT EXISTS jobs(id INT PRIMARY KEY, title TEXT NOT NULL, " \
                            "company TEXT NOT NULL, " \
                            "description TEXT NOT NULL, " \
                            "location TEXT NOT NULL, tags TEXT NOT NULL, " \
                            "publication_date TEXT NOT NULL, remote TEXT NOT NULL, date_added_to_db TEXT NOT NULL, " \
                            "publication_date_modified TEXT NOT NULL)"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_jobs_table)
    else:
        print("Error: cannot create database connection")

    # length of feed
    entry_length = len(website_feed['entries'])
    assert entry_length > 0, "No entries found"

    # gets the information of the entry feed
    for feed_entry_number in range(entry_length):
        job_id = get_id(website_feed, feed_entry_number )
        title_of_job = get_title(website_feed, feed_entry_number )
        remote = get_remote(title_of_job)
        location_of_company = get_location(website_feed, feed_entry_number )
        publication_date_of_job = get_publication_date(website_feed, feed_entry_number)

        publication_date_of_job_split = publication_date_of_job.split(" ")

        if publication_date_of_job.find("Jan") != -1:
            publication_date_of_job_split[2] = "01"
        elif publication_date_of_job.find("Feb") != -1:
            publication_date_of_job_split[2] = "02"
        elif publication_date_of_job.find("Mar") != -1:
            publication_date_of_job_split[2] = "03"
        elif publication_date_of_job.find("Apr") != -1:
            publication_date_of_job_split[2] = "04"
        elif publication_date_of_job.find("May") != -1:
            publication_date_of_job_split[2] = "05"
        elif publication_date_of_job.find("Jun") != -1:
            publication_date_of_job_split[2] = "06"
        elif publication_date_of_job.find("Jul") != -1:
            publication_date_of_job_split[2] = "07"
        elif publication_date_of_job.find("Aug" != -1):
            publication_date_of_job_split[2] = "08"
        elif publication_date_of_job.find("Sep") != -1:
            publication_date_of_job_split[2] = "09"
        elif publication_date_of_job.find("Oct") != -1:
            publication_date_of_job_split[2] = "10"
        elif publication_date_of_job.find("Nov") != -1:
            publication_date_of_job_split[2] = "11"
        elif publication_date_of_job.find("Dec" != -1):
            publication_date_of_job_split[2] = "12"

        publication_date_of_job_modified = publication_date_of_job_split[4].split(":")
        publication_date_of_job_final = (publication_date_of_job_split[3] + "-" +
                                            publication_date_of_job_split[2] + "-" +
                                            publication_date_of_job_split[1] + " " +
                                         publication_date_of_job_modified[0] + ":" +
                                         publication_date_of_job_modified[1])

        clean_description_of_job = get_description(website_feed, feed_entry_number )
        company_name = get_company(website_feed, feed_entry_number )
        final_tag_list = get_tags(website_feed, feed_entry_number )

        date_added_to_database = datetime.datetime.now()
        date_added_to_database = date_added_to_database.strftime("%Y-%m-%d %H:%M")

        # inserts the information from the feed into the table
        with conn:
            c = conn.cursor()
            c.execute(
                "INSERT OR IGNORE INTO jobs(id, title, company, description, location, "
                "tags, publication_date, remote, date_added_to_db, publication_date_modified)"
                " VALUES(?,?,?,?,?,?,?,?,?,?)",
                (job_id, title_of_job, company_name, clean_description_of_job, location_of_company, final_tag_list,
                 publication_date_of_job, remote, date_added_to_database, publication_date_of_job_final)
            )


def load_after_delete(last_publication_date):
    connection = sqlite3.connect(r"C:\\sqlite\python_sqlite.db")
    print("IN LOAD DELETE: ", last_publication_date)
    # inserts the information from the feed into the table
    with connection:
        c = connection.cursor()
        c.execute(
            "DELETE FROM jobs WHERE publication_date_modified <= ?", (last_publication_date,)
        )
