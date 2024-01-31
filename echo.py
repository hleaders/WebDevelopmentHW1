# -*- coding: utf-8 -*-

def echo(text: str, repetitions: int = 3) -> str:
    result = ""
    for i in reversed(range(repetitions)):
        result +=  (text[-i - 1:]) + "\n"
    result += "."
    return result


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
