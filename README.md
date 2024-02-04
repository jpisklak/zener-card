# Zener Card Replication Program: zener.py

This Python program runs a computerized replication of the well-known Zener Card studies originally conducted by Dr. J.B. Rhine. In this simulation, Zener cards are substituted with the numbers 1, 2, 3, 4, and 5.

## Background
Dr. J.B. Rhine's original studies aimed to explore specific types of extra-sensory perception (ESP), defined as "perception without the function of the recognized senses." One intriguing aspect investigated was *precognition* - the alleged ability to perceive and predict events that would occur in the future.

Despite Rhine's claims of discovering evidence for such phenomena in his book [Extrasensory Perception](https://archive.org/embed/extrasensoryperc0000rhin_j6u0), his methodology has faced significant criticism, and subsequent attempts to replicate his results have proven challenging. Nevertheless, a persistent belief in the possibility of extraordinary powers, including precognition, continues to capture the imagination of many.

## Features
- Conduct as many or as few trials as desired.
- Provides statistical analysis of results.
- Evaluates whether the user demonstrates precognitive abilities using a decision criteria of $\alpha = 0.05$.
- Saves results to the user's computer in graphical and spreadsheet (.csv) formats.

## Requirements
- `sys`
- `datetime`
- `textwrap`
- `numpy`
- `pandas`
- `matplotlib.pyplot`
- `scipy.stats`

## Standard Usage
1. Download `zener.py` to your local machine.
2. Install the required Python packages using your preferred package manager (e.g., pip, conda).
3. Run the program and follow the on-screen instructions to complete trials.
4. View statistical results and saved files on your computer.

## Run Online via Google Colaboratory
1. Go to https://colab.research.google.com/drive/1xxmxVQDdg4JtRaJl35ucXCUVbuoFVMiB?usp=sharing
2. Save a copy of the Colab notebook to your Google Drive account.
3. Open the notebook from your Googel Drive account and run it by slecting the *Runtime* menu and *Run All*.
4. The graph and data file can be obtained by clicking the file folder on the left side of Google Colab once the test is complete.

## Additional Information
Rhine's original book, *Extrasensory Perception*, can be accessed here: https://archive.org/embed/extrasensoryperc0000rhin_j6u0
