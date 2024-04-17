# Ebook-PR-Application

The goal of this application is to allow CRKN librarians to access and know whether they have perpetual rights to a specific book if purchased through a CRKN deal or if they have tracked it using a spreadsheet that mimics the CRKN specs for such spreadsheets.   This is originally the work of Team 3 of the Winter 2024 CS4820 UPEI class.
.
This is done by scraping excel files from the CRKN Website (using this test page to get the files from, https://library.upei.ca/test-page-ebooks-perpetual-access-project). These excel files are then added to a local SQLite database, and functionalities such as searching for a specific book, or manually upload excel files to the database are created, and a neat front-end GUI to support user usage is designed.

# Setup
For development: do `pip install -r requirements.txt`, then run the mainrun.py file. Make sure you have Python 3.10 atleast installed. You should have an installation of Qt on your system -- usually this is automatically installed.

For production: use `pip install pyinstaller` to get pyinstaller, and then use `pyinstaller mainrun.spec` to compile an executable for your operating system.

