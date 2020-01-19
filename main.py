import os
import argparse
from mido import MidiFile
import mido
import pygame
from music21 import converter, instrument

def arguments():
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-FS", "--file_src", type=str, default="resource/Gurenge_full.mid")

    args = parser.parse_args()
    print(args)

    return args

def main(args):
    # more realistic approach
    
    # play_by_mingus(args)
    # eletronic approach
    
    PlayMusic(args)
    # midi_file = Change_instrument(args)
    # PlayMusic(args, midi_file)
    

    '''
    mid_file = MidiFile(args.file_src, clip=True)
    #port = mido.open_output("SH-201")#Integra-7")
    port = mido.open_output("Midi Through:Midi Through Port-0 14:0")#"Integra-7")
    import pdb;pdb.set_trace()
    for msg in mid_file.play():
        print(msg)
        port.send(msg)
    port.close()
    print(mid_file)
    '''
    pass

def PlayMusic(args, midi_file=None):
    open_file = args.file_src if midi_file is None else midi_file
    print(open_file)
    pygame.init()
    pygame.mixer.music.load(open_file)
    pygame.mixer.music.play()
    input("press to exit")

def Change_instrument(args):
    s = converter.parse(args.file_src)
    for p in s.parts:
        p.insert(0, instrument.Violin())
    s.write('midi', 'temp.mid')
    return "temp.mid"

def play_by_mingus(args):
    from mingus.midi import fluidsynth
    #fluidsynth.init(args.file_src)
    fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2', "alsa")
    fluidsynth.play_Note(64, 0 , 100)
    

if __name__ == "__main__":
    args = arguments()
    main(args)
