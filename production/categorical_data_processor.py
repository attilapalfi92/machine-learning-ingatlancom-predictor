from sklearn.preprocessing import LabelEncoder, OneHotEncoder


class CategoricalDataProcessor:
    def _prepareDataset_(self, dataset):
        dataset = dataset.drop('ac', 1) if 'ac' in dataset.columns else dataset
        dataset = dataset.drop('attic', 1) if 'attic' in dataset.columns else dataset
        dataset = dataset.drop('barrier_free', 1) if 'barrier_free' in dataset.columns else dataset
        dataset = dataset.drop('build_year', 1) if 'build_year' in dataset.columns else dataset
        dataset = dataset.drop('energy_cert', 1) if 'energy_cert' in dataset.columns else dataset
        dataset = dataset.drop('garden_connected', 1) if 'garden_connected' in dataset.columns else dataset

        dataset['building_material'] = dataset['building_material'].astype('category')
        dataset['comfort'] = dataset['comfort'].astype('category')
        dataset['cond'] = dataset['cond'].astype('category')
        dataset['heating'] = dataset['heating'].astype('category')
        dataset['parking'] = dataset['parking'].astype('category')
        dataset['sub_type'] = dataset['sub_type'].astype('category')
        dataset['toilet'] = dataset['toilet'].astype('category')
        return dataset

    def __init__(self, dataset):
        dataset = self._prepareDataset_(dataset)
        X = dataset.values
        # encoding categorical data
        self.categoricalIndexes = []
        self.labelEncoders = {}
        for column in dataset.columns:
            if dataset[column].dtype.name == 'category':
                idx = dataset.columns.get_loc(column)
                print(idx)
                self.categoricalIndexes.append(idx)
                label_encoder = LabelEncoder()
                X[:, idx] = label_encoder.fit_transform(X[:, idx])
                self.labelEncoders[idx] = label_encoder

        # libs take care of dummy variable trap so I don't have to
        # (otherwise should drop first column for each category)
        self.oneHotEncoder = OneHotEncoder(categorical_features=self.categoricalIndexes)
        self.X = self.oneHotEncoder.fit_transform(X).toarray()
        self.dataset = dataset

    def transform(self, dataset):
        dataset = self._prepareDataset_(dataset)
        X = dataset.values
        for idx in self.categoricalIndexes:
            X[:, idx] = self.labelEncoders[idx].transform(X[:, idx])
        X = self.oneHotEncoder.transform(X).toarray()
        return X

    def getX(self):
        return self.X

    def getDataset(self):
        return self.dataset