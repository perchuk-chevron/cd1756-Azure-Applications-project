import os

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_var(name):
    value = os.environ.get(name)
    if not value:
        raise ValueError(f"Need to define {name} environment variable")
    return value

class Config(object):
    SECRET_KEY = get_env_var('SECRET_KEY')

    BLOB_ACCOUNT = get_env_var('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = get_env_var('BLOB_STORAGE_KEY') 
    BLOB_CONTAINER = get_env_var('BLOB_CONTAINER')

    SQL_SERVER = get_env_var('SQL_SERVER') 
    SQL_DATABASE = get_env_var('SQL_DATABASE')
    SQL_USER_NAME = get_env_var('SQL_USER_NAME')
    SQL_PASSWORD = get_env_var('SQL_PASSWORD')
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = get_env_var("CLIENT_SECRET")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = get_env_var("CLIENT_ID")

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session