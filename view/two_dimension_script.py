from matplotlib import pyplot as plt


def graph_functions(f1, f2, r):
    x = [i for i in r]
    y1_values = [f1(i) for i in r]
    y2_values = [f2(i) for i in r]

    plt.plot(r, y1_values)
    plt.plot(r, y2_values)

    y1_zero = f1(0)
    y2_zero = f2(0)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.ylim(0, max(y1_zero, y2_zero))
    #plt.annotate('f1', xy=(2, f1(2)), xytext=(0+2, y1_zero), arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="angle3,angleA=0,angleB=-90"))
    plt.annotate('f1', xy=(3, f1(3)), xytext=(2, f1(2)), arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=0,angleB=-90"))

    plt.fill_between(x, y1_values, color='green', alpha=0.5, interpolate=True)
    plt.fill_between(x, y2_values, color='red', alpha=0.5, interpolate=True)
    plt.legend(['a','b'])
    plt.yticks(r)
    plt.grid()
    plt.show()

def fill_feasible_region(x, y1, y2):
    plt.fill_between(x, y1, y2, color='green', alpha=0.5)


