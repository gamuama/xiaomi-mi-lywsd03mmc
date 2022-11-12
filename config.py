# domoticz configuration
DOMOTICZ_SERVER_IP = "192.168.178.11"
DOMOTICZ_SERVER_PORT = "8080"
DOMOTICZ_USERNAME = ""
DOMOTICZ_PASSWORD = ""

# sensor dictionary to add own sensors
# if you don't want to use the raw voltage option, just write -1 in the VOLTAGE_IDX value field
sensors = { 1: {"MAC": "A4:C1:38:CB:2D:74", "TH_IDX": 48, "VOLTAGE_IDX": -1, "UPDATED": False}, #EVAN
			2: {"MAC": "A4:C1:38:E0:63:E2", "TH_IDX": 47, "VOLTAGE_IDX": -1, "UPDATED": False}, # NIJA
			3: {"MAC": "A4:C1:38:AB:B5:C0", "TH_IDX": 67, "VOLTAGE_IDX": -1, "UPDATED": False}, # Lenja
			4: {"MAC": "A4:C1:38:D8:C2:03", "TH_IDX": 68, "VOLTAGE_IDX": -1, "UPDATED": False}, # uta
			5: {"MAC": "A4:C1:38:B1:64:B2", "TH_IDX": 69, "VOLTAGE_IDX": -1, "UPDATED": False} # Podstresje
                #        6: {"MAC": "A4:C1:38:CE:47:8C", "TH_IDX": xx, "VOLTAGE_IDX": -1, "UPDATED": False} # Kopalnica spodaj

	  }
# other configuration
TEMPERATURE_PREC = 1
NUM_RETRY = 3 #number of connection retries - 0 = retry disabled


# Logfile configuration
LOG_FILE_NAME = "loginfo.log"
LOG_FILE_SIZE = 16384		# file size in bytes
