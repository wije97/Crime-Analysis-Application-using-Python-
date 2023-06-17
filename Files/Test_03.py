import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import itertools

df_southwales_2020 = pd.read_csv('D:\Ongoing\Melani\CSV\Southwales_2020.csv')
df_southwales_2021 = pd.read_csv('D:\Ongoing\Melani\CSV\Southwales_2021.csv')
month_array = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec", '']
month_array_2 = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
sns.set()
"""multi cmnt"""
df = df_southwales_2020

def show_bar_chart(dtframe, x_label_name, y_label_name, title, btm_margin, right_margin, rotation):
    # print(dtframe_for_crime_type)
    dtframe.plot.bar(stacked=True)
    plt.xlabel(x_label_name)
    plt.ylabel(y_label_name)
    plt.title(title)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.subplots_adjust(bottom=btm_margin, right=right_margin)
    plt.xticks(rotation=rotation)
    plt.show()

def show_pie_chart(sizes, labels):

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    ax.axis('equal')
    plt.show()

def show_line_chart(type, x, y, x_label_name, y_label_name, title,label_name, btm_margin, right_margin, rotation):

    # Create a pie chart
    # plotting
    if type == 1:
        plt.plot(x, y, color="red", label=label_name)

    elif type == 2:
        i = 0

        for tr_row in y:
            if i!=14:
                plt.plot(x, tr_row,label=label_name[0][i])   #,label=label_name[i]
            i = i + 1

    elif type == 3:
        i = 0

        for tr_row in y:
            if i != 2:
                plt.plot(x, tr_row, label=label_name[i])  # ,label=label_name[i]
            i = i + 1


    plt.title(title)
    plt.xlabel(x_label_name)
    plt.ylabel(y_label_name)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.subplots_adjust(bottom=btm_margin, right=right_margin)
    plt.xticks(rotation=rotation)
    plt.grid(True)
    plt.show()


######################################################
def func_get_data_place(type, param2):
    value_counts = df[type].value_counts()
    print(value_counts.keys())
    plt.bar(value_counts.keys(), value_counts.values, color='g', width=0.72, label=value_counts.keys())
    plt.xlabel(type)
    plt.ylabel('Number of Crimes')
    plt.title('Crime Report 2020 - ' + type)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.subplots_adjust(bottom=0.4, right=0.8)
    #plt.show()

    # plt.pie(value_counts.values, labels=value_counts.keys(), autopct='%.2f%%')
    # plt.title('Crime Percentages', loc='left', color='blue', fontweight='bold', fontsize=15)
    # plt.show()
#func_get_data_place('LSOA name',1)



######################################################
def filter_data_by_crime_type_and_month(df_data, type):
    sp_rows_array = []
    index_arr_rtn = []
    plot_arr_rtn = []
    i = 0

    grouped_month = df_data.groupby('Month')

    for month, group in grouped_month:
        specific_rows_by_month = df_data.loc[df_data['Month'] == month]
        specific_rows_by_crime = specific_rows_by_month.loc[specific_rows_by_month['Crime type'] == type]
        sp_rows_array.append(specific_rows_by_crime)

    for row in sp_rows_array:
        # Get the rows you want using the DataFrame's "loc" method
        value_counts_by_crime = row['Crime type'].value_counts()
        plot_arr_rtn.append(value_counts_by_crime.values)
        if (i == 0):
            index_arr_rtn.append(value_counts_by_crime.keys())
        i = i + 1
    return plot_arr_rtn, index_arr_rtn

def func_get_data_by_crime_type(type, chart):

    return_array = filter_data_by_crime_type_and_month(df, type)
    plot_array, index_array = return_array

    #print(plot_array)

    dtframe_for_crime_type = pd.DataFrame(data=plot_array, index=month_array, columns=index_array)
    print(dtframe_for_crime_type)

    # Data to plot as sequence
    plt_sequence = itertools.chain(*plot_array)
    plt_sequence = list(plt_sequence)

    if chart == "bar":
        show_bar_chart(dtframe_for_crime_type, 'Months', 'Number of Crimes', 'Crime Report 2020 - ' + type, 0.2, 0.8, 0)
    elif chart == "pie":
        labels = month_array_2
        sizes = plt_sequence
        show_pie_chart(sizes, labels)
    elif chart == "line":
        # data to be plotted
        x = month_array_2
        y = plt_sequence
        show_line_chart(1, x, y, 'Months', 'Number of Crimes', 'Crime Report 2020 - ' + type, type, 0.2, 0.8, 0)
#func_get_data_by_crime_type('Violence and sexual offences', 'line')



######################################################
def filter_all_crime_data_by_month(df_data):
    sp_rows_array = []
    index_arr_rtn = []
    plot_arr_rtn = []
    i = 0

    grouped_month = df_data.groupby('Month')

    for month, group in grouped_month:
        # Get the rows you want using the DataFrame's "loc" method
        specific_rows_by_month = df_data.loc[df_data['Month'] == month]
        sp_rows_array.append(specific_rows_by_month)

    for row in sp_rows_array:
        value_counts_by_crime = row['Crime type'].value_counts()
        plot_arr_rtn.append(value_counts_by_crime.values)
        if (i == 0):
            index_arr_rtn.append(value_counts_by_crime.keys())
        i = i + 1

    return plot_arr_rtn, index_arr_rtn

