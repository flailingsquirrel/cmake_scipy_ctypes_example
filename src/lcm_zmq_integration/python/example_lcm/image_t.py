"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class image_t(object):
    __slots__ = ["width", "height", "size", "data"]

    def __init__(self):
        self.width = 0
        self.height = 0
        self.size = 0
        self.data = []

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(image_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">hhi", self.width, self.height, self.size))
        buf.write(struct.pack('>%df' % self.size, *self.data[:self.size]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != image_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return image_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = image_t()
        self.width, self.height, self.size = struct.unpack(">hhi", buf.read(8))
        self.data = struct.unpack('>%df' % self.size, buf.read(self.size * 4))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if image_t in parents: return 0
        tmphash = (0x7cff7cb7a9819c8f) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if image_t._packed_fingerprint is None:
            image_t._packed_fingerprint = struct.pack(">Q", image_t._get_hash_recursive([]))
        return image_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

