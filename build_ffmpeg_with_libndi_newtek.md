# Building ffmpeg with libndi_newtek

## IMPORTANT NOTE
libndi_newtek support was removed from ffmpeg due to a GPL Violation. As a result, the latest version that supports libndi_newtek is ffmpeg 4.1.5. 
If you are looking to take advantage of the latest features of ffmpeg, such as new hardware encoder offloading support, you will not receive
support from the ffmpeg team. 

In addition, the output of this build process requires the --include-nonfree flag, which produces a binary that is not compatible for distribution 
according to ffmpeg's license. You MAY NOT distribute the outputted binaries in your software. 

## How to build.

You will need:
* The NDI SDK for Linux (available from https://ndi.tv/sdk/).
* ffmpeg source from version 4.1.5. 
* build tools for your system
  * Your OS distro's build tools package may not include an asm compiler. You will need one. Output from `configure` will help you pull a compatible compiler. 
* libx264 development headers (for Ubuntu, this was the apt package `libx264-devel`)

Steps to build:
1. Install the NDI SDK.
2. Install the NDI headers and libraries on your system.
  * For my system, this meant copying contents of the `lib` directory to `/lib/`, and copying `include/*` to `/usr/include`. You may need to pick a different architecture depending on your system.
3. Clone the ffmpeg source.
4. In the ffmpeg directory, run `./configure` with the arguments `--enable-nonfree --enable-libndi_newtek --enable-gpl --enable-libx264`
5. Run `make` from the ffmpeg directory. 

