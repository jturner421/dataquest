#4
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

#5
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

#7
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
         top20_deathtoll['Total_Deaths'])

#8
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

# Initial Code

# fig, ax = plt.subplots(figsize=(4.5, 6))
# ax.barh(top20_deathtoll['Country_Other'],
#        top20_deathtoll['Total_Deaths'])

# for location in ['left', 'right', 'top', 'bottom']:
#    ax.spines[location].set_visible(False)
# ax.tick_params(bottom=False, left=False)
# *** *** *** *** *** *** *** *** *** ***
#9
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

# Initial Code

# fig, ax = plt.subplots(figsize=(4.5, 6))
# ax.barh(top20_deathtoll['Country_Other'],
#         top20_deathtoll['Total_Deaths'],
#         height=0.45)

# for location in ['left', 'right', 'top', 'bottom']:
#     ax.spines[location].set_visible(False)
# ax.tick_params(bottom=False, left=False)
# ax.set_xticks([0, 150000, 300000])
# *** *** *** *** *** *** *** *** *** ***

#10
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.set_xticks([0, 150000, 300000])
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
# *** *** *** *** *** *** *** *** *** ***

#11
import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.set_xticks([0, 150000, 300000])
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.text(x=-80000, y=23.5,
        s='The Death Toll Worldwide Is 1.5M+',
        weight='bold', size=17)
ax.text(x=-80000, y=22.5,
        s='Top 20 countries by death toll (December 2020)',
        size=12)
# *** *** *** *** *** *** *** *** *** ***
