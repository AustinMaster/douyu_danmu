#!/usr/bin/env python
# -*- coding=utf8 -*-
import time, sys

#from danmu import DanMuClient
from danmu import *
NOBLE_DICT = {
    '1': '骑士',
    '2': '子爵',
    '3': '伯爵',
    '4': '公爵',
    '5': '国王',
    '6': '皇帝',
    '7': '游侠',
}
def pp(msg):
    print(msg.ene(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

dmc = DanMuClient('https://www.douyu.com/2009')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    pp('[%s] %s' % (msg['NickName'], msg['Content']))

@dmc.gift
def gift_fn(msg):
    pp('[%s] sent a gift!' % msg['NickName'])

@dmc.anbc
def anbc_fn(msg):
    if 'gvnk' not in msg:
       print('[%s] 在 [%s] 开通 [%s]!' % (msg['unk'].encode("utf8"), msg['donk'].encode("utf8"), NOBLE_DICT[msg['nl'].encode("utf8")]))
    else:
       print('[%s] 在 [%s] 给 [%s] 开通 [%s]!' % (msg['gvnk'].encode("utf8"), msg['unk'].encode("utf8"), msg['donk'].encode("utf8"), NOBLE_DICT[msg['nl'].encode("utf8")]))
    sys.stdout.flush()

@dmc.rnewbc
def rnewbc_fn(msg):
    if 'gvnk' not in msg:
        print('[%s] 在 [%s] 续费[%s]!' % (msg['unk'].encode("utf8"), msg['donk'].encode("utf8"), NOBLE_DICT[msg['nl'].encode("utf8")]))
    else:
        print('[%s] 在 [%s] 给 [%s] 续费!' % (msg['gvnk'].encode("utf8"), msg['unk'].encode("utf8"), msg['donk'].encode("utf8"), NOBLE_DICT[msg['nl'].encode("utf8")]))
#@dmc.other
#def other_fn(msg):
#    if msg['type'] == None or msg['type'] == "keeplive":
#       return
#    print msg
#    sys.stdout.flush()
dmc.start(blockThread=True)
