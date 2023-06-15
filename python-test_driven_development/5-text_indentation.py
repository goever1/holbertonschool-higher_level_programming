#!/usr/bin/python3
"""
defining a tect identation function
"""


def text_indentation(text):
    """
    prints a tec¿xt with 2 new lines.
    Arguments:
        dataype:
    Raises:
        TypeError (text): text must be a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if  text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
                continue
        i += 1
