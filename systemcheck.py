#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Systemcheck.py

    A multi-usage systemcheck file to give the user or the administrator a quick
    system check. Made for FreeBSD, the option of devleoping it in python
    instead of a shell-script was because I wanted to learn python more, and was
    a cleaner result. Copyright 2010. MIT License.

"""
import subprocess
import collections

user_info = collections.defaultdict()
user_info['1-System Information'] = {
    "01-Operating System": "uname -sr",
    "02-Architecture"    : "uname -p",
    "03-Kernel modules"  : "kldstat | grep -vE '^USER|ps -aux'| wc -l",
    "04-CPU"             : "sysctl -a | egrep -i 'hw.model' | sed -r 's/^.{10}//' | cut -c 1-30",
    "05-CPU Cores"       : "sysctl -a | egrep -i 'hw.ncpu' | sed -r 's/^.{9}//'",
    "06-CPU Load"        : "uptime | awk -F'averages:' '{ print $2 }'",
    "07-Processes"       : "ps -aux | wc -l"
}
user_info['2-Network Information'] = {
   "01-Gateway"          : "netstat -r | grep 'default' | awk {' print $2 '}",
   "02-IP Internal"      : "/sbin/ifconfig -a | awk '/(cast)/ { print $2 }'",
   "03-IP External"      : "curl --silent ifconfig.me/ip",
   "04-Hostname"         : "hostname"
}
user_info['3-User Information'] = {
    "01-User"            : "echo $(id -un) '(ID: '$(id -u)')'",
    "02-Date"            : "date '+%Y-%m-%d% %H:%M:%S'"
}

def exec_command(cmd):
    """ Execute shell command

        Args:
            cmd: shell command to execute

        Returns:
            return: value of executed command, if the command fails to be
                    executed, then return string with value 'None'
    """
    try:
        return(subprocess.check_output(cmd, shell=True)).strip().decode(errors="ignore")
    except:
        return("None")


def get_information(info):
    """ Crawl information from list collection dict


        Retries a list collection of category dicts with key and values from
        'info'. Information gets processed, values get executed as shell
        commands and then printed out as category-title and key-values in a
        column view for easy readability.

        Args:
            info: A list with collection of dicts with commands

        Returns:
            data: A list of row with title and values.

    """

    # Store all data in a list
    data = []

    # Crawl data for each category dict that will append to the data list
    for category in sorted(info):

        # Temporary category data list
        tmp = []

        # Category title
        data.append("\n- "+category[2:].upper()+"\n")

        # Crawl information with title and executed command as value
        for title, command in sorted(info[category].items()):
            tmp.append([title[3:], exec_command(command)])

        # Add category data rows to data
        for row in tmp:
            data.append("".join(value.ljust(max(len(value) for row in tmp for value in row)) for value in row))

    # Return list with executed values
    return(data)

def main():

    # Notify the user about information is now loading, some network
    # tasks can take a little while
    print('Reciving information...')

    # Print user accessable information
    for data in get_information(user_info):
        print(data)

if __name__ == '__main__':
    main()
