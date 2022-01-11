#4
def slope(x1,x2,y1,y2):
    ## Finish the function here
    return 0

#6
import seaborn

seaborn.set(style='darkgrid')


def draw_secant(x_values):
    x = np.linspace(-20, 30, 100)
    y = -1 * (x ** 2) + x * 3 - 1
    plt.plot(x, y)
    # Add your code here.
    plt.show()
