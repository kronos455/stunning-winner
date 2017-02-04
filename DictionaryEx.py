# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:41:27 2017

@author: bmitchell
"""

def main():
    d = {}
    d["spam"] = 3
    print(d)
    d.update({"spam":1, "eggs":2})
    print(d)
    print("d has", len(d), "items")
    print("eggs" in d)
    print("keys:", list(d.keys()))
    print("values:", list(d.values()))
    for key in d:
        print(key, d[key])
    print(d.get("toast", "not in dictionary"))
    del(d["eggs"])
    print(d)

main()