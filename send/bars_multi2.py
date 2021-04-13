import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df = pd.read_csv('DSA_data.csv')
df = df[[ 'age', 'marital', 'poutcome', 'housing', 'loan', 'default', 'contact', 'month', 'day_of_week', 'campaign', 'education', 'job', 'y' ]]
df_yes = df[df['y'] == 'yes']


fig=plt.figure()
gs1 = gridspec.GridSpec(4, 3)           #set the number of subplots
gs1.update(wspace=0.1, hspace=0.2)          # set the spacing between axes.


for col in [i for i in df.columns if i !='y']:

    count = df[col].value_counts().sort_index()
    count_yes = df_yes[col].value_counts().sort_index()

    ax = plt.subplot(gs1[df.columns.get_loc(col)])

    count.plot.bar(fontsize=5)
    count_yes.plot.bar(fontsize=5, color='r')
    rotate=0
    if col=='job' or col=='education':
        rotate=40

    if col=='day_of_week':
        plt.ylim(ymax = 10000)

    if col=='education':
        plt.ylim(ymax = 15000)

    if col=='housing':
        plt.ylim(ymax = 27500)

    font=8
    if col=='age':
        font=6
        plt.legend(bbox_to_anchor=(0.47,0.42), labels=['Clients Called', 'Clients Subscribed'])

    plt.xticks(fontsize=font, rotation=rotate)

    plt.title(str(col).capitalize(), x=.8, y=.8)

    if col=='age':
        plt.setp(ax.get_xticklabels()[::2], visible=False)


fig.suptitle('Client Statistics', y=.95, fontsize=30)
plt.tight_layout()

plt.show(block=True)
