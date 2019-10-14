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
        '1/1000' : [[],[],[]],
        '1/10000' : [[],[],[]],
        '1/100000' : [[],[],[]],
        '1/1000000' : [[],[],[]],
        '1/10000000' : [[],[],[]],
        '1/100000000' : [[],[],[]],
        '1/1000000000' : [[],[],[]],
        '1/10000000000' : [[],[],[]],
        '1/100000000000' : [[],[],[]],
        '1/1000000000000' : [[],[],[]]
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

def plot_data(data):
    epsilon_handler = [
        '1/1000',
        '1/10000',
        '1/100000', 
        '1/1000000', 
        '1/10000000', 
        '1/100000000', 
        '1/1000000000', 
        '1/10000000000', 
        '1/100000000000', 
    ]
    for i in range(0, len(epsilon_handler)):
        fig, (ax, bx) = plt.subplots(2)
        ep_data = data.get(epsilon_handler[i])
        domain = ep_data[0]
        time = ep_data[1]
        error = ep_data[2]
        ax.set_ylabel('Error(Percent)')
        bx.set_xlabel('Domain Sizes')
        bx.set_ylabel('Time (Minutes)')
        ax.plot(domain, error)
        bx.plot(domain, time)

        fig.suptitle(f'Epsilon is {epsilon_handler[i]}')
        plt.savefig(f'./plots/Random/{i}.png')

    

def main():
    parsed_data = parse_data('../results_random.txt')
    chart_ready_data = create_epsilon_error_charts(parsed_data) 
    plot_data(chart_ready_data)


main()
