#2

import pandas as pd
housing = pd.read_csv('housing.csv')

#3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice')
# plt.show()

#4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
#             hue='Overall Qual', palette='RdYlGn')
# plt.show()
#5
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
#             hue='Overall Qual', palette='RdYlGn',
#             size='Garage Area', sizes=(1,300))
# plt.show()

#6
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
#             hue='Overall Qual', palette='RdYlGn',
#             size='Garage Area', sizes=(1,300),
#             style='Rooms')
# plt.show()

