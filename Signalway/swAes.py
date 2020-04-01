#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : swAes.py
# @Author: luowq
# @Date  : 2019/9/4 17:31
# @Desc  :
from Crypto.Cipher import AES
import base64

class PKCS7Encoder(object):
    """提供基于PKCS7算法的加解密接口"""

    block_size = 16

    def encode(self, text):
        """
        明文使用PKCS7填充,目前填充\x00
        """
        bs = AES.block_size  # 16
        length = len(text)
        bytes_length = len(bytes(text, encoding='utf-8'))
        padding_size = length if(bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = '\x00'* padding
        return text + padding_text


    def decode(self, decrypted):
        """
        删除明文补位
        """
        return decrypted.replace(u'\x00',u'').replace(u'\x05',u'')


class SwAesCBCPsck7(object):

    def __init__(self):
        self.mode = AES.MODE_CBC
        self.encoder = PKCS7Encoder()

    @classmethod
    def encrypt(cls,key,iv,text):
        encryptor = AES.new(key.encode("utf-8"), cls().mode, iv.encode("utf-8"))
        pad_text = cls().encoder.encode(text)
        cipher = encryptor.encrypt(pad_text.encode("utf-8"))
        #cipher = encryptor.encrypt(bytes(pad_text,encoding='utf-8'))
        result = base64.b64encode(cipher)
        return str(result, encoding='utf-8')

    @classmethod
    def decrypt(cls,key,iv,text):
        encryptor = AES.new(key.encode("utf-8"), cls().mode, iv.encode("utf-8"))
        encrypt_bytes = base64.b64decode(text)
        decrypt_bytes = encryptor.decrypt(encrypt_bytes)
        result = str(decrypt_bytes, encoding='utf-8')
        result = cls().encoder.decode(result)
        return result

# print(SwAesCBCPsck7.encrypt("F7A0B971B199FD2A","2019101720191017",'{"carNOC":"蓝","confid":886,"memo":"","picN":"20191017133134桂A73X15.jpg","triggT":"2019-10-17 13:31:34"}'))
# print(SwAesCBCPsck7.decrypt("F7A0B971B199FD2A","2019101720191017","831jQOMgd9Dklh1p6m0h/iNE9D1vhNTlU7y4YFdwKd3peTgDqrP5O8frggb4lc9gl1qwckBa45EuIeMtuNP65D4Nw1ydoGUs1b9SkMEzP2uxAAZsfw4w+O9c7jIsvLVSUMWipKCt9nEnC6eaKsJv0/1PZuYTuZuUy0g/fHsY2eg="))