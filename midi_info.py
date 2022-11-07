from pathlib import Path
from time import sleep

import mido

from pymprovisator.chord import Chord
from pymprovisator.music import CHORD_ARPEGGIO
from pymprovisator.track import Track

CHORDS = [(4, 60, '7'), (2, 62, 'm7'), (2, 67, '7alt'), (4, 60, 'm7'), (4, 65, '7'), (8, 70, 'maj7#11')]


def play(outport):
    channel = 1
    with open(Path('gm_patches.txt')) as f:
        for index, line in enumerate(f.readlines()):
            patch_name = line.strip()
            print(patch_name)
            outport.send(mido.Message('program_change', channel=channel, program=index))
            for note in [60, 62, 64, 65, 67, 69, 71, 72]:
                outport.send(mido.Message('note_on', channel=channel, note=note, velocity=100))
                sleep(0.5)
                outport.send(mido.Message('note_off', channel=channel, note=note))


def play_sequence(outport):
    channel = 1
    tempo = 0.3
    for duration, note, scale in CHORDS:
        arpeggio = CHORD_ARPEGGIO.get(scale)
        for offset in arpeggio:
            outport.send(mido.Message('note_on', channel=channel, note=note + offset, velocity=100))
        sleep(tempo * duration)
        for offset in arpeggio:
            outport.send(mido.Message('note_off', channel=channel, note=note + offset))
    for duration, note, scale in CHORDS:
        chord = Chord(note, scale)
        for n in chord.arpeggio:
            outport.send(mido.Message('note_on', channel=channel, note=n, velocity=100))
        sleep(tempo * duration)
        for n in chord.arpeggio:
            outport.send(mido.Message('note_off', channel=channel, note=n))


def play_track(outport):
    # first we build the track
    track = Track()
    time = 0
    for duration, note, scale in CHORDS:
        track.punch_chord([note + o for o in CHORD_ARPEGGIO.get(scale)], time, duration)
        time += duration
    # then we play the track
    channel = 1
    tempo = 0.3
    for tick in range(time):
        for n in track.note_on[tick]:
            outport.send(mido.Message('note_on', channel=channel, note=n, velocity=100))
        for n in track.note_off[tick]:
            outport.send(mido.Message('note_off', channel=channel, note=n))
        sleep(tempo)


if __name__ == '__main__':
    # test from original
    # chords = ['4C7', '2Dm7', '2G7alt', '4Cm7', '4F7', '8Bbmaj7#11']
    output_names = mido.get_output_names()
    outport = mido.open_output(output_names[0])
    play_track(outport)
