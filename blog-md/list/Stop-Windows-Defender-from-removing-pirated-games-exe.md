Before doing anything, go into Windows Defender and **TURN OFF** `Real Time Protection`.

Open a `Command Prompt (Open As Administrator)`

Make a directory `C:\Temp` and operate from that directory.

Then at the command prompt you can use:

```bat
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -restore -listall
```

... to see what is in quarantine.

And then,

```bat
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -restore -all -Path c:\temp
```
... to restore everything to the `C:\Temp` directory.


Move your recovered files to where you want them.

Then, in `Windows Virus and Threat protection`, go to `Virus & threat prtection settings` -> `Manage Settings`.

Then down to `Exclusions`, and `add Folder and File level exclusions` to ensure your file doesn't get quarantined again.

Then **TURN ON** `Real Time Protection`. 

<sub><sup>didnt come up with this, i found this on the internet and lost the link</sup></sub>
