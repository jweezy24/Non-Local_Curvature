import matplotlib.pyplot as plt

def main():
    points = []
    with open('../outside_points.txt', 'r') as f:
        for line in f:
            try:
                x,y = line.split(',')
            except:
                continue
            point = (float(x),float(y))
            points.append(point)
    for x,y in points:
        plt.scatter(x,y)
    plt.show()

main()
