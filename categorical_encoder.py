import numpy as np
from sklearn.preprocessing import OrdinalEncoder


class Encoder:
    def __init__(self, data, cat_columns):
        self.frame = data
        self.cat_cols = cat_columns
        self.encoder = None
        self.encoded_frame = self.frame.copy()

    def category_encode(self):
        self.encoder = OrdinalEncoder(dtype = np.float64, unknown_value = np.nan, handle_unknown = "use_encoded_value")
        for column in self.cat_cols:
            self.encoded_frame[column] = self.encoder.fit_transform(self.encoded_frame[[column]])

    def get_encoded_data(self):
        self.category_encode()
        return self.encoded_frame
