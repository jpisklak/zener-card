import sys
import datetime as dt
import textwrap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp

#Background and Instructions
bkgd_title = 'Background'.upper()
inst_title = 'Instructions'.upper()

bkgd_info_1 = 'This program runs a basic computerized replication of the (in)famous Zener Card studies conducted by Dr. J.B. Rhine (he had a PhD in botany, not psychology).'

bkgd_info_2 = 'Rhine\'s original studies were designed to evaluate specific types of extra-sensory perception (ESP). That is, according to Rhine, "perception without the function of the recognized senses". Among other things, Rhine believed he had found legitimate evidence of what is today referred to as \'precognition\', the ability to perceive (and therefore predict) an event that will occur in the future. However, Rhine\'s methodology has been heavily critiqued in the years since he first discussed his findings in his book "Extrasensory Perception" (https://archive.org/embed/extrasensoryperc0000rhin_j6u0).  Despite the critique and general inability to replicate his results, many people to this day still take him at his word that he discovered something phenomenal and, indeed, many people believe that such powers are possible and they themselves may possess them.'

bkgd_info_3 = 'This program is designed to put those one of those alleged abilities to the test in a manner similar to that employed by Rhine; though, with a little bit more scientific rigour.'

bkgd_words = [bkgd_info_1, bkgd_info_2, bkgd_info_3]

inst_info_1 = '- The computer will select a number 1, 2, 3, 4, or 5 at random.  You need to predict what number the computer will choose before it has selected it.'

inst_info_2 = '- Each attempt will place the chosen number back into the list, meaning it could be chosen more than once in a row.'

inst_info_3 = '- It is reccommended that you complete at least 50 trials for a decent sample size.'

inst_info_4 = '- Typing "end" will exit the test and display the results.'

inst_info_5 = '- A spreadsheet file of the data and graph will be saved when you exit.'

inst_words = [inst_info_1, inst_info_2, inst_info_3, inst_info_4, inst_info_5]

#Instructions and background print
print(bkgd_title.center(80, '='))
print('')
for i in bkgd_words:
    print(textwrap.fill(text = i, width = 80), '\n')

print(inst_title.center(80, '='))
print('')
for i in inst_words:
    print(textwrap.fill(text = i, width = 80), '\n')

#Zener cards as numbers
cards = np.arange(1, 6, 1)

#Data storage
data = np.zeros((0, 4)) #Trial, human response, human latency, computer choice

# Start test
begin_prog = False

while begin_prog == False:
    confirm_start = input('Type "start" to begin or "end" to quit. ')
    
    if confirm_start.lower() == 'end':
        sys.exit()

    elif confirm_start.lower() == 'start':
        start_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        begin_prog = True

test_complete = False
trial = 0

while test_complete == False:
    trial = trial + 1
    trial_str = ' Trial: ' + str(trial) + " "
    print()
    print(trial_str.center(80, '-'))
    tr_start_time = dt.datetime.now()
    sub_resp = input('What number will the computer select? ').lower().replace(' ', '')
   
    if sub_resp.isdigit() == True and int(sub_resp) > 0 and int(sub_resp) < 6 :
        tr_end_time = dt.datetime.now()
        comp_sel = np.random.choice(a = cards)
        sub_lat = tr_end_time - tr_start_time   
        data = np.append(data, [[trial, int(sub_resp),sub_lat.total_seconds(), comp_sel]], axis = 0)
        print('Response Logged')
    
    elif sub_resp == 'end':
        if trial == 1:
            sys.exit()
        trial = trial - 1
        #print(data)
        test_complete = True
   
    else:
        trial = trial - 1
        print('Please input a number between 1 and 5, or type "end" to quit and see your results.')
        
#Results---------------------------------
#Summary Stats              
attempts = np.max(data[0:, 0])
sub_hits = np.sum(data[0:, 1] == data[0:, 3]) 
hit_range = np.arange(0, attempts + 1, 1)
prob_hit = 1/5

#The probability of x hits in y trials trials (Binomial Model)
sub_hit_prob = sp.binom.pmf(k = sub_hits, n = attempts, p = prob_hit)

#Hit probability across a range of values
hit_prob = sp.binom.pmf(k = hit_range, n = attempts, p = prob_hit)

#What is the expected number of hits in x plays?
exp_hits = attempts * prob_hit

#Standard deviation of model
sd_hits = np.sqrt(attempts * prob_hit * (1 - prob_hit))

#95% Boundry
upper_bound = sp.binom.ppf(1 - 0.05, n = attempts, p = prob_hit)

#Cumulative Probability
cdf_score = sp.binom.cdf(k = sub_hits, n = attempts, p = prob_hit)  

# Evaluation
print('\n\n')
print(str("Evaluation:").center(80, '='))
print('\nYou made', int(attempts), 'attemps.\n')
print("You have made the correct prediction ", sub_hits, " times.\n")

print('There is approximately a', 
      str(round((1 - cdf_score) * 100, 2)),
      '% chance of making at least that many correct predictions.'
      )

print(
    'On average you would expect to get', round(exp_hits, 2), 'correct in', int(attempts), 'attempts.\n'
    )

print(
    'A person with true precognitive abilities would reasonably be expected to get\n',
    'at least', int(upper_bound), 'attempts correct.\n'
    )

print(
    'The orange bar on the graph indicates your score. The vertical dashed line\n',
    'indicates the upper 95% boundry beyond which a true precognitive person would\n',
    'be expected to score.\n'
    )

print('The essence of science is repeatability. See if you can replicate your findings.\n')

#Save Data
save_time = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
df = pd.DataFrame(data, columns = ['trial','human_resp', 'latency_s', 'comp_selection'])
df['correct_pred'] = (data[0:,1] == data[0:,3])
df['start_date'] = start_date
df.to_csv("pre_cognition_results-" + 
          save_time + 
          '.csv', 
          index = False)

#Plot Parameters
ax_font_size = 16

if trial < 10:
    xticks = np.arange(0, np.max(hit_range) + 1, 1)
elif trial < 30:
    xticks = np.arange(0, np.max(hit_range) + 1, 2)
elif trial < 50:
    xticks = np.arange(0, np.max(hit_range) + 1, 5)
else:
    xticks = np.arange(0, np.max(hit_range) + 1, 10)

colours = []

for i in range(len(hit_range)):
    if i == sub_hits:
        colours.append("#D55E00")
    elif i >= upper_bound:
        colours.append("#0072B2")
    else:
        #colors.append("#A6CEE3")
        colours.append("#0072B2")

#Plot
plt.bar(hit_range, hit_prob, color = colours, ec = "black", linewidth = 1)
plt.axvline(x = round(upper_bound) - .5, color = "black", linestyle = "--", linewidth = 2)
plt.xticks(xticks, fontsize = ax_font_size)
plt.yticks(fontsize = ax_font_size)
plt.xlabel("Number of Correct Predictions", fontsize = ax_font_size)
plt.ylabel("Probability", fontsize = ax_font_size)

plt.savefig("pre_cognition_results-" +
            save_time +
            '.png',
            dpi = 300, transparent = False, bbox_inches = 'tight')
plt.show()

exit
