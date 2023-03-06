import pandas as pd
import numpy as np

class Pipeline:
    
    def __init__(self, data):
        import joblib
        self.df = pd.read_json(data)
        self.model = joblib.load('cltv_predictor.joblib')
        self.data_to_encode = pd.read_csv('train_BRCpofr.csv')
    
    def drop_columns(self):
        self.df = self.df.drop(['vintage', 'claim_amount', 'id'], axis=1)
        self.data_to_encode = self.data_to_encode.drop(['vintage', 'claim_amount', 'id', 'cltv'], axis=1)
        
        return self.df
    
    def replace_values(self):
        replace_gender = {
                    'Male' : 0,
                    'Female' : 1,
        }
        self.df['gender'] = self.df['gender'].map(replace_gender)
        self.data_to_encode['gender'] = self.data_to_encode['gender'].map(replace_gender)
        
        replace_type_of_policy = {
                    'Silver' : 0,
                    'Gold' : 1,
                    'Platinum' : 2
        }
        self.df['type_of_policy'] = self.df['type_of_policy'].map(replace_type_of_policy)
        self.data_to_encode['type_of_policy'] = self.data_to_encode['type_of_policy'].map(replace_type_of_policy)

        
        return self.df
    
    def one_hot_encoder(self):
        from category_encoders.one_hot import OneHotEncoder
        self.encoder = OneHotEncoder(cols=['area', 'qualification', 'income', 'num_policies', 'policy'], handle_missing="value", handle_unknown="value")
        self.encoder.fit(self.data_to_encode)
        self.df = self.encoder.transform(self.df)

        return self.df
    
    def predict(self):
        self.df['predict'] = self.model.predict(self.df)
        
        return self.df
    
    def transform_predict(self):
        self.df['predict'] = np.exp(self.df['predict'])

        return self.df
    
    def execute_pipe(self):
        self.df = self.drop_columns()
        self.df = self.replace_values()
        self.df = self.one_hot_encoder()
        self.df = self.predict()
        self.df = self.transform_predict()

        return self.df.to_json()


# json = pd.read_csv('test_koRSKBP.csv').to_json()
# json = 'dados_para_prever.json'
# pipe = Pipeline(json)
# df_test = pipe.execute_pipe()
# print((df_test))