from shadetree.obd import modes
from shadetree.obd import pids

VEHICLE_ID_NUMBER_COMMAND = '{0} {1}'.format(modes.VEHICLE_INFORMATION_DATA, pids.VEHICLE_IDENTIFICATION_NUMBER)
ECU_NAME_COMMAND = '{0} {1}'.format(modes.VEHICLE_INFORMATION_DATA, pids.ECU_NAME)
FUEL_TYPE_COMMAND = '{0} {1}'.format(modes.CURRENT_DATA, pids.FUEL_TYPE)

CLEAR_TROUBLE_CODES_COMMAND = '{0}'.format(modes.CLEAR_TROUBLE_CODES_AND_VALUES)

CURRENT_ENGINE_COOLANT_TEMP_COMMAND = '{0} {1}'.format(modes.CURRENT_DATA, pids.ENGINE_COOLANT_TEMPERATURE)
CURRENT_ENGINE_OIL_TEMP_COMMAND = '{0} {1}'.format(modes.CURRENT_DATA, pids.ENGINE_OIL_TEMPERATURE)
CURRENT_ENGINE_RPM = '{0} {1}'.format(modes.CURRENT_DATA, pids.ENGINE_RPM)

CURRENT_MODE_PIDS_SUPPORTED_COMMAND = '{0} {1}'.format(modes.CURRENT_DATA, pids.PIDS_SUPPORTED_00_20)