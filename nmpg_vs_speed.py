import pandas as pd
import matplotlib.pyplot as plt

gphs = range(3, 16)
gphs

v_nmphs = range(0, 251)
v_nmphs

all_nmpg_per_gph = []
for gph in gphs:
    nmpg_per_gph = []
    for v_nmph in v_nmphs:
        nmpg = v_nmph / gph
        nmpg_per_gph.append(nmpg)
    all_nmpg_per_gph.append(nmpg_per_gph)

agg_ac_perf_df = pd.read_csv('nmpg_speed_table.csv').set_index('Speed [kts]')

plt.figure(figsize=(16, 8))
for index, nmpg_per_gph in enumerate(all_nmpg_per_gph):
    plt.plot(v_nmphs, nmpg_per_gph, label = '%s GPH'%gphs[index])

agg_ac_perf_df.groupby('Model')['NMPG'].plot(style='o', markersize=4, legend=True)

plt.axvline(250, color='k', linestyle='--')

plt.title('NMPG vs. Speed for Various Aircraft')
plt.xlabel('Speed [kts]')
plt.xticks(range(0,300,10))
plt.ylabel('NMPG [NM/gal]')
plt.yticks(range(0,90,5))
plt.legend(loc='upper left', bbox_to_anchor=(1,1),
           ncol=1, fancybox=True, shadow=True)
plt.grid()
plt.tight_layout()
plt