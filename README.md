# KITTDisplayTalk
Application in Python to let your KITT-Replica talk for a specific time, while standing on an Exhibition.

It offers you the possibility to personalize it's features, using a JSON-Config.

It think is pretty self-explaining just a few informations regarding the `repeat_duration` and the `audio_break`:

- the unit for `repeat_duration` is minutes. So if you want it to run for 2 hours, you need to enter `120`
- the unit for `audio_break` is seconds. So if you want it to pause for 2 minutes, you need to enter `120`

```json
{
  "display" : {
    "audio_format" : ".mp3",
    "repeat_duration" : 15,
    "audio_break" : 5
  }
}
```
The audiofiles for the Display-Mode are pulled out of the `display_audio`-Folder. So everything, that you want to be played when running the Display-Mode needs to be placed in the specified Folder.