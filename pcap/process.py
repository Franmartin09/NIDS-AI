import time
import json
import os

data_log = {
    "src_ip": "",
    "src_port": "",
    "dst_ip": "",
    "dsr_port": "",
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
    "dns_query": "",
    "dns_qclass": "",
    "dns_qtype": "",
    "dns_rcode": "",
    "dns_AA": "",
    "dns_RD": "",
    "dns_RA": "",
    "dns_rejected": "",
    "ssl_version": "",
    "ssl_cipher": "",
    "ssl_resumed": "",
    "ssl_established": "",
    "ssl_subject": "",
    "ssl_issuer": "",
    "http_trans_depth": "",
    "http_method": "",
    "http_uri": "",
    "http_version": "",
    "http_request_body_len": "",
    "http_response_body_len": "",
    "http_status_code": "",
    "http_user_agent": "",
    "http_orig_mime_types": "",
    "http_resp_mime_types": "",
    "weird_name": "",
    "weird_addl": "",
    "weird_notice": ""
}


def leer_conn(archivo):
    ultima_posicion = 0
    while True:
        with open(archivo, 'r') as f:
            f.seek(ultima_posicion)
            nuevas_lineas = f.read()
            if nuevas_lineas:
                for linea in nuevas_lineas.splitlines():
                    try:
                        objeto_json = json.loads(linea)

                        data_log.update({
                            "src_ip": objeto_json.get('id.orig_h', '-'),
                            "src_port": objeto_json.get('id.orig_p', '-'),
                            "dst_ip": objeto_json.get('id.resp_h', '-'),
                            "dsr_port": objeto_json.get('id.resp_p', '-'),
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

                        http_log = "http.log"
                        dns_log = "dns.log"
                        ssl_log = "ssl.log"
                        weird_log = "weird.log"
                        
                        data_dns = leer_dns(dns_log, objeto_json.get('uid', ''))
                        data_ssl = leer_ssl(ssl_log, objeto_json.get('uid', ''))
                        data_http = leer_http(http_log, objeto_json.get('uid', ''))
                        data_weird = leer_weird(weird_log, objeto_json.get('uid', ''))
                        
                        if data_dns:
                            data_log.update(data_dns)

                        if data_ssl:
                            data_log.update(data_ssl)

                        if data_http:
                            data_log.update(data_http)

                        if data_weird:
                            data_log.update(data_weird)

                        
                        print(data_log)
                        print("________________________")
                    except json.JSONDecodeError:
                        print(f"Error al decodificar JSON: {linea}")
                print("________________Hasta aqui he leido______________________")
                ultima_posicion += len(nuevas_lineas)
        time.sleep(1)

def leer_http(archivo, uid):
    if not os.path.exists(archivo):
        return None
    with open(archivo, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data['uid'] == uid:
                    data_http = {
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
                    }
                    break
                else:
                    data_http = {
                        "http_trans_depth": '-',
                        "http_method": '-',
                        "http_uri": '-',
                        "http_version": '-',
                        "http_request_body_len":  0,
                        "http_response_body_len":  0,
                        "http_status_code": 0,
                        "http_user_agent": '-',
                        "http_orig_mime_types": '-',
                        "http_resp_mime_types": '-',
                    }
            except json.JSONDecodeError:
                continue
        return data_http

def leer_dns(archivo, uid):
    if not os.path.exists(archivo):
        return None
    with open(archivo, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data['uid'] == uid:
                    data_dns = {
                        "dns_query": data.get('query', '-'),
                        "dns_qclass": data.get('qclass', '0'),
                        "dns_qtype": data.get('qtype', '0'),
                        "dns_rcode": data.get('rcode', '0'),
                        "dns_AA": "T" if data.get('AA', False) else "F" if data.get('AA', False) is not None else "-",
                        "dns_RD": "T" if data.get('RD', False) else "F" if data.get('RD', False) is not None else "-",
                        "dns_RA": "T" if data.get('RA', False) else "F" if data.get('RA', False) is not None else "-",
                        "dns_rejected": "T" if data.get('rejected', False) else "F" if data.get('rejected', False) is not None else "-"
                    }
                    break
                else:
                    data_dns = {
                        "dns_query": '-',
                        "dns_qclass": 0,
                        "dns_qtype": 0,
                        "dns_rcode": 0,
                        "dns_AA": "-",
                        "dns_RD": "-",
                        "dns_RA": "-",
                        "dns_rejected": "-"
                    }

            except json.JSONDecodeError:
                continue
        return data_dns
def leer_ssl(archivo, uid):
    if not os.path.exists(archivo):
        return None
    with open(archivo, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data['uid'] == uid:
                    data_ssl = {
                        "ssl_version": data.get('version', '-'),
                        "ssl_cipher": data.get('cipher', '-'),
                        "ssl_resumed": data.get('resumed', '-'),
                        "ssl_established": data.get('established', '-'),
                        "ssl_subject": data.get('server_name', '-'),
                        "ssl_issuer": data.get('curve', '-')
                    }
                    break
                else:
                    data_ssl = {
                        "ssl_version": '-',
                        "ssl_cipher": '-',
                        "ssl_resumed": '-',
                        "ssl_established": '-',
                        "ssl_subject": '-',
                        "ssl_issuer": '-'
                    }
                
            except json.JSONDecodeError:
                continue
        return data_ssl

def leer_weird(archivo, uid):
    if not os.path.exists(archivo):
        return None
    with open(archivo, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data['uid'] == uid:
                    data_weird = {
                        "weird_name": data.get('name', '-'),
                        "weird_addl": data.get('weird_addl', '-'),
                        "weird_notice": data.get('notice', '-')
                    }
                    break
                else:
                    data_weird = {
                        "weird_name": '-',
                        "weird_addl": '-',
                        "weird_notice": '-'
                    }
                
            except json.JSONDecodeError:
                continue
        return data_weird

if __name__ == "__main__":
    conn_log = "conn.log"
    leer_conn(conn_log)