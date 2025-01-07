import pandas as pd
import matplotlib.pyplot as plt
from pyscript import display
from pyscript import document
import warnings

warnings.filterwarnings("ignore")

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

document.getElementById("result_area").innerHTML = " <br>READY FOR USE!<br>" 


# Define the function that gets called when the button is clicked
def run_func(e):
    
    # Clear the previous output in the result div
    document.getElementById("result_area").innerHTML = ""  # Clear the result div
    
    # Get the input value from the HTML element using PyScript's access
    user_input_MARK = document.getElementById("userInputMARK").value.casefold()
    user_input_COMMON_NAME = document.getElementById("userInputCOMMON_NAME").value.casefold()
    user_input_MODEL_NAME = document.getElementById("userInputMODEL_NAME").value.casefold()
    user_input_BASE_PROVINCE_OR_STATE_E = document.getElementById("userInputBASE_PROVINCE_OR_STATE_E").value.casefold()
    user_input_FULL_NAME = document.getElementById("userInputFULL_NAME").value.casefold()
    user_input_OWNER_NAME_OLD_FORMAT = document.getElementById("userInputOWNER_NAME_OLD_FORMAT").value.casefold()
    
    query_string = []
    if user_input_MARK:
        query_string.append(f'(df_ccars_merged[\'MARK\'].str.casefold().str.str.contains(\'{user_input_MARK}\'))')
    if user_input_COMMON_NAME:
        query_string.append(f'(df_ccars_merged[\'COMMON_NAME\'].str.casefold().str.contains(\'{user_input_COMMON_NAME}\'))')
    if user_input_MODEL_NAME:
        query_string.append(f'(df_ccars_merged[\'MODEL_NAME\'].str.casefold().str.contains(\'{user_input_MODEL_NAME}\'))')
    if user_input_BASE_PROVINCE_OR_STATE_E:
        query_string.append(f'(df_ccars_merged[\'BASE_PROVINCE_OR_STATE_E\'].str.casefold().str.contains(\'{user_input_BASE_PROVINCE_OR_STATE_E}\'))')
    if user_input_FULL_NAME:
        query_string.append(f'(df_ccars_merged[\'FULL_NAME\'].str.casefold().str.contains(\'{user_input_FULL_NAME}\'))')
    if user_input_OWNER_NAME_OLD_FORMAT:
        query_string.append(f'(df_ccars_merged[\'OWNER_NAME_OLD_FORMAT\'].str.casefold().str.contains(\'{user_input_OWNER_NAME_OLD_FORMAT}\'))')
    
    # If the input is empty, do nothing
    if query_string == []:
        display("Please enter a valid value.", target="result_area")
        return
    
    # Display the value entered in the input box
    display(f"You entered: {user_input_MODEL_NAME}", target="result_area")

    # Example of using the input value to filter or plot
    filter_clause = ' & '.join(query_string)    
    
    filtered_data = df_ccars_merged[eval(filter_clause)]
    display(filtered_data, target="result_area")

    # Group by a column and show the count
    group_data = filtered_data.groupby('BASE_PROVINCE_OR_STATE_E').count()[['MARK']]
    display(group_data, target="result_area")

    # Plot the data
    ax = filtered_data.groupby('BASE_PROVINCE_OR_STATE_E').count()['MARK'].plot.bar()
    plt.title(f"Count per Province for Model {user_input_MODEL_NAME}")
    plt.xlabel('Province')
    plt.ylabel('Count')
    plt.grid()
    plt.tight_layout()

    # Display the plot
    display(plt, target="result_area")

# Attach the event handler to the button click
document.getElementById("runButton").onclick = run_func