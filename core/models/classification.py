import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json
from core.models.preprocess import DataPreprocess

class XGBoostClassifier:
    def __init__(self, dataset):
        self.dataset = dataset
        self.model = None
        self.features = None
        self.target = None

    def preprocess_data(self):
        preprocessor = DataPreprocess(self.dataset)
        self.dataset = preprocessor.preprocess()

        self.features = self.dataset.drop('target_column', axis=1)
        self.target = self.dataset['target_column']

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.target, test_size=0.2, random_state=42)

        self.model = xgb.XGBClassifier()
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy}")

    def json_xgb_model(self, file_path):
        model_json = self.model.get_booster().get_dump(dump_format='json')
        
        return model_json
