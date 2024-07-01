import pandas as pd
from pairs_selector import PairsSelector

import warnings
warnings.filterwarnings('ignore')

P_i = pd.read_csv('./data/data.csv').set_index('Date').dropna()
P_i.index = pd.to_datetime(P_i.index)

P_i = P_i.last('10Y')

ps = PairsSelector(P_i)
ps.dimensionality_reduction(5)
#ps.plot_pca_matrix()

ps.cluster()
#ps.plot_clustering_info()
print("ps.plot_clustering_info()")

if __name__ == '__main__':
    ps.criterion_selector()
    #ps.plot_selected_pairs()
    print("ps.criterion_selector()")

    ps.print_info()
    print("ps.print_info()")

    print(ps.final_pairs)