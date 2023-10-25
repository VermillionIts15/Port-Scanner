import socket

def port_info(ip, port):
    try:
        service_info = socket.getservbyport(port)
        protocol_map = {
            6: "TCP",
            17: "UDP"
        }

        protocol_name = protocol_map.get(port, "Desconhecido")
        
        # Obtém a família de protocolos (IPv4 ou IPv6)
        family = socket.AF_INET if ':' not in ip else socket.AF_INET6
        hostname, _, _ = socket.gethostbyaddr(ip)

        print(f"IP de destino: {ip}")
        print(f"Porta: {port}")
        print(f"Nome do serviço: {service_info}")
        print(f"Tipo de protocolo: {protocol_name}")
        print(f"Família de protocolos: {family}")
        print(f"Nome do host: {hostname}")
    except Exception as e:
        print(f"Erro ao obter informações da porta {port}: {e}")

if __name__ == "__main__":
    ip = input("Informe o IP de destino: ")
    port = int(input("Informe o número da porta: "))

    port_info(ip, port)
