#!/usr/bin/env python3 
import subprocess
import json
import sys
import os
import codecs

def ffmpeg_check_sources(dummyArg=None):
    subprocess.check_call(['ffmpeg', '-f', 'libndi_newtek', '-find_sources', '1', '-i', 'dummy'])

def ffmpeg_encode(framerate=30, resolution="1280x720", intVideoBitrate=3, audioBitrate="128k", x264Preset = "veryfast", ndiSource=None, rtmpStream=None):
    if not ndiSource or not rtmpStream:
        print("NDI Source or RTMP URI not specified. Exiting.")
        sys.exit(1)
    else:
        videoBitrate = str(intVideoBitrate) + "M"
        videoBuffer = str(intVideoBitrate*2) + "M"
        ffmpeg_encode_args = ['ffmpeg', '-f', 'libndi_newtek', '-i', 
        ndiSource, '-r', str(framerate), '-g', str(framerate*2), '-keyint_min', str(framerate), 
        '-s', resolution, '-pix_fmt', 'yuv420p', '-c:v', 'libx264', 
        '-ac', '2', '-ar', '44100', '-c:a', 'aac', '-b:a', audioBitrate,
        '-b:v', videoBitrate, '-minrate', videoBitrate, '-maxrate', videoBitrate, '-bufsize', videoBuffer,
        '-x264-params', 'nal-hrd=cbr', '-preset', x264Preset, '-f', 'flv', '-threads', '0', rtmpStream]
        subprocess.call(ffmpeg_encode_args)

def broadcast(encoderProfileFile):
    # Grabs the contents of the profile, and launches the broadcast with ffmpeg_encode
    if not encoderProfileFile:
        print("No encoder profile specified, exiting.")
        sys.exit(2)
    else:
        with open(encoderProfileFile) as fileEncoderProfileFile:
            encoderProfile = json.load(fileEncoderProfileFile)
        with open(encoderSettings['encoderPresetsPath']) as fileEncoderPresets:
            encoderPresets = json.load(fileEncoderPresets)
        encoderPreset = encoderPresets[encoderProfile['encoderPreset']]
        ffmpeg_encode(
            framerate=encoderPreset['framerate'], 
            resolution=encoderPreset['resolution'], 
            intVideoBitrate=encoderPreset['videoBitrate'], 
            audioBitrate=encoderPreset['audioBitrate'], 
            x264Preset=encoderPreset['x264Preset'], 
            ndiSource=encoderProfile['ndiSourceName'], 
            rtmpStream=encoderProfile['rtmpStream']
            )

def show_presets(dummyArg=None):
    with open(encoderSettings['encoderPresetsPath']) as fileEncoderPresets:
        encoderPresets = json.load(fileEncoderPresets)
    print("Available Presets to use:")
    for preset, presetSettings in encoderPresets.items():
        print(preset)
        print("  " + presetSettings['description'])
    sys.exit(0)

def encoder_help(dummyArg=None):
    return showArguments()

appArguments = {
    'show_ndi_sources': {
        'func': ffmpeg_check_sources,
        'instructions': 'This lists the NDI source available to the encoder to choose from. To use, create a encoder configuration that specifies this NDI source (see example.json for details)'
    },
    'broadcast': {
        'func': broadcast,
        'instructions': 'This begins a broadcast. Must supply an encoder profile to provide settings for the broadcast.  See the readme for more info.'
    },
    'show_presets': {
        'func': show_presets,
        'instructions': 'This provides the names of all the encoder presets you can use in an encoder profile. You may review the individual settings, as well as create your own encoder preset by opening the file at ./settings/encoderPresets.json'
    },
    'help': {
        'func': encoder_help,
        'instructions': 'This help message.'
    }
}

def showArguments(args=appArguments):
    # Returns instructions for how to use the encoder, then exits.
    # print("Either no arguments were specified, or there was a syntax error. Showing help.")
    for arg, argdict in args.items():
        print(arg + ": " + argdict['instructions'])
    sys.exit(0)  

if __name__ == "__main__":
    print("NDI to RTMP Encoder")
    with open("encoderSettings.json") as fileEncoderSettings:
        encoderSettings = json.load(fileEncoderSettings)

    if len(sys.argv) > 1:
        if sys.argv[1] in appArguments:
            appMode = appArguments[sys.argv[1]]['func']
        # appMode = appArguments.get(sys.argv[1],showArguments(appArguments))['func']
    else:
        print("No arguments specified, showing help.")
        showArguments()
    if len(sys.argv) > 2:
        appMode(sys.argv[2])
    else:
        appMode(None)
    

