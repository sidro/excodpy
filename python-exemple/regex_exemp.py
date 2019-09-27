import re

def parse_bytes(string): 
     parser = re.compile(r"\b[01]{8}\b") 
     res = parser.findall(string) 
     print(res)

parse_bytes("my bytes are 10101010 10001111 10010111110001 gg")