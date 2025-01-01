import pandas as pd
import matplotlib.pyplot as plt
from pyscript import display

df_ccarscurr = pd.read_csv("carscurr.txt",
                            encoding = "ISO-8859-1",
                            header = None,
                            skipfooter=1
                            )#.dropna(thresh=40)#.dropna(subset=[24]) and 10 for ownr
df_ccarscurr

df_ccarsownr = pd.read_csv("carsownr.txt",
                            encoding = "ISO-8859-1",
                            header = None)
df_ccarsownr = df_ccarsownr.drop(df_ccarsownr.tail(1).index) # since skipfooter in read_csv was having issues
df_ccarsownr

layout_df = pd.read_fwf("carslayout.txt",
                        encoding = "ISO-8859-1",
                        header=None)
layout_df = layout_df.drop(layout_df.tail(2).index) # since skipfooter not avail in read_fwf
layout_df.dropna(axis=1, how='all', inplace=True)
layout_df

first_fle_index_start = layout_df[layout_df[4]=='FILE'].index[0]
second_fle_index_start = layout_df[layout_df[4]=='FILE'].index[1]

layout_first_file = layout_df[first_fle_index_start + 1 : second_fle_index_start]
layout_first_file
layout_first_file

layout_second_file = layout_df[second_fle_index_start + 1::]
layout_second_file

list_carscurr_headers = list(layout_first_file[3])
list_carsownr_headers = list(layout_second_file[3])

df_ccarscurr = df_ccarscurr.set_axis(list_carscurr_headers, axis=1)
df_ccarscurr

df_ccarsownr = df_ccarsownr.set_axis(list_carsownr_headers, axis=1)
df_ccarsownr

df_ccars_merged = pd.merge(df_ccarscurr,
                           df_ccarsownr,
                           left_on='MARK',
                           right_on='MARK_LINK',
                           suffixes=('', '_ownr'))


display(df_ccars_merged[df_ccars_merged['MODEL_NAME'] == "175"])

display(df_ccars_merged[df_ccars_merged['MODEL_NAME'] == "175"].groupby('BASE_PROVINCE_OR_STATE_E').count()[['MARK']])



ax=df_ccars_merged[df_ccars_merged['MODEL_NAME'] == "175"].groupby('BASE_PROVINCE_OR_STATE_E').count()['MARK'].plot.bar()
plt.title('Count per Province')
plt.xlabel('Province')
plt.ylabel('Count')
plt.grid()
plt.tight_layout()
display(plt)
#display(df_ccars_merged[df_ccars_merged['MODEL_NAME'] == "175"].groupby('BASE_PROVINCE_OR_STATE_E').count()['MARK'].plot.bar())