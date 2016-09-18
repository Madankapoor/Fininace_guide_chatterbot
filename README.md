# Fininace_guide_chatterbot
A guide to common man for financial investments using chatterbot.

Software:
>Flask microframework.

Tags:
>Python,Cython,Postgresql,Sqlite

Website:
>https://finchatbot.herokuapp.com/

Repo Structure
```
Procfile                        Configuration Setting for Heroku Cloud
README.md                       This File.    
Structure                       Structure of the Repo    
aiml/                           Directory With all aiml files.
app/                            Main Application Module.
app.db                          Local Test Database.
bot_brain.brn                   Brain file generated for quick Loading of application.
config.py                       Configuration File of Application
create_db.py                    Python file for Creation of local and production Databases.
db_downgrade.py                 Used to downgrade the Database Migration Repo 
db_migrate.py                   Used to Reflect the changes made in models to Database - Produce Migration
db_repository/                  Interior of Migration Repo
db_upgrade.py                   Used to Upgrade the Database Migration Repo     
dep-aiml/                       Depency Files of Aiml
deploy.sh                       Script to Deploy the Application to Heroku
investment.aiml                 
makec.sh                        Used for building Application Depency
requirements.txt                List of Depency of the Application.
run.sh                          Script Used to start the application in debug mode.
std-startup.xml                 Xml configuration of the BOT
test.py                         Unit Tests 
unit_tests/                     Specific Unit Tests
uwsgi.ini                       Setting for the production Server.    


Python Code Files.
./app:                          Main Directory of the Application  
    __init__.py                 File used to Initialize the Application
    chatprocess/                The chat Engine of the bot. 
        Engine.pyx              Cython File -Provides Saving chat and quick loading functionality.
        __init__.py             File used to Initialize the chatbot
    forms.py                    The classes for forms used in Application
    hashinfo.py                 Information to passed by chat bot using #
    helper.py                   File provides various helper functions.
    models.py                   The Object Oriented Mapper for RDBMS.
    static/                     Contains all static resources of application like js,css,images,videos
    templates/                  Contains all Pages which are to rendered.
    views.py                    The url mapping of the links to Pages with settings.

Application HTML pages.
./app/templates:
    Home.html
    _formhelpers.html
    bots.html
    chats/
    chatui.html
    contact.html
    contactform.html
    homel.html
    index.html
    index2.html
    index3.html
    login.html
    quotes.html
    register.html
    reset.html
    resetrequest.html
    tag.html
    team.html
    teaml.html
```
