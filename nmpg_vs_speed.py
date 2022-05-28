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
    
plt.figure(figsize=(12, 6))
for index, nmpg_per_gph in enumerate(all_nmpg_per_gph):
    plt.plot(v_nmphs, nmpg_per_gph, label = '%s GPH'%gphs[index])


plt.axvline(250, color='k', linestyle='--')

plt.title('NMPG vs. Speed for Various Aircraft')
plt.xlabel('Speed [kts]')
plt.xticks(range(0,300,10))
plt.ylabel('NMPG [NM/gal]')
plt.yticks(range(0,90,5))
plt.legend(loc='upper left', bbox_to_anchor=(1,1),
           ncol=1, fancybox=True, shadow=True)
plt.grid()
plt