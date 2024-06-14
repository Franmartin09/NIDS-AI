import json
import joblib, os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model


class Model:
    def __init__(self):
        # self.model = joblib.load('clase/modulo/modelo.joblib')
        self.model = load_model("clase/modulo/rnn_final.h5")
        self.encoders = joblib.load("clase/modulo/encoders.joblib")
        self.keys_order = [
        "src_ip", "src_port", "dst_ip", "dst_port", "proto", "service", "duration",
        "src_bytes", "dst_bytes", "conn_state", "missed_bytes", "src_pkts",
        "src_ip_bytes", "dst_pkts", "dst_ip_bytes", "dns_query", "dns_qclass",
        "dns_qtype", "dns_rcode", "dns_AA", "dns_RD", "dns_RA", "dns_rejected",
        "ssl_version", "ssl_cipher", "ssl_resumed", "ssl_established", "ssl_subject",
        "ssl_issuer", "http_trans_depth", "http_method", "http_uri", "http_referrer", "http_version",
        "http_request_body_len", "http_response_body_len", "http_status_code",
        "http_user_agent", "http_orig_mime_types", "http_resp_mime_types", "weird_name",
        "weird_addl", "weird_notice"
        ]
        print("ModelClass inicialized!")
    
    
    def predict(self, data):
        return self.model.predict(data)
    
    def preproces(self, data):
        # data_values = {key: [data[key]] for key in self.keys_order} 
        # print(list(data.values()))
        data_values=list(data.values())
        data_values = {key: [data_values[idx]] for idx, key in enumerate(self.keys_order)}
        data_df = pd.DataFrame(data_values)
        # print(data)
        # print(data_df)
        # print(data_df['src_ip'].dtype)
        #  # Tokenización (si es necesario)
        encoder = LabelEncoder()
        # data_values = encoder.fit_transform(data_df)
        # Iterate through each column
        for column in data_df.columns:
            # if data_df[column].dtype == 'object':
                # data_df[column] = encoder.fit_transform(data_df[column].astype(str))
            if data_df[column].dtype == 'object' and column in self.encoders:
                print(data_df[column])
                # data_df[column] = self.encoders[column].transform(data_df[column].astype(str))
                try:
                    data_df[column] = self.encoders[column].transform(data_df[column].astype(str))
                except ValueError as e:
                    # data_df[column] = encoder.fit_transform(data_df[column].astype(str))
                    print(f"Warning: {e}")
                    # Asignar la etiqueta 'unknown' si no está presente en el encoder
                    unknown_label = 'unknown'
                    # Añadir la etiqueta 'unknown' al encoder
                    if unknown_label not in self.encoders[column].classes_:
                        self.encoders[column].classes_ = np.append(self.encoders[column].classes_, unknown_label)
                    # Transformar los datos
                    data_df[column] = data_df[column].apply(lambda x: x if x in self.encoders[column].classes_ else unknown_label)
                    data_df[column] = self.encoders[column].transform(data_df[column].astype(str))
        

        # print(data_df)
        # scaler = MinMaxScaler()
        # df_normalized = scaler.fit_transform(data_df)
        # df_normalized = pd.DataFrame(df_normalized, columns=data_df.columns)
        # data_df[df_normalized.columns] = df_normalized
        # print(np.array(data_df))
        print(np.array(data_df))
        return (data_df)

