# KITTDisplayTalk
Application in Python to let your KITT-Replica talk for a specific time, while standing on an Exhibition.

It offers you the possibility to personalize it's features, using a JSON-Config.
And it delivers a script to setup your Python-Environment.

## Requirement:
* Python 3 needs to be installed

# Setup
The setup.sh is going to set up your Python-Environment so that you can start the Application without any issues. 

Be aware of, that it only installs `pip` (Pythons own Package-Manager) on your System. The Python-Installation needs to be done by yourself.

To start the setup run following command in your terminal in the Application-Folder

```bash
sudo bash setup.sh
```
The Script now sets up the Environment and after that you can start configure the Application.


# Config

I think it's pretty self-explaining but just a few informations regarding the `repeat_duration` and the `audio_break`:

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

# Starting the Application
When configured the Application can be started by using the start.sh or entering following command in your bash:

```bash
bash start.sh -d
```