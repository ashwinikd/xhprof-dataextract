import time

file_handle = None

def log(message, logtype="INFO"):
	global file_handle
	fname = "{log_dir}/{prefix}.{date_time}.log".format(
		log_dir = xhprof_config["logs"]["dir"],
		prefix = xhprof_config["logs"]["prefix"],
		date_time = time.strftime("%Y-%m-%d.%H")
	)

	try:
		with open(fname, 'a') as f:
			file_handle = f
			data = "{date_time} [{log_type}] {log_msg}".format(
				date_time = time.strftime("%Y-%m-%d %H:%M:%S"),
				log_type = logtype,
				log_msg = message
			)
			f.write(data + "\n")
	except IOError as e: print "ERROR opening log file"
	finally:
		file_handle.close()

def debug(message):
	log(message, "DEBUG")

def error(message):
	log(message, "ERROR")

def info(message):
	log(message, "INFO")
