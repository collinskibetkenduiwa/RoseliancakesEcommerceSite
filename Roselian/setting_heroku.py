import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES = { 'default': dj_database_url.config() }