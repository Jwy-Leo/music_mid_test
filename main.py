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
    midi_file = Change_instrument(args)
    PlayMusic(args, midi_file)
    
    #Two_ins_play(args, midi_file)

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
    import pdb;pdb.set_trace()
    Is = ['BaritoneSaxophone', 'Bass', 'BassClarinet', 'BassDrum', 'BassTrombone', 'Bassoon', 'BongoDrums', 'BrassInstrument', 'Castanets', 'Celesta', 'ChurchBells', 'Clarinet', 'Clavichord', 'CongaDrum', 'Contrabass', 'Cowbell', 'CrashCymbals', 'Cymbals', 'Dulcimer', 'ElectricBass', 'ElectricGuitar', 'ElectricOrgan', 'EnglishHorn', 'FingerCymbals', 'Flute', 'FretlessBass', 'Glockenspiel', 'Gong', 'Guitar', 'Handbells', 'Harmonica', 'Harp', 'Harpsichord', 'HiHatCymbal', 'Horn', 'Instrument', 'InstrumentException', 'Kalimba', 'KeyboardInstrument', 'Koto', 'Lute', 'Mandolin', 'Maracas', 'Marimba', 'MezzoSoprano', 'Oboe', 'Ocarina', 'OrderedDict', 'Organ', 'PanFlute', 'Percussion', 'Piano', 'Piccolo', 'PipeOrgan', 'PitchedPercussion', 'Ratchet', 'Recorder', 'ReedOrgan', 'RideCymbals', 'SandpaperBlocks', 'Saxophone', 'Shakuhachi', 'Shamisen', 'Shehnai', 'Siren', 'Sitar', 'SizzleCymbal', 'SleighBells', 'SnareDrum', 'Soprano', 'SopranoSaxophone', 'SplashCymbals', 'SteelDrum', 'StringInstrument', 'SuspendedCymbal', 'Taiko', 'TamTam', 'Tambourine', 'TempleBlock', 'Tenor', 'TenorDrum', 'TenorSaxophone', 'Test', 'TestExternal', 'Timbales', 'Timpani', 'TomTom', 'Triangle', 'Trombone', 'Trumpet', 'Tuba', 'TubularBells', 'Ukulele', 'UnpitchedPercussion', 'Vibraphone', 'Vibraslap', 'Viola', 'Violin', 'Violoncello', 'Vocalist', 'Whip', 'Whistle', 'WindMachine', 'Woodblock', 'WoodwindInstrument', 'Xylophone']
    ISc = vars(instrument)
    #_instru = "Violin"
    #_instru = "Clarinet"
    #_instru = "EnglishHorn"
    #_instru = "Flute"
    _instru = "Organ"
    #_instru = "Whistle"
    #"WoodwindInstrument"
    for p in s.parts:
        p.insert(0, ISc[_instru]())
    s.write('midi', 'temp.mid')
    return "temp.mid"

def play_by_mingus(args):
    from mingus.midi import fluidsynth
    #fluidsynth.init(args.file_src)
    fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2', "alsa")
    fluidsynth.play_Note(64, 0 , 100)

def Two_ins_play(args, midi_file):
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    import pdb;pdb.set_trace()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(args.file_src)) 
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(midi_file))
    input("press to exit")

if __name__ == "__main__":
    args = arguments()
    main(args)
