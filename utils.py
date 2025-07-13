import requests
import base64
import json
import re
import socket

def extract_ip_from_connection(connection: str) -> str | None:
    """
    Extracts the server address (IP or domain) from various proxy URI schemes.
    Returns the host or None if parsing fails.
    """
    if not connection or not isinstance(connection, str):
        return None

    host = None
    try:
        if connection.startswith("vmess://"):
            encoded_part = connection.split("vmess://")[1]
            padding = len(encoded_part) % 4
            if padding:
                encoded_part += "=" * (4 - padding)
            decoded_json = base64.b64decode(encoded_part).decode("utf-8")
            host = json.loads(decoded_json).get("add")
        elif connection.startswith(("vless://", "trojan://")):
            # Format: protocol://user@host:port?params#name
            host = connection.split("@")[1].split("?")[0].split("#")[0].split(":")[0]
        elif connection.startswith("ss://"):
            # Shadowsocks format can be encoded or user:pass@host:port
            if "@" in connection:
                match = re.search(r"@([\w\.\-]+):", connection)
                if match:
                    host = match.group(1)
            else:
                # Encoded format: ss://method:pass@host:port or ss://base64...
                encoded_part = connection.split("://")[1].split("#")[0]
                if ":" not in encoded_part: # Likely base64
                    padding = len(encoded_part) % 4
                    if padding:
                        encoded_part += "=" * (4 - padding)
                    decoded_part = base64.b64decode(encoded_part).decode("utf-8")
                    host = decoded_part.split("@")[1].split(":")[0]
    except Exception:
        return None # Return None on any parsing error

    return host if host else None

def resolve_to_ip(host: str) -> str | None:
    """Resolves a domain name to an IP address."""
    if not host or not isinstance(host, str):
        return None
    # Basic regex to check if it's already an IP
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host):
        return host
    try:
        return socket.gethostbyname(host)
    except (socket.gaierror, UnicodeError):
        return None
