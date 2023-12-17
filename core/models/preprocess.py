from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest

class DataPreprocess():
    def __init__(self, dataset):
        self.dataset = dataset
        self.categorical_features = None
        self.numerical_features = None

    def _identify_features(self):
        self.categorical_features = self.dataset.select_dtypes(include=['object']).columns.tolist()
        self.numerical_features = self.dataset.select_dtypes(include=['float64', 'int64']).columns.tolist()

    def _label_encoding(self):
        if self.categorical_features:
            for col in self.categorical_features:
                label_encoder = LabelEncoder()
                self.dataset[col] = label_encoder.fit_transform(self.dataset[col])

    def _standard_scaling(self):
        if self.numerical_features:
            scaler = StandardScaler()
            self.dataset[self.numerical_features] = scaler.fit_transform(self.dataset[self.numerical_features])

    def _handle_missing_values(self, strategy='mean'):
        imputer = SimpleImputer(strategy=strategy)
        self.dataset[self.numerical_features] = imputer.fit_transform(self.dataset[self.numerical_features])

    def _remove_outliers(self):
        if self.numerical_features:
            outlier_detector = IsolationForest()
            self.dataset['outlier'] = outlier_detector.fit_predict(self.dataset[self.numerical_features])
            self.dataset = self.dataset[self.dataset['outlier'] == 1].drop(columns='outlier')

    def preprocess(self):
        self._identify_features()
        self._label_encoding()
        self._standard_scaling()
        self._handle_missing_values()
        self._remove_outliers()
        return self.dataset