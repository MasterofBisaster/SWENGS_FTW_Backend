# FTW - Backend

## Setup Guide

### install the required Python packeges with pip

1. Clone the project (if not already done)
2. open a command line tool and navigate to the project root (cmd executed as Admin is highly recommended)
3. Type the following:
```bash
pip install -r requirements.txt
```

### create the database
```bash
python manage.py migrate
```

### import the demo database
```bash
python manage.py loaddata db.json
```

### run backend server
```bash
python manage.py runserver
```

