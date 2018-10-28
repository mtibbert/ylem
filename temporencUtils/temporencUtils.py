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
    def byte_str_2_bin_str(byte_str, fill_len=1, align_byte_boundry=False):
        val = bin(
            int(TemporencUtils.hexify_byte_str(byte_str).upper(), 16))[2:] \
            .zfill(fill_len)
        # if align_byte_boundry and (fill_len % 2):
        #     val = "0" + val
        # l_val = len(val)
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



