## Building a 'Metallica-Detecting' TensorFlow Neural Network ##

Neural network in TensorFlow to categorise music as either 'Metallica' and 'R.E.M'.

### Usage

```bash
python train_model.py
```

At the prompt, provide a directory where labelled mp3 music files can be found:

```bash
Metallica - Fade To Black.mp3
Metallica - Master Of Puppets.mp3
R.E.M. - Everybody Hurts.mp3
R.E.M. - Losing My Religion.mp3
```

WAV file chunks of each audio recording will also be generated in this same folder.

### Requirements

Required python packages (may have other associated dependencies):

```bash
sudo pip install tensorflow tflearn pydub scipy numpy

```