#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import student

    
if __name__ == '__main__':
    count = 0
    while True:
        command = input("Что вы хотите? ").lower()

        if command == "exit":
            break
        elif command == "add":
            student.add()
        elif command == "list":
            student.list()
        elif command == "select":
            student.select()
        elif command == "help":
            student.help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)