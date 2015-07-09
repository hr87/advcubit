"""
Utility functions for controlling Cubit

This module provides general functions to controll settings, load, save and export files
and merging and imprinting
"""

import advcubit.system as _system


def startCubit():
    """ Starts cubit

    :return: None
    """
    _system.cubitModule.init([''])


def enableDeveloperCommands(enabled=True):
    """ Enable the developer commands granting access to advanced beta functionality

    :param enabled: Flag if on or off
    :return: None
    """
    if enabled:
        enabled = 'on'
    else:
        enabled = 'off'
    _system.cubitCmd('set developer commands {0}'.format(enabled))


def enableJournal(enabled=True):
    """ Turn the journal on or off,

    :param enabled: Flag if on or off
    :return:
    """
    if enabled:
        enabled = 'on'
    else:
        enabled = 'off'
    _system.cubitCmd('journal {0}'.format(enabled))


def newFile():
    """ Creates an empty workspace

    :return: None
    """
    _system.cubitCmd('reset')


def open(fileName):
    """ Open a Cubit format file

    :param fileName: File path to open
    :return: None
    """
    _system.cubitCmd('open {0}'.format(fileName))


def save(fileName, overwrite=True):
    """ Saves the current file to Cubit format

    :param fileName: File name to save to
    :param overwrite: Flag if existing files is to overwrite
    :return: None
    """

    if overwrite:
        _system.cubitCmd('save as "{0}" overwrite'.format(fileName))
    else:
        _system.cubitCmd('save as "{0}"'.format(fileName))


def export(filename, overwrite=True):
    """ Export to external format

    :param filename: path to export to
    :param overwrite: flag if to everwrite existing file
    :return: None
    """
    _system.cubitCmd('export mesh "{0}" overwrite'.format(filename))
