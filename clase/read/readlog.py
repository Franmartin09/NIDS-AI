import json
import time
import os
import numpy as np
from datetime import datetime


class ReadLog:
    def __init__(self):
        self.ultima_posicion = 0
        self.data_log = {}
        print("ReadClass initialized!")

    def inicialice_data_log(self):
            self.data_log = {
            "src_ip": "",
            "src_port": "",
            "dst_ip": "",
            "dst_port": "",
            "proto": "",
            "service": "",
            "duration": "",
            "src_bytes": "",
            "dst_bytes": "",
            "conn_state": "",
            "missed_bytes": "",
            "src_pkts": "",
            "src_ip_bytes": "",
            "dst_pkts": "",
            "dst_ip_bytes": "",
            "dns_query": "-",
            "dns_qclass": 0,
            "dns_qtype": 0,
            "dns_rcode": 0,
            "dns_AA": "-",
            "dns_RD": "-",
            "dns_RA": "-",
            "dns_rejected": "",
            "ssl_version": "-",
            "ssl_cipher": 0,
            "ssl_resumed": 0,
            "ssl_established": 0,
            "ssl_subject": "-",
            "ssl_issuer": "-",
            "http_trans_depth": "-",
            "http_method": "-",
            "http_uri": "-",
            "http_version": "-",
            "http_request_body_len": 0,
            "http_response_body_len": 0,
            "http_status_code": 0,
            "http_user_agent": "-",
            "http_orig_mime_types": "-",
            "http_resp_mime_types": "-",
            "http_referrer": "-",
            "weird_name": "-",
            "weird_addl": "-",
            "weird_notice": "-"
        }

    def read_log(self, app, model):
        if app.execute_bool:
            with open("pcap/conn.log", 'r') as file:
                file.seek(self.ultima_posicion)
                lineas = file.read().splitlines()
                if len(lineas)>self.ultima_posicion:
                        try:
                            objeto_json = json.loads(lineas[self.ultima_posicion])
                            self.inicialice_data_log()
                            self.data_log.update({
                                "src_ip": objeto_json.get('id.orig_h', '-'),
                                "src_port": objeto_json.get('id.orig_p', '-'),
                                "dst_ip": objeto_json.get('id.resp_h', '-'),
                                "dst_port": objeto_json.get('id.resp_p', '-'),
                                "proto": objeto_json.get('proto', '-'),
                                "service": objeto_json.get('service', '-'),
                                "duration": objeto_json.get('duration', 0),
                                "src_bytes": objeto_json.get('orig_bytes', 0),
                                "dst_bytes": objeto_json.get('resp_bytes', 0),
                                "conn_state": objeto_json.get('conn_state', '-'),
                                "missed_bytes": objeto_json.get('missed_bytes', '-'),
                                "src_pkts": objeto_json.get('orig_pkts', '-'),
                                "src_ip_bytes": objeto_json.get('orig_ip_bytes', '-'),
                                "dst_pkts": objeto_json.get('resp_pkts', '-'),
                                "dst_ip_bytes": objeto_json.get('resp_ip_bytes', '-')
                            })

                            http_log = "pcap/http.log"
                            dns_log = "pcap/dns.log"
                            ssl_log = "pcap/ssl.log"
                            weird_log = "pcap/weird.log"

                            data_dns = self.read_dns(dns_log, objeto_json.get('uid', ''))
                            data_ssl = self.read_ssl(ssl_log, objeto_json.get('uid', ''))
                            data_http = self.read_http(http_log, objeto_json.get('uid', ''))
                            data_weird = self.read_weird(weird_log, objeto_json.get('uid', ''))
                            # print(data_dns)
                            if data_dns:
                                self.data_log.update(data_dns)

                            if data_ssl:
                                self.data_log.update(data_ssl)

                            if data_http:
                                self.data_log.update(data_http)

                            if data_weird:
                                self.data_log.update(data_weird)

                            data = model.preproces(self.data_log)
                            # print(data)
                            prediction = model.predict(data)
                            print(prediction)
                            res = np.argmax(prediction)
                            print("{:.2f}".format(float(np.max(prediction)*100)))
                            if res==1:
                                log_line = f"Ts:{datetime.fromtimestamp(objeto_json.get('ts', '-')).strftime('%Y-%m-%d %H:%M:%S')}, Src IP: {self.data_log['src_ip']}, Proto: {self.data_log['proto']}, Amb una prediccio de un: {"{:.2f}".format(float(np.max(prediction)*100))} %"
                                app.update_scrollable_frame(log_line)
                                # app.update_scrollable_frame(log_line)
                                # self.previous_lines.add(log_line)
                        except (json.JSONDecodeError, IndexError):
                            app.update_scrollable_frame(f"Error al decodificar JSON o leer fichero")
                        self.ultima_posicion += 1
                    
        app.root.after(100, self.read_log, app, model)

    def read_http(self, archivo, uid):
        if not os.path.exists(archivo):
            return None
        with open(archivo, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data['uid'] == uid:
                        return {
                            "http_trans_depth": data.get('trans_depth', '-'),
                            "http_method": data.get('method', '-'),
                            "http_uri": data.get('uri', '-'),
                            "http_version": data.get('version', '-'),
                            "http_request_body_len": data.get('request_body_len', 0),
                            "http_response_body_len": data.get('response_body_len', 0),
                            "http_status_code": data.get('status_code', 0),
                            "http_user_agent": data.get('user_agent', '-'),
                            "http_orig_mime_types": data.get('http_orig_mime_types', '-'),
                            "http_resp_mime_types": data.get('http_resp_mime_types', '-'),
                            "http_referrer": data.get('http_referrer', '-')
                        }
                except json.JSONDecodeError:
                    continue
        return None

    def read_dns(self, archivo, uid):
        if not os.path.exists(archivo):
            return None
        with open(archivo, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data['uid'] == uid:
                        return {
                            "dns_query": data.get('query', '-'),
                            "dns_qclass": data.get('qclass', '0'),
                            "dns_qtype": data.get('qtype', '0'),
                            "dns_rcode": data.get('rcode', '0'),
                            "dns_AA": 'F' if data.get('AA')=='F' else ("T" if data.get('AA', False) else "F"),
                            "dns_RD": 'F' if data.get('RD')=='F' else ("T" if data.get('AA', False) else "F"),
                            "dns_RA": 'F' if data.get('RA')=='F' else ("T" if data.get('AA', False) else "F"),
                            "dns_rejected": 'F' if data.get('rejected')=='F' else ("T" if data.get('rejected', False) else "F"),
                        }
                except json.JSONDecodeError:
                    continue
        return None

    def read_ssl(self, archivo, uid):
        if not os.path.exists(archivo):
            return None
        with open(archivo, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data['uid'] == uid:
                        return {
                            "ssl_version": data.get('version', '-'),
                            "ssl_cipher": data.get('cipher', '-'),
                            "ssl_resumed": data.get('resumed', '-'),
                            "ssl_established": data.get('established', '-'),
                            "ssl_subject": data.get('server_name', '-'),
                            "ssl_issuer": data.get('curve', '-')
                        }
                except json.JSONDecodeError:
                    continue
        return None

    def read_weird(self, archivo, uid):
        if not os.path.exists(archivo):
            return None
        with open(archivo, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data['uid'] == uid:
                        return {
                            "weird_name": data.get('name', '-'),
                            "weird_addl": data.get('weird_addl', '-'),
                            "weird_notice": data.get('notice', '-')
                        }
                except json.JSONDecodeError:
                    continue
        return None
    