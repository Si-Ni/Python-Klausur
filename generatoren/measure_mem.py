#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Measure memory of current process.
"""

import os
import psutil


def measure_own_memory(unit='MB'):
    """Measure memory of current process.

    Returns memory with given unit one of B, KB, MB, or GB,
    defaults to MB.
    """
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3
        }
    fact = units[unit]
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / fact, unit


def show_memory(unit='MB'):
    """Print memory usage of current process,
    """
    value, unit = measure_own_memory(unit)
    print('Memory usage: {} {}'.format(value, unit))


if __name__ == '__main__':
    show_memory()
