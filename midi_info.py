from time import sleep

import mido

from pymprovisator.chord import Chord
from pymprovisator.track import Track
from pymprovisator.tune import Sample

SAMPLES = [
    Sample(4, Chord(60, '7')),
    Sample(2, Chord(62, 'm7')),
    Sample(2, Chord(67, '7alt')),
    Sample(4, Chord(60, 'm7')),
    Sample(4, Chord(65, '7')),
    Sample(8, Chord(70, 'maj7#11')),
]


def play_track(midi_outport):
    # first we build the track
    track = Track()
    time = 0
    for sample in SAMPLES:
        track.punch_chord(sample.chord.arpeggio, time, sample.duration)
        time += sample.duration
    # then we play the track
    channel = 1
    tempo = 0.3
    midi = track.to_midi(channel)
    for tick in range(time):
        for message in midi[tick]:
            midi_outport.send(message)
        sleep(tempo)



if __name__ == '__main__':
    # test from original
    # chords = ['4C7', '2Dm7', '2G7alt', '4Cm7', '4F7', '8Bbmaj7#11']
    output_names = mido.get_output_names()
    outport = mido.open_output(output_names[0])
    play_track(outport)
