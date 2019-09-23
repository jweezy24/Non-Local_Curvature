import matplotlib.pyplot as plt
import numpy as np

def graph_points():
    data_points = []
    with open('../random_domains.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            data_holder = line.split(':')
            pull_data = False
            title_set = False
            for value in data_holder:
                if 'Domain' in value and 'Size' not in value and 'Error' not in value:
                    pull_data = True
                    continue
                if 'Error' in value:
                    title_set = True
                    continue
                if pull_data:
                    points = value.split(',')
                    points_ints = []
                    x_vals = []
                    y_vals = []
                    pos = 0
                    while pos < len(points)-1:
                        tmp_point = (points[pos],points[pos+1])
                        tmp_x = tmp_point[0].replace('(','').replace(')','').strip()
                        tmp_y = tmp_point[1].replace('(','').replace(')','').strip()
                        try:
                            tmp_point_fin = (float(tmp_x), float(tmp_y))
                            points_ints.append(tmp_point_fin)
                        except:
                            tmp_point_fin = (float(tmp_x.split(' ')[0]), float(tmp_y.split(' ')[0]))
                            points_ints.append(tmp_point_fin)
                        pos+=2
                    data_points.append(points_ints)
                    pull_data = False
                if title_set:
                    title = value.split(' ')[1]
                    plt.title(f'Error is {float(title.strip())*100}')
                    title_set = False
            if count%9 == 4:
                for x,y in points_ints:
                    plt.scatter(x, y)
                plt.savefig(f'./plots/plotted_random_domains/{count}_differntx.png')
            count+=1


def main():
    graph_points()

main()
