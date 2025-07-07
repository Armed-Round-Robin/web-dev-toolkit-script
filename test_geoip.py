import geoip2.database
import subprocess

# Get your own IPv4 address
result = subprocess.run(['curl', '-4', 'ifconfig.me'], capture_output=True, text=True)
your_ip = result.stdout.strip()

print("Your IPv4 address:", your_ip)

# Path to the database
db_path = '/home/kali/app/ufonet/GeoLite2-City_20250704/GeoLite2-City.mmdb'

# Lookup your own IP
response = geoip2.database.Reader(db_path).city(your_ip)

if response.city.name:
    print("Your city:", response.city.name)
else:
    print("City info not available for your IP.")

