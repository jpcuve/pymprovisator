from time import sleep

import mido

if __name__ == '__main__':
    output_names = mido.get_output_names()
    print(output_names)
    outport = mido.open_output(output_names[0])
    channel = 1
    for note in [60, 62, 64, 65, 67, 69, 71, 72]:
        outport.send(mido.Message('note_on', channel=channel, note=note, velocity=100))
        sleep(0.5)
        outport.send(mido.Message('note_off', channel=channel, note=note))
