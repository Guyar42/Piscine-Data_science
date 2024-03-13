import pandas as pd
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print("loading dataset of dimensions", df.shape)
        # tab = df["France", "2020"]
        # print("shape of table", tab.shape)
        # print("Bonjour")
        tab = df.loc[df['country'] == 'France']
        y_values = tab.iloc[:, 1:].values.flatten().tolist()  # Ignorer la colonne 'country' et convertir en liste
        x_values = tab.iloc[:, 1:].columns.astype(int).values  # Utiliser les noms des colonnes comme valeurs de 'y'  

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')

        fig.suptitle("France life expectancy Projections")
        plt.show()
        print(y_values)
        # print("Liste de toutes les valeurs de 'x' pour la France :", x_values)
        # print("Liste de toutes les valeurs de 'x' pour la France :", y_values)
        
        return df
    except Exception as e:
        print(e)
        return None
