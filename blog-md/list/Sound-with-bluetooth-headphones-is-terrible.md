When you have some app accessing the microphone in MacOS and you have Bluetooth headphones connected, the audio will sound terrible.

You can see why when opening the "Audio Midi Setup" app and selecting the headphones. The format will probably be 1ch 16000 Hz, it should be 2ch 44000Hz, so change it!

If it refuses to change, go to the "Activity Monitor" app, search for "coreaudiod" and force quit the process, it'll restart automatically and apply the correct setting. This seems to be the same correcting behaviour turning off the headphones, opening the app that access the microphone and then connecting the bluetooth headphones again, just less cumbersome.
