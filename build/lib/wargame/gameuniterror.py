# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:27:59 2019

@author: Tuna ERTEKİN
"""

class GameUnitError(Exception):
    
    def __init__(self, message='', code=000):
        super().__init__(message)
        self.error_message = '~'*50 + '\n'
        self.error_dict = {
            000: "Error 000 : Unspesified error",
            101: "Error 101 : Healt Metter Problem!",
            102: "Error 102 : Attack issue! Ignored", 
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~'*50