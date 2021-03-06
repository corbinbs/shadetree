# Information about OBD-II PIDs
# http://en.wikipedia.org/wiki/OBD-II_PIDs

#PID hex codes
PIDS_SUPPORTED_00_20 = "00"
MONITOR_STATUS_SINCE_DTC_CLEARED = "01"
FREEZE_DTC = "02"
VEHICLE_IDENTIFICATION_NUMBER = "02"
FUEL_SYSTEM_STATUS = "03"
CALCULATED_ENGINE_LOAD = "04"
ENGINE_COOLANT_TEMPERATURE = "05"
SHORT_TERM_FUEL_TRIM_BANK_1 = "06"
LONG_TERM_FUEL_TRIM_BANK_1 = "07"
SHORT_TERM_FUEL_TRIM_BANK_2 = "08"
LONG_TERM_FUEL_TRIM_BANK_2 = "09"
FUEL_PRESSURE = "0A"
ECU_NAME = "0A"
INTAKE_MANIFOLD_PRESSURE = "0B"
ENGINE_RPM = "0C"
VEHICLE_SPEED = "0D"
TIMING_ADVANCE = "0E"
INTAKE_AIR_TEMPERATURE = "0F"
MAF_AIR_FLOW = "10"
THROTTLE_POSITION = "11"

#TODO: Oxygen sensors

AUXILIARY_INPUT_STATUS = "1E"
ENGINE_RUN_TIME_SINCE_START = "1F"
PIDS_SUPPORTED_21_40 = "20"
DISTANCE_TRAVELED_WITH_MIL_ON = "21"

FUEL_RAIL_PRESSURE = "23"

COMMANDED_EGR = "2C"
EGR_ERROR = "2D"
COMMANDED_EVAPORATIVE_PURGE = "2E"
FUEL_LEVEL_INPUT = "2F"
DISTANCE_TRAVELED_SINCE_CODES_CLEARED = "31"
EVAP_SYSTEM_VAPOR_PRESSURE = "32"
BAROMETRIC_PRESSURE = "33"

PIDS_SUPPORTED_41_60 = "40"
CONTROL_MODULE_VOLTAGE = "41"
ABSOLUTE_LOAD_VALUE = "42"
AMBIENT_AIR_TEMPERATURE = "46"

TIME_RUN_WITH_MIL_ON = "4D"
TIME_SINCE_TROUBLE_CODES_CLEARED = "4E"

FUEL_TYPE = "51"
ETHANOL_FUEL_PERCENTAGE = "52"

RELATIVE_ACCELERATOR_PEDAL_POSITION = "5A"
HYBRID_BATTERY_PACK_REMAINING_LIFE = "5B"
ENGINE_OIL_TEMPERATURE = "5C"
FUEL_INJECTION_TIMING = "5D"
ENGINE_FUEL_RATE = "5E"


PIDS_SUPPORTED_61_80 = "60"
ENGINE_PERCENT_TORQUE = "64"

#TODO: remaining PIDs
