# FlaskBoilerplate

 A boilerplate Flask App.



This project requires:

- Python 3.x

- Flask

- Flask-SQLAlchemy

To run the server:

1. Open a terminal/command prompt window.

2. Change directory to the project

3. Run `python app.py` of `python3 app.py`

To create the database:

1. Open the `website\__init__.py` file

2. Under `db.init_app(app)`, add:
   
   ```python
   db.create_all(app=app)
   ```

3. Then run server.

4. Once you see a, `database.db` (note this may not show up in your text editor's file structure because it's a binary file, so check your file brower just to be safe), remove the line and save.
