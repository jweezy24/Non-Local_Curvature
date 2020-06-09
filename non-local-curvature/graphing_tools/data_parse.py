import matplotlib.pyplot as plt

def parse_data(file_path):
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            lines.append(line)
    
    line_data = []
    for line in lines:
        line_tmp = line.split('\t')
        line_data_tmp = []
        for words in line_tmp:
            seperated_data = words.split(':')
            line_data_tmp.append((seperated_data[0], seperated_data[1]))
        line_data.append(line_data_tmp)
    return line_data

def create_epsilon_error_charts(data):
    epsilon_handler = {
        '1/100.0' : [[],[],[]],
        '1/1000.0' : [[],[],[]],
        '1/10000.0' : [[],[],[]]
        # '1/100000.0' : [[],[],[]],
        # '1/1000000.0' : [[],[],[]],
        # '1/10000000.0' : [[],[],[]],
        # '1/100000000.0' : [[],[],[]],
        # '1/1000000000.0' : [[],[],[]],
        # '1/10000000000.0' : [[],[],[]],
        # '1/100000000000.0' : [[],[],[]],
        # '1/1000000000000.0' : [[],[],[]]
    }
    for line in data:
        
        domain_tmp = ''
        time_tmp = ''
        error_tmp = '' 
        for val in line:
            if 'Error' in val[0]:
                error_tmp = float(val[1])*100
            if 'Domain' in val[0]:
                domain_tmp = float(val[1])
            if 'Time' in val[0]:
                time_tmp = float(val[1].strip())
            
        for val in line:
            if 'Epsilon' in val[0]:
                epsilon_handler.get(val[1])[0].append(domain_tmp)
                epsilon_handler.get(val[1])[1].append(time_tmp)
                epsilon_handler.get(val[1])[2].append(error_tmp)
    return epsilon_handler

def plot_data(data, path, isclosed=True):
    epsilon_handler = [
        '1/100.0',
        '1/1000.0',
        '1/10000.0' 
        # '1/1000000', 
        # '1/10000000', 
        # '1/100000000', 
        # '1/1000000000', 
        # '1/10000000000', 
        # '1/100000000000', 
    ]
    for i in range(0, len(epsilon_handler)):
        fig, (ax, bx) = plt.subplots(2)
        ep_data = data.get(epsilon_handler[i])
        domain = ep_data[0]
        time = ep_data[1]
        error = ep_data[2]
        if isclosed:
            ax.set_ylabel('Error(Percent)')
            bx.set_xlabel('Domain Sizes')
            bx.set_ylabel('Time (Minutes)')
        else:
            ax.set_ylabel('Curvature')
            bx.set_xlabel('Domain Sizes')
            bx.set_ylabel('Time (Minutes)')

        ax.plot(domain, error)
        bx.plot(domain, time)

        if i == 2:
            ax.set_ylim([0,200])
            ax.set_xlim([400,10000])
            if i== 1:
                continue

        fig.suptitle(f'Epsilon is {epsilon_handler[i]}')
        if 'winding_number' in path:
            plt.savefig(f'./plots/Winding_number/{i}.png')
        if 'bounding_box' in path:
            plt.savefig(f'./plots/Bounding_Box/{i}.png')
        if 'crossing_number' in path:
            #plt.show()
            plt.savefig(f'./plots/Crossing_number/{i}.png')


def parse_ellipse(data):

    x_axis = []
    y_axis = []
    plt.clf()
    for item in data:
        for stuff in item:
            if 'Integration' in stuff[0]:
                y_axis.append(float(stuff[1]))
            elif 'iter' in stuff[0]:
                if '0/100' == stuff[1]:
                    x_axis.append(float(0))
                else:
                    x_axis.append(float(eval(stuff[1])))
    
    plt.plot(x_axis,y_axis)
    plt.ylabel('Integral Evaluation')
    plt.xlabel('Iter')
    plt.savefig(f'./plots/Ellipse/Week1.png')


def create_open_set_chart(data):
    epsilon_handler = {
        '1/100.0' : [[],[],[]],
        '1/1000.0' : [[],[],[]],
        '1/10000.0' : [[],[],[]]
        # '1/100000.0' : [[],[],[]],
        # '1/1000000.0' : [[],[],[]],
        # '1/10000000.0' : [[],[],[]],
        # '1/100000000.0' : [[],[],[]],
        # '1/1000000000.0' : [[],[],[]],
        # '1/10000000000.0' : [[],[],[]],
        # '1/100000000000.0' : [[],[],[]],
        # '1/1000000000000.0' : [[],[],[]]
    }
    for line in data:
        
        domain_tmp = ''
        time_tmp = ''
        error_tmp = '' 
        for val in line:
            if 'Evaluation' in val[0]:
                error_tmp = float(val[1])
            if 'Domain' in val[0]:
                domain_tmp = float(val[1])
            if 'Time' in val[0]:
                time_tmp = float(val[1].strip())
            
        for val in line:
            if 'Epsilon' in val[0]:
                epsilon_handler.get(val[1])[0].append(domain_tmp)
                epsilon_handler.get(val[1])[1].append(time_tmp)
                epsilon_handler.get(val[1])[2].append(error_tmp)
    return epsilon_handler

    

def main():
    path_winding = '../results_winding_number.txt'
    path_bounding = '../results_bounding_box.txt'
    path_ellipse = '../results_bounding_box_ellipse.txt'
    path_crossing = '../results_crossing_number.txt'

    # parsed_data = parse_data(path_winding)
    # chart_ready_data = create_epsilon_error_charts(parsed_data) 
    # plot_data(chart_ready_data, path_winding)

    # print("HERE")

    # parsed_data = parse_data(path_bounding)
    # chart_ready_data = create_open_set_chart(parsed_data) 
    # plot_data(chart_ready_data, path_bounding, isclosed=False)

    # print("HERE")

    # parsed_data = parse_data(path_ellipse)
    # parse_ellipse(parsed_data)

    parsed_data = parse_data(path_crossing)
    chart_ready_data = create_epsilon_error_charts(parsed_data) 
    plot_data(chart_ready_data, path_crossing)


main()
