import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df   = pd.read_csv("medium_data.csv\medium_data.csv")
data = df["responses"].tolist()
popuation_mean = statistics.mean(data)
std_dev        = statistics.stdev(data)

print("Population Mean = "    , popuation_mean)
print("Standard deviation = " , std_dev)

def random_set_of_mean(counter):
    dataset = []

    for i in range(0 , counter):
        random_index = random.randint(0 , len(data)-1)
        value        = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df   = mean_list
    mean = statistics.mean(df)
    fig  = ff.create_distplot([df] , ["Claps"] , show_hist=False)
    fig.add_trace(
        go.Scatter(
            x    =  [mean , mean] ,
            y    = [0,1] , 
            mode = "lines" , 
            name = "Mean"
        )
    )
    fig.show()

def setup() :
    mean_list = []

    for i in range(0 , 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)

    print("Mean of the sampling distribution = " , mean)

setup()

def std_dev():
    mean_list = []

    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    std_dev = statistics.stdev(mean_list)

    print("Standard Deviation of the sampling Distribution : " , std_dev)

std_dev()
