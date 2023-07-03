# coding: utf-8

# Author   : InferiorAK
# Facebook : fb.com/InferiorAK
# Github   : github.com/InfeiriorAK
# Twitter  : twitter.com/InferiorAK
# Youtube  : youtube.com/@InferiorAK
# 1st Release : 3rd July, 2023

import sys
from argparse import ArgumentParser

# Arguments
parser = ArgumentParser(usage="%(prog)s [options]", description="Size and Counter Tool by InferiorAK")
parser.add_argument("-f", "--file", metavar="", type=str, help="Target File")
parser.add_argument("-bc", "--byte", help="Count Bytes", action="store_true")
parser.add_argument("-cc", "--char", help="Count Characters", action="store_true")
parser.add_argument("-wc", "--word", help="Count Words", action="store_true")
parser.add_argument("-lc", "--line", help="Count Lines", action="store_true")
parser.add_argument("-sz", "--size", help="File Size", action="store_true")
parser.add_argument("-v", "--version", help="Show Version", action="store_true")
args = parser.parse_args()

# mains
class Data:
    def __init__(self, file):
        self.__file = file
        self.__data = open(file, "r").read()
    def byte(self, file):
        self.__bc = len(open(file, "rb").read())
        print(f"[+] Total bytes: {self.__bc}")
    def char(self):
        self.__cc = len(self.__data)
        print(f"[+] Total characters: {self.__cc}")
    def word(self):
        self.__wc = len(self.__data.split())
        print(f"[+] Total words: {self.__wc}")
    def line(self):
        self.__lc = len(open(self.__file).readlines())
        print(f"[+] Total lines: {self.__lc}")

class Size:
    def __init__(self, file):
        block_size = ["bytes", "KB", "MB", "GB", "TB"]
        size = len(open(file, "rb").read())
        for bs in block_size:
            lim = 1024
            if size < lim:
                print(f"[+] file size: {size:.2f} {bs}")
                break
            size /= lim

f = args.file
b = args.byte
c = args.char
w = args.word
l = args.line
s = args.size
v = args.version

if f:
    if len(sys.argv) - 2 <= 1: # comparing given arguments count
        d = Data(f)
        d.byte(f); d.char(); d.word(); d.line(); Size(f)
    else:
        d = Data(f)
        if b:
            d.byte(f)
        if c:
            d.char()
        if w:
            d.word()
        if l:
            d.line()
        if s:
            Size(f)
elif v:
    print("Sizak 1.0 ")
else:
    parser.print_help()