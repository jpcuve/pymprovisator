from pathlib import Path
from time import sleep

import mido

from pymprovisator.music import CHORD_ARPEGGIO

def play():
    output_names = mido.get_output_names()
    print(output_names)
    outport = mido.open_output(output_names[0])
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


if __name__ == '__main__':
    # test from original
    # chords = ['4C7', '2Dm7', '2G7alt', '4Cm7', '4F7', '8Bbmaj7#11']
    output_names = mido.get_output_names()
    outport = mido.open_output(output_names[0])
    channel = 1
    chords = [(4, 60, '7'), (2, 62, 'm7'), (2, 67, '7alt'), (4, 60, 'm7'), (4, 65, '7'), (8, 70, 'maj7#11')]
    tempo = 0.3
    for duration, note, chord in chords:
        arpeggio = CHORD_ARPEGGIO.get(chord)
        for offset in arpeggio:
            outport.send(mido.Message('note_on', channel=channel, note=note + offset, velocity=100))
        sleep(tempo * duration)
        for offset in arpeggio:
            outport.send(mido.Message('note_off', channel=channel, note=note + offset))

