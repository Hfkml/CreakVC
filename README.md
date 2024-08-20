<div style="text-align: center;">
  <img width="559" alt="image" style="margin-bottom: 50px;" src="https://github.com/user-attachments/assets/c7aa5d36-999f-41ef-99c2-dc7947430cbd">
</div>

<br>

**CreakVC** is a tool based on [FreeVC](https://github.com/OlaWod/FreeVC) for researching the voice quality known as creaky voice or vocal fry. It additionally uses [creapy](https://gitlab.tugraz.at/speech/creapy) for measuring creak and plotting. 
CreakVC is able to take any good-quality single-speaker speech input and modify the degree of creaky voice present in the audio.  

# Abstract
We introduce a human-in-the-loop one-shot voice conversion
tool called CreakVC designed to modulate the level of creaky
voice in the converted speech. Creaky voice, often used by
speakers to convey sociolinguistic cues, presents challenges to
speech processing due to its complex phonation characteristics.
The primary goal of CreakVC is to enable in-depth research
into how these cues are perceived, using systematic perceptual
studies. CreakVC provides access to a diverse range of voice
identities exhibiting creaky voice, while maintaining consis-
tency in other parameters. We developed a spectrogram-frame
level creak representation using CreaPy and finetuned FreeVC,
a one-shot voice conversion tool, by conditioning the speaker
embedding and the self-supervised audio representation with
the creak representation. An integrated plotting feature allows
users to visualize and manipulate portions of speech for pre-
cise adjustments of creaky phonation levels. Beyond research,
CreakVC has potential applications in voice-interactive systems
and multimedia production.

CreakVC requires the following in order to work:
* Clone the CreakVC repository ````git clone https://github.com/Hfkml/CreakVC/````
* Download the CreakVC checkpoint
* Download [WavLM](https://github.com/microsoft/unilm/tree/master/wavlm) and save it in the folder ````wavlm/````
* Download the pretrained G_CreakVC.pth model from the Github release
* Open CreakVC.ipynb
* Watch [this video](https://play.kth.se/media/Show%20and%20Tell%20/0_hpyq9vy1) for instructions
