<h1>Wavblend (A Tool for Music Producers) - WIP</h1>

This is the beta version of Wavblend, a Python script for merging multiple .wav files built on top of the pydub library. Given a set of .wav files, Wavblend will generate and merge all possible subsets of your files. The main merging function makes use of a modified recursive powerset algorithm - time complexity of O(2^n - (n - 1)) - so don’t try and merge a powerset of 200 files at once or you’re going to be waiting for the process to finish until you die. Literally.

Requirements:
- Python 3.x
- pydub
- tqdm

<i>- JudGe</i>

