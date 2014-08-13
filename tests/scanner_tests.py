from shadetree.obd.scanner import decode_bitwise_pids

DURANGO_SUPPORTED_PIDS_RESPONSE = 'BE 3E B8 10 '
JETTA_DIESEL_SUPPORTED_PIDS_RESPONSE = '98 3B 80 19 '


def test_decode_bitwise_pids_durango():
    """
        Verify we correctly parse information about supported PIDs on a 1999 Dodge Durango
    """
    supported_pids = decode_bitwise_pids(DURANGO_SUPPORTED_PIDS_RESPONSE)
    assert supported_pids == {
        '01': True,
        '02': False,
        '03': True,
        '04': True,
        '05': True,
        '06': True,
        '07': True,
        '08': False,
        '09': False,
        '0A': False,
        '0B': True,
        '0C': True,
        '0D': True,
        '0E': True,
        '0F': True,
        '10': False,
        '11': True,
        '12': False,
        '13': True,
        '14': True,
        '15': True,
        '16': False,
        '17': False,
        '18': False,
        '19': False,
        '1A': False,
        '1B': False,
        '1C': True,
        '1D': False,
        '1E': False,
        '1F': False,
        '20': False
    }


def test_decode_bitwise_pids_jetta_diesel():
    """
        Verify we correctly parse information about supported PIDs on a 2004 Jetta Diesel Wagon
    """
    supported_pids = decode_bitwise_pids(JETTA_DIESEL_SUPPORTED_PIDS_RESPONSE)
    assert  supported_pids == {
        '01': True,
        '02': False,
        '03': False,
        '04': True,
        '05': True,
        '06': False,
        '07': False,
        '08': False,
        '09': False,
        '0A': False,
        '0B': True,
        '0C': True,
        '0D': True,
        '0E': False,
        '0F': True,
        '10': True,
        '11': True,
        '12': False,
        '13': False,
        '14': False,
        '15': False,
        '16': False,
        '17': False,
        '18': False,
        '19': False,
        '1A': False,
        '1B': False,
        '1C': True,
        '1D': True,
        '1E': False,
        '1F': False,
        '20': True
    }