# NDI Encoder Appliance

## Pre-requisites
* Python 
* ffmpeg compiled with NDI support
    * To build your own, see [Building ffmpeg with libndi_newtek support](build_ffmpeg_with_libndi_newtek.md)
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
This was developed against Ubuntu 19.10. YMMV on other OSes. 

## Getting Started

To create a profile, copy the profile.example.json file to a new file, and change the settings as approriate for your stream.  

## Running as a service
I've had good experience with running this w/ systemd. 
