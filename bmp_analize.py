__author__ = 'JJW'

import struct


def bmp_analise(file_name):
    with open(file_name,'rb') as f:
        s = f.read(30)
    print(s)
    s1 = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    s_analise = struct.unpack('<ccIIIIIIHH', s1)
    print(s_analise)
    print(s_analise[0]+s_analise[1])
    if s_analise[0]+s_analise[1] == b'BM':
        print('size is %dx%d, color is %d' % (s_analise[6], s_analise[7], s_analise[9]))
    else:
        print('This picture is not a wei tu!')

bmp_analise('aaa.bmp')
