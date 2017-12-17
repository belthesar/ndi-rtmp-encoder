# NDI Encoder Appliance

## Pre-requisites
* Python 2.7
* ffmpeg compiled with NDI support
    * I will be providing instructions on how to do this at a later date. 
    * Install your FF binaries into a locale 
* avahi
    * NDI is dependent on zeroconf support. This can be provided with avahi
* You may need to disable reverse packet filtering on you network interfaces. 

## Arguments

* no arguments:
    * return all arguments
* show_ndi_sources:
   * return a list of all the NDI sources the encoder can see
* broadcast /path/to/profile.json
    * start a broadcast using the specified profile config file 
* show_presets:
    * return a list of all the built in encoder presets as defined in settings/encoderPresets.json

## Notes
This was developed against Ubuntu 16.04 and has not been tested on any other OS. I don't 

## Getting Started

To create a profile, copy the profile.example.json file to a new file, and change the settings as approriate for your stream.  

## Running as a service
Instructions on how to do this will be provided soon.