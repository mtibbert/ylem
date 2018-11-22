import binascii
import temporenc


class TemporencUtils:
    def __init__(self):
        pass

    @staticmethod
    def packb(value=None, type=None,
              year=None, month=None, day=None,
              hour=None, minute=None, second=None,
              millisecond=None, microsecond=None, nanosecond=None,
              tz_offset=None):
        return temporenc.packb(value, type,
                               year, month, day,
                               hour, minute, second,
                               millisecond, microsecond, nanosecond,
                               tz_offset)

    @staticmethod
    def unpackb(value):
        return temporenc.unpackb(value)

    @staticmethod
    def byte_str_2_bin_str(byte_str, fill_len=1):
        """
        Converts a byte string into a binary string.
        :param byte_str: the byte string to convert
        :type byte_str: byte string
        :param fill_len: the length to pad the binary string. The returned
                         string will be left padded with zeros. If fill_len is
                         less than the length of the converted binary string,
                         then padding will be added to restore leading zeros.
        :type fill_len: int
        :return: a binary representation of the byte string
        :rtype: string

        >>> byte_str = TemporencUtils.packb(year=1983, month=1, day=15)

        >>> TemporencUtils.byte_str_2_bin_str(byte_str)
        '100011110111111000001110'

        >>> byte_str = TemporencUtils.packb(\
        year=1983, month=1, day=15, hour=18, minute=25, second=12)

        >>> TemporencUtils.byte_str_2_bin_str(byte_str)
        '0001111011111100000111010010011001001100'

        """
        if fill_len < (len(byte_str) * 8):
            fill_len = len(byte_str) * 8
        hexified = TemporencUtils.hexify_byte_str(byte_str)
        val = bin(int(hexified, 16))[2:].zfill(fill_len)  # 00010111
        return val

    @staticmethod
    def hexify_byte_str(byte_str):
        """
        Return the uppercase hexadecimal representation of the binary data. Every
        byte of data is converted into the corresponding 2-digit hex representation.
        The resulting string is therefore twice as long as the length of data.
        :param byte_str: byte string
        :type byte_str: byte string
        :return: string
        :rtype: string

        >>> TemporencUtils.hexify_byte_str(b'hello world')\
            == binascii.hexlify(b'hello world').upper()
        True
        """
        return binascii.hexlify(byte_str).upper()



