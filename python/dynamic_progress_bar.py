#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import os

def get_terminal_size(values='xy'):
    """ Get Terminal window size

    Original source-code by Johannes Weiß, chown
    https://stackoverflow.com/questions/566746/how-to-get-linux-console-window-width-in-python
    """
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            import struct
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    if values == 'x':
        return int(cr[1])
    elif values == 'y':
        return int(cr[0])
    else:
        return int(cr[1]), int(cr[0])



def print_progress_bar(iteration, total, prefix='Progress:', suffix='', decimals=1, length=None, fill='█', background=' '):
    """ Text-based progress bar for Terminal/CLI.

    Generate progress bar out of a loop.

    Example:
        Progress: [█████████████████████████████████████████████    ] 90.0%

    Args:
        iteration (int): Current iteration
        total (int): Total iterations

        prefix (str): Prefix string
        suffix (str): Suffix string
        decimals (int): Posetive number of decimals in percent complete
        length (int): Characher length of bar
        fill (str): Characher for progress filling
        background (str): Background characher of progressbar

    Notes:
        Function is a modified version of the function originally written
        by Greenstick.
        https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """

    # Calculate width of terminal (if no width is specified)
    if length is None:
        length = get_terminal_size('x') - 10 - len(prefix) - len(suffix) - int(decimals)

    # Progress bar execution
    string = "{0:." + str(decimals) + "f}"
    percent = string.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    progress_bar = (fill * filled_length + background * (length - filled_length))
    print('\r%s [%s] %s%% %s' % (prefix, progress_bar, percent, suffix), end='\r')

    # Add new line on last iteration
    if iteration == total:
        print()


# Example code
items = list(range(0, 57))
print_progress_bar(0, len(items))
for i, item in enumerate(items):
    time.sleep(0.05)
    print_progress_bar(i + 1, len(items))
