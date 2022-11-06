#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Pymprovisator v. 0.1.1
# This program is free software. See the files LICENSE.TXT and README.TXT for more details
# Written by David Asorey Álvarez (forodejazz@yahoo.es). Madrid (Spain). August 2003.

import json
from pathlib import Path

import song


def load_song(file_name: str):
    with open(Path(file_name)) as f:
        data = json.load(f)
        return song.Song(
            data['id'],
            data['title'],
            data['tempo'],
            data['key'],
            data['style'],  # TODO enum
            data['inputChords'],
            data['nBars'],
            data['nChoruses'],
            data['activeInstruments']
        )


def save_song(file_name: str, song: song.Song):
    with open(Path(file_name), 'w') as f:
        json.dump({
            'id': song.id,
            'title': song.title,
            'tempo': song.tempo,
            'key': song.key,
            'style': song.style,
            'chords': ' '.join(song.chord_seq),
            'nBars': song.n_bars,
            'nChoruses': song.n_choruses,
            'activeInstruments': ' '.join(song.instruments)
        }, f)

# def load_song(fs):
#     parser = ConfigParser.ConfigParser()
#     try:
#         parser.readfp(open(fs))
#         id = parser.get('SONG', 'id')
#         title = parser.get('SONG', 'title')
#         tempo = parser.get('SONG', 'tempo')
#         key = parser.get('SONG', 'key')
#         style = parser.get('SONG', 'style')
#         chords = parser.get('SONG', 'chords')
#         n_bars = parser.get('SONG', 'n_bars')
#         n_choruses = parser.get('SONG', 'n_choruses')
#         active_instruments = parser.get('SONG', 'active_instruments')
#         input_chords = string.split(chords)
#         input_instruments = string.split(active_instruments)
#         return song.Song(id, title, tempo, key, eval('song.' + style), input_chords, n_bars, n_choruses, input_instruments)
#     except:
#         #~ print e
#         return None
# def save_song(fs, song):
#     parser = ConfigParser.ConfigParser()
#     try:
#         aux = open(fs, 'w')
#         parser.readfp(aux)
#         parser.add_section('SONG')
#         parser.set('SONG', 'id', song.id)
#         parser.set('SONG', 'title', song.title)
#         parser.set('SONG', 'tempo', song.tempo)
#         parser.set('SONG', 'key', song.key)
#         parser.set('SONG', 'style', song.style.name)
#         parser.set('SONG', 'chords', ' '.join(song.chord_seq))
#         parser.set('SONG', 'n_bars', song.n_bars)
#         parser.set('SONG', 'n_choruses', song.n_choruses)
#         parser.set('SONG', 'active_instruments', ' '.join(song.instruments))
#         parser.write(aux)
#         return 1
#     except Exception as e:
#         print(e)
#         return 0
