from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def make_databsae():
    """
    Make the Postgres database and create the table
    :return: database connexion
    """

    dbname = 'KlinesEthDB'
    username = 'Delphine'
    tablename = 'klines_eth_table'

    engine = create_engine()

