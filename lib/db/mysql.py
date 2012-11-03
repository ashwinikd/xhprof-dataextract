import MySQLdb
import MySQLdb.cursors
import sys

conn = None

"""
Connect to database.
"""
def connect(db_host = "localhost",
			db_user = "root",
			db_pass = "",
			db_name = "xhprof"):
	global conn

	try:
		logger.log("Trying to connect to db")
		conn = MySQLdb.connect(
			xhprof_config["db"]["host"],
			xhprof_config["db"]["user"],
			xhprof_config["db"]["pass"],
			xhprof_config["db"]["name"]
		)
	except MySQLdb.OperationalError, e:
		logger.error("Error[%d]: %s" %(e.args[0], e.args[1]))
		logger.error("Unable to connect to the database")
		sys.exit()

	logger.log("Connected to database.")

	return conn



"""
Execute an sql query
"""
def query(sql, fetchall=True):
	global conn
	conn = connect()
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
	num_rows = 0

	if not sql:
		logger.error("QUERY is Empty")
		return False

	try:
		if isinstance(sql, str):
			logger.debug("Executing Query {sql_query}".format(
				sql_query = sql
			))
			num_rows = cursor.execute(sql)
			logger.info("Rows affected: %d" % (num_rows))
			close()
		else:
			query = sql[0]
			params = sql[1]
			logger.debug("Executing Query {sql_query} with params {query_params}".format(
				sql_query = sql[0],
				query_params = str(sql[1])
			))
			num_rows = cursor.execute(query, params)
			logger.info("Num Rows affected: %d" % (num_rows))
			close()
	except MySQLdb.ProgrammingError, e:
		logger.error("Invalid SQL query")
		close()
		sys.exit(1)

	return (num_rows, cursor)

def write(sql):
	global conn
	conn = connect()
	cursor = conn.cursor()

	try:
		if isinstance(sql, str):
			logger.debug("Executing Query {sql_query}".format(
				sql_query = sql
			))
			num_rows = cursor.execute(sql)
			conn.commit()
			logger.info("Num rows affected: %d" % (num_rows))
		else:
			logger.debug("Executing Query {sql_query} with params {query_params}".format(
				sql_query = sql[0],
				query_params = str(sql[1])
			))
			query = sql[0]
			params = sql[1]
			num_rows = cursor.execute(query, params)
			conn.commit()
			logger.log("Query Successful. Num rows affected: %d" % (num_rows))
			close()
	except MySQLdb.ProgrammingError, e:
		logger.error("Error[%d]: %s" %(e.args[0], e.args[1]))
		logger.error("Invalid SQL query")
		close()
		sys.exit(1)
	except MySQLdb.IntegrityError, e:
		logger.error("--->SQL Error: %s" % e)
		return False
	except Exception, e:
		logger.error("fatal:" + str(e))
		close()
	close()
"""
Close the Connection
"""
def close():
	global conn, cursor
	logger.info("Closing database connection.")
	try:
		conn.close()
	except MySQLdb.ProgrammingError, e:
		pass

def _check_connection():
	global conn, cursor

	if not conn or not cursor:
		print "Database Connection is not available! Exiting"
		sys.exit(1)
