#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Pymprovisator v. 0.1.1
# This program is free software. See the files LICENSE.TXT and README.TXT for more details
# Written by David Asorey �lvarez (forodejazz@yahoo.es). Madrid (Spain). August 2003.
import json
from pathlib import Path
from typing import Dict

# Default values:
# preferences_file = os.path.join(os.path.expanduser('~'), '.pymprovisator.conf')
# if not os.path.exists(preferences_file):
#     # Simulates the UNIX command 'touch'
#     fp = open(preferences_file, 'w')
#     fp.close()
# prefered_instruments = {'bass': 'Acoustic Bass', 'piano': 'Acoustic Grand Piano'}
# prefered_volume = {'bass': 90, 'piano': 90, 'drums': 90}

DEFAULT_CONFIG_LOCATION = '../config.json'


def load_preferences() -> Dict[str, any]:
    with open(Path(DEFAULT_CONFIG_LOCATION)) as f:
        preferences = json.load(f)
    return preferences


def save_preferences(preferences: Dict[str, any]):
    with open(Path(DEFAULT_CONFIG_LOCATION), 'w') as f:
        json.dump(preferences, f)


def get_preferred_instruments() -> Dict[str, str]:
    preferences = load_preferences()
    preferred_instruments = preferences.get('preferredInstruments', {})
    return {
        'bass': preferred_instruments.get('bass', 'Acoustic Bass'),
        'piano': preferred_instruments.get('piano', 'Acoustic Grand Piano')
    }


def get_preferred_volumes() -> Dict[str, str]:
    preferences = load_preferences()
    preferred_volumes = preferences.get('preferredVolumes', {})
    return {
        'bass': preferred_volumes.get('bass', 90),
        'piano': preferred_volumes.get('piano', 90),
        'drums': preferred_volumes.get('drums', 90)
    }


def get_external_program_paths() -> Dict[str, str]:
    preferences = load_preferences()
    external_program_paths = preferences.get('externalProgramPaths', {})
    return {
        'abc2midi': external_program_paths.get('abc2midi', '/path/to/abc2midi'),
        'midiPlayer': external_program_paths.get('midiPlayer', '/path/to/a/midiplayer')
    }


def set_defaults():
    preferences = {
        'preferredInstruments': get_preferred_instruments(),
        'preferredVolumes': get_preferred_volumes(),
        'externalProgramPaths': get_external_program_paths()
    }
    save_preferences(preferences)


# def get_prefered_instruments():
#     prefs = prefered_instruments
#     if os.path.exists(preferences_file):
#         parser = ConfigParser.ConfigParser()
#         file = open(preferences_file, 'r')
#         parser.readfp(file)
#         if parser.has_section('PREFERED_INSTRUMENTS'):
#             prefs['piano'] = parser.get('PREFERED_INSTRUMENTS', 'piano')
#             prefs['bass'] = parser.get('PREFERED_INSTRUMENTS', 'bass')
#             file.close()
#     return prefs
#
# def set_prefered_instruments(pr_inst=prefered_instruments):
#     parser = ConfigParser.ConfigParser()
#     if os.path.exists(preferences_file):
#         file = open(preferences_file, 'r')
#         parser.readfp(file)
#         file = open(preferences_file, 'w')
#         if not parser.has_section('PREFERED_INSTRUMENTS'):
#             parser.add_section('PREFERED_INSTRUMENTS')
#     else:
#         file = open(preferences_file, 'w')
#         parser.readfp(file)
#         parser.add_section('PREFERED_INSTRUMENTS')
#     parser.set('PREFERED_INSTRUMENTS', 'piano', pr_inst['piano'])
#     parser.set('PREFERED_INSTRUMENTS', 'bass', pr_inst['bass'])
#     parser.write(file)
#     file.close()
#
# def get_prefered_volume():
#     prefs = prefered_volume
#     if os.path.exists(preferences_file):
#         parser = ConfigParser.ConfigParser()
#         file = open(preferences_file, 'r')
#         parser.readfp(file)
#         if parser.has_section('PREFERED_VOLUME'):
#             prefs['piano'] = parser.getint('PREFERED_VOLUME', 'piano')
#             prefs['bass'] = parser.getint('PREFERED_VOLUME', 'bass')
#             prefs['drums'] = parser.getint('PREFERED_VOLUME', 'drums')
#             file.close()
#     return prefs
#
# def set_prefered_volume(pr_vol=prefered_volume):
#     parser = ConfigParser.ConfigParser()
#     if os.path.exists(preferences_file):
#         file = open(preferences_file, 'r')
#         parser.readfp(file)
#         file = open(preferences_file, 'w')
#         if not parser.has_section('PREFERED_VOLUME'):
#             parser.add_section('PREFERED_VOLUME')
#     else:
#         file = open(preferences_file, 'w')
#         parser.readfp(file)
#         parser.add_section('PREFERED_VOLUME')
#     parser.set('PREFERED_VOLUME', 'piano', str(pr_vol['piano']))
#     parser.set('PREFERED_VOLUME', 'bass', str(pr_vol['bass']))
#     parser.set('PREFERED_VOLUME', 'drums', str(pr_vol['drums']))
#     parser.write(file)
#     file.close()
#
#
#
#
#
#
# def get_external_prog_path(variable):
#     if os.path.exists(preferences_file):
#         parser = ConfigParser.ConfigParser()
#         file = open(preferences_file, 'r')
#         parser.readfp(file)
#         if parser.has_option('PATHS', variable):
#             file.close()
#             return parser.get('PATHS', variable)
#     return ''
#
# def set_external_prog_path(variable, path):
#     parser = ConfigParser.ConfigParser()
#     if os.path.exists(preferences_file):
#         file = open(preferences_file, 'r')
#         parser.readfp(file)
#         file = open(preferences_file, 'w')
#         if not parser.has_section('PATHS'):
#             parser.add_section('PATHS')
#     else:
#         file = open(preferences_file, 'w')
#         parser.readfp(file)
#         parser.add_section('PATHS')
#     parser.set('PATHS', variable, path)
#     parser.write(file)
#     file.close()
#
# def set_defaults():
#     set_prefered_instruments()
#     set_prefered_volume()
#     set_external_prog_path('ABC2MIDI', '/path/to/abc2midi')
#     set_external_prog_path('MIDIPLAYER', '/path/to/a/midiplayer')


if __name__ == '__main__':
    # set_defaults()
    print(get_preferred_instruments())
    print(get_preferred_volumes())
    print(get_external_program_paths())
    set_defaults()
