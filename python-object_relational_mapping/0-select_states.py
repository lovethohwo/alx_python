# 0-select_states.pyd
import MySQLdb
database = MySQLdb.connect(host="localhost", user="root", passwd="Judyloveth@2023", db="hbtn_0e_0_usa")
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)")
