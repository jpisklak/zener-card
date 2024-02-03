# zener.py

This basic Python program runs a simple computerized replication of the (in)famous Zener Card studies conducted by Dr. J.B. Rhine. Rhine's original studies were designed to evaluate specific types of extra-sensory perception (ESP) That is, according to Rhine, "perception without the function of the recognized senses". Among other things, Rhine believed he had found legitimate evidence of what is today referred to as *precognition*, the ability to perceive (and therefore predict) an event that will occur in the future. However, Rhine\'s methodology has been heavily critiqued in the years since he first discussed his findings in his book *Extrasensory Perception* (https://archive.org/embed/extrasensoryperc0000rhin_j6u0).  Despite the critique and general inability to replicate his results, many people to this day still take him at his word that he discovered something phenomenal and, indeed, many people believe that such powers are possible and they themselves may possess them.

This program is designed to put those one of those alleged abilities to the test in a manner similar to that employed by Rhine; though, with a little bit more scientific rigour.

It allows you to complete as many or as few trials as you'd like and will statisically describe the results and evaluate whether you are precognitive according to a $\alpha = 0.05$ decision criteria. The program will also save the results to your computer as 
 a graph and spreadsheet file.

Requires the following Python packages to run
- sys
- datetime
- textwrap
- numpy
- pandas
- matplotlib.pyplot
- scipy.stats
