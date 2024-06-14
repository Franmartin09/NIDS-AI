import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Cargar el DataFrame
df_training_large_even2 = pd.read_csv('prueba/training_large_even.csv', low_memory=False)

filtered_df1 = df_training_large_even2[df_training_large_even2['label'] == 1].head(433375)
filtered_df2 = df_training_large_even2[df_training_large_even2['label'] == 0]
unified_df = pd.concat([filtered_df1, filtered_df2], ignore_index=True)

class DataPreprocessor:
    def __init__(self, df, keys_order):
        self.keys_order = keys_order
        self.encoders = self.train_encoders(df)

    def train_encoders(self, df):
        encoders = {}
        for column in df.columns:
            if df[column].dtype == 'object':
                encoder = LabelEncoder()
                df[column] = encoder.fit_transform(df[column].astype(str))
                encoders[column] = encoder
        return encoders

    def save_encoders(self, path):
        joblib.dump(self.encoders, path)

    def load_encoders(self, path):
        self.encoders = joblib.load(path)

    def preprocess(self, data):
        data_values = list(data.values())
        data_values = {key: [data_values[idx]] for idx, key in enumerate(self.keys_order)}
        data_df = pd.DataFrame(data_values)
        
        # Apply Label Encoding for each column that is of type 'object'
        for column in data_df.columns:
            if data_df[column].dtype == 'object' and column in self.encoders:
                data_df[column] = self.encoders[column].transform(data_df[column].astype(str))
        
        print(data_df)
        return data_df

# Define your keys order
keys_order = ['src_ip', 'src_port', 'dst_ip', 'dst_port', 'proto', 'service', 'duration', 'src_bytes', 'dst_bytes', 'conn_state', 
              'missed_bytes', 'src_pkts', 'src_ip_bytes', 'dst_pkts', 'dst_ip_bytes', 'dns_query', 'dns_qclass', 'dns_qtype', 
              'dns_rcode', 'dns_AA', 'dns_RD', 'dns_RA', 'dns_rejected', 'ssl_version', 'ssl_cipher', 'ssl_resumed', 
              'ssl_established', 'ssl_subject', 'ssl_issuer', 'http_trans_depth', 'http_method', 'http_uri', 'http_version', 
              'http_request_body_len', 'http_response_body_len', 'http_status_code', 'http_user_agent', 'http_orig_mime_types', 
              'http_resp_mime_types', 'http_referrer', 'weird_name', 'weird_addl', 'weird_notice']

# Create your DataPreprocessor object and train the encoders
preprocessor = DataPreprocessor(unified_df, keys_order)

# Save the encoders to a file
preprocessor.save_encoders("encoders.joblib")

# Load the encoders from a file
preprocessor.load_encoders("encoders.joblib")

# Your sample data
data = {
    'src_ip': '192.168.1.190', 'src_port': 36806, 'dst_ip': '203.119.86.101', 'dst_port': 53, 'proto': 'udp', 'service': 'dns', 
    'duration': 0.0252, 'src_bytes': 48, 'dst_bytes': 491, 'conn_state': 'SF', 'missed_bytes': 0, 'src_pkts': 1, 'src_ip_bytes': 76, 
    'dst_pkts': 1, 'dst_ip_bytes': 519, 'dns_query': '195.41.in-addr.arpa', 'dns_qclass': 1, 'dns_qtype': 43, 'dns_rcode': 0, 
    'dns_AA': 'F', 'dns_RD': 'F', 'dns_RA': 'F', 'dns_rejected': 'F', 'ssl_version': '-', 'ssl_cipher': 0, 'ssl_resumed': 0, 
    'ssl_established': 0, 'ssl_subject': '-', 'ssl_issuer': '-', 'http_trans_depth': '-', 'http_method': '-', 'http_uri': '-', 
    'http_version': '-', 'http_request_body_len': 0, 'http_response_body_len': 0, 'http_status_code': 0, 'http_user_agent': '-', 
    'http_orig_mime_types': '-', 'http_resp_mime_types': '-', 'http_referrer': '-', 'weird_name': '-', 'weird_addl': '-', 
    'weird_notice': '-'
}

# Preprocess the data
preprocessed_data = preprocessor.preprocess(data)
print(preprocessed_data)
