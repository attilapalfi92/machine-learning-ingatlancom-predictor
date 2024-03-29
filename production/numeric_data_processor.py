from production.polynomizer import Polynomizer
from sklearn.preprocessing import Imputer
import numpy as np
import pandas as pd


class NumericDataProcessor:
    def _impute_(self, dataset, X, column_name):
        idx = dataset.columns.get_loc(column_name)
        imputer = Imputer(missing_values="NaN", strategy='mean', axis=0)
        imputer.fit(X[:, idx:idx + 1])
        X[:, idx:idx + 1] = imputer.transform(X[:, idx:idx + 1])
        return X, imputer, idx

    def __init__(self, dataset, poly_degree=4):
        dataset = self.prepareDataset(dataset)
        dataset['price'] = dataset['price'] \
            .apply(lambda p: p.replace(' millió Ft', '').replace(',', '.')) \
            .astype(float)

        self.y = dataset['price'].values
        dataset = dataset.drop('id', 1).drop('price', 1)

        X = dataset.values

        # keys are column indexes
        self.imputers = {}
        X, imputer, i = self._impute_(dataset, X, 'floor')
        self.imputers[i] = imputer
        X, imputer, i = self._impute_(dataset, X, 'building_levels')
        self.imputers[i] = imputer
        dataset = pd.DataFrame(X, columns=dataset.columns)

        # adding polynomial features
        self.polynomizer = Polynomizer(dataset)
        self.dataset = self.polynomizer.transform(dataset)

    def process(self, dataset):
        dataset = self.prepareDataset(dataset)
        X = dataset.values
        for index, imputer in self.imputers.items():
            X[:, index:index + 1] = imputer.transform(X[:, index:index + 1])

        dataset = pd.DataFrame(X, columns=dataset.columns)
        return self.polynomizer.transform(dataset)

    def prepareDataset(self, dataset):
        dataset['floor'] = dataset['floor'] \
            .apply(lambda f: f.replace('nincs megadva', 'NaN')).astype(float)
        dataset['building_levels'] = dataset['building_levels'] \
            .apply(lambda f: f.replace('nincs megadva', 'NaN')).astype(float)
        room_data = dataset['rooms'].str.split(' \+ ', 1, expand=True)
        dataset['rooms'] = room_data[0].astype(str) \
            .apply(lambda hr: hr.replace(' fél', '')).astype(float)
        dataset['half_rooms'] = room_data[1].astype(str) \
            .apply(lambda hr: hr.replace(' fél', '')) \
            .apply(lambda hr: hr.replace('None', '0')).astype(float)
        dataset['size'] = dataset['size'].astype(str) \
            .apply(lambda s: s.replace(' m²', '')).apply(lambda s: s.replace(' ', '')) \
            .astype(float)

        # some clearing
        dataset = dataset[dataset['size'] > 20]
        dataset = dataset[dataset['size'] < 250]
        dataset = dataset[dataset['rooms'] < 10]
        dataset = dataset[dataset['half_rooms'] < 10]
        dataset = dataset[np.isfinite(dataset['longitude'])]
        dataset = dataset[np.isfinite(dataset['latitude'])]

        dataset = dataset.drop('ac', 1) if 'ac' in dataset.columns else dataset
        dataset = dataset.drop('attic', 1) if 'attic' in dataset.columns else dataset
        dataset = dataset.drop('barrier_free', 1) if 'barrier_free' in dataset.columns else dataset
        dataset = dataset.drop('build_year', 1) if 'build_year' in dataset.columns else dataset
        dataset = dataset.drop('energy_cert', 1) if 'energy_cert' in dataset.columns else dataset
        dataset = dataset.drop('garden_connected', 1) if 'garden_connected' in dataset.columns else dataset

        return dataset

    def getY(self):
        return self.y

    def getDataset(self):
        return self.dataset