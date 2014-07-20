
#AT command strings
RESET_COMMAND = "AT Z"
ECHO_OFF_COMMAND = "AT E0"
ECHO_ON_COMMAND = "AT E1"
BATTERY_VOLTAGE_COMMAND = "AT RV"
SELECT_PROTOCOL_COMMAND = "AT SP 0"


#TODO: externalize configuration settings
DEFAULT_BAUDRATE = 38400
DEFAULT_BYTESIZE = 8
#This seems to be the most common port used when combining an ELM327 bluetooth OBDII scanner with a Raspberry Pi
#Will make this more general purpose later on.  Main focus now is specific use with ELM327 bluetooth on Raspberry Pi
DEFAULT_PORTNAME = '/dev/rfcomm0'
DEFAULT_STOPBITS = 1
DEFAULT_TIMEOUT = 3

DEFAULT_RETRIES = 10
