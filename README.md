# Test
Testing exercise

# Create Enviroment
python3.X -m venv testenv

# Init Enviroment
source testenv/bin/activate

# Copy content .env.example to .env and set database credentials
# Init migration
python manage.py migrate

# Creating superuser. Give him username and password
python manage.py createsuperuser

# Initialization seeds
python manage.py seed_init
