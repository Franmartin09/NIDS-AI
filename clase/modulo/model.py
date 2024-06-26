import json
import joblib, os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle 

class Model:
    def __init__(self):
        self.model = load_model("clase/modulo/rnn_final_final.h5")
        pkl_file = open('clase/modulo/label_encoders.pkl', 'rb')
        self.encoders = pickle.load(pkl_file) 
        pkl_file.close()
        self.keys_order = [
        "src_ip", "src_port", "dst_ip", "dst_port", "proto", "service", "duration",
        "src_bytes", "dst_bytes", "conn_state", "missed_bytes", "src_pkts",
        "src_ip_bytes", "dst_pkts", "dst_ip_bytes", "dns_query", "dns_qclass",
        "dns_qtype", "dns_rcode", "dns_AA", "dns_RD", "dns_RA", "dns_rejected",
        "ssl_version", "ssl_cipher", "ssl_resumed", "ssl_established", "ssl_subject",
        "ssl_issuer", "http_trans_depth", "http_method", "http_uri", "http_version",
        "http_request_body_len", "http_response_body_len", "http_status_code",
        "http_user_agent", "http_orig_mime_types", "http_resp_mime_types", "http_referrer", "weird_name",
        "weird_addl", "weird_notice"
        ]
        print("ModelClass inicialized!")
    
    
    def predict(self, data):
        return self.model.predict(data)
    
    def preproces(self, data):
        data_values=list(data.values())
        data_values = {key: [data_values[idx]] for idx, key in enumerate(self.keys_order)}
        data_df = pd.DataFrame(data_values)

        for column in data_df.columns:
            # print(column)
            if column in self.encoders:
                # print(column)
                encoder = self.encoders[column]
                new_values = data_df[column].apply(lambda x: x not in encoder.classes_)
                if new_values.any():
                    # Añadir nuevas clases al encoder
                    new_classes = list(set(data_df[column][new_values]))
                    updated_classes = list(encoder.classes_) + new_classes
                    encoder.classes_ = np.array(updated_classes)
                
                data_df[column] = encoder.transform(data_df[column])

        return (np.array(data_df))