def func_get_data_by_all_crimes_vs_month(type, chart):

    return_array = filter_all_crime_data_by_month(df)
    plot_array, index_array = return_array

    dtframe_for_month = pd.DataFrame(data=plot_array, index=month_array, columns=index_array)
    #print(dtframe_for_month)
    plt.show()

    if chart == "bar":
        show_bar_chart(dtframe_for_month, 'Months', 'Number of Crimes', 'Crime Report 2020 - Monthly Crime Frequency', 0.2, 0.8, 45)
    elif chart == "line":

        plot_list = []

        for row in plot_array:
            sequence = list(row)
            plot_list.append(sequence)

        del plot_list[-1]
        transposed_arr = list(map(list, zip(*plot_list)))
        # print(transposed_arr)
        # data to be plotted

        x = month_array_2
        y = transposed_arr
        show_line_chart(2, x, y, 'Months', 'Number of Crimes', 'Crime Report 2020 - Monthly Crime Frequency', index_array ,0.2, 0.8, 45)
#func_get_data_by_all_crimes_vs_month(1, 'line')



######################################################
def filter_data_by_crime_type(df_data):

    plt_arr = []
    ind_arr = []

    value_counts_by_crime = df_data['Crime type'].value_counts()
    plt_arr.append(value_counts_by_crime.values)
    ind_arr.append(value_counts_by_crime.keys())

    return plt_arr, ind_arr

def func_get_data_by_year(param1, chart):

    df_1 = df_southwales_2020
    df_2 = df_southwales_2021

    return_array = filter_data_by_crime_type(df_1)
    plot_array_1 = return_array[0]
    idx_rtn_array = return_array[1]

    return_array = filter_data_by_crime_type(df_2)
    plot_array_2 = return_array[0]

    dtframe_from_2020 = pd.DataFrame(data=plot_array_1, index=["2020"], columns=idx_rtn_array)
    dtframe_from_2021 = pd.DataFrame(data=plot_array_2, index=["2021"], columns=idx_rtn_array)
    dtframe_for_month = pd.concat([dtframe_from_2020,dtframe_from_2021], axis=0)
    my_df = pd.DataFrame(dtframe_for_month.transpose())
    #print(dtframe_for_month)

    if chart == "bar":
        show_bar_chart(my_df, 'Crime Type', 'Number of Crimes', 'Crime Report 2020 vs 2021', 0.4, 0.8, 90)
    elif chart == "line":
        # data to be plotted
        plot_array = []

        plot_array.append(plot_array_1)
        plot_array.append(plot_array_2)

        sequence = None
        plot_list = []

        for x_row in idx_rtn_array:
            sequence = list(x_row)
            del sequence[-1]

        for y_row in plot_array:
            y_sequence = itertools.chain(*y_row)
            y_sequence = list(y_sequence)
            del y_sequence[-1]
            plot_list.append(y_sequence)

        x = sequence
        y = plot_list
        show_line_chart(3, x, y, 'Crime Type', 'Number of Crimes', 'Crime Report 2020 vs 2021', ['2020','2021'],0.4, 0.8, 90)
func_get_data_by_year(1, 'bar')



######################################################
def func_get_data_by_year_with_crime_type(type, chart):

    df_1 = df_southwales_2020
    df_2 = df_southwales_2021

    return_array = filter_data_by_crime_type_and_month(df_1, type)
    plot_array_1 = return_array[0]
    idx_rtn_array = return_array[1]

    return_array = filter_data_by_crime_type_and_month(df_2, type)
    plot_array_2 = return_array[0]

    #print(plot_array_1)
    #print(plot_array_2)
    #print(idx_rtn_array)
    dtframe_from_2020 = pd.DataFrame(data=plot_array_1, index=month_array, columns=["2020"])
    dtframe_from_2021 = pd.DataFrame(data=plot_array_2, index=month_array, columns=["2021"])
    dtframe_for_crime_type = pd.concat([dtframe_from_2020, dtframe_from_2021], axis=1)

    #print(dtframe_for_crime_type)

    if chart == "bar":
        show_bar_chart(dtframe_for_crime_type, 'Months', 'Number of Crimes', 'Crime Report 2020 vs 2021- ' + type, 0.2, 0.8, 0)
    elif chart == "line":
        # data to be plotted
        plot_array = []
        plot_list = []

        plot_array.append(plot_array_1)
        plot_array.append(plot_array_2)

        for y_row in plot_array:
            y_sequence = itertools.chain(*y_row)
            y_sequence = list(y_sequence)
            plot_list.append(y_sequence)

        x = month_array_2
        y = plot_list
        show_line_chart(3, x, y, 'Months', 'Number of Crimes', 'Crime Report 2020 vs 2021- ' + type, ['2020','2021'], 0.2, 0.8, 0)
func_get_data_by_year_with_crime_type('Robbery', 'bar')
