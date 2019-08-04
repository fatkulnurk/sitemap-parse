import mysql.connector

def mysql_connection():
    mydb = mysql.connector.connect(
    host="sgx9.cloudhost.id",
    user="dibumico_torrent_bos",
    passwd="indonesiazonk",
    database="dibumico_torrent"
    )
    return mydb.cursor()
