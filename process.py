import base64
import dnslib
import json

data = json.load(open("atlas-results.json")) # from https://atlas.ripe.net/measurements/4480110/

for datum in data:
    if not "result" in datum:
        continue

    print("Client: %s" % datum["from"])

    print("Answer:")
    packet = base64.decodestring(datum["result"]["abuf"])
    record = dnslib.DNSRecord.parse(packet)
    print(repr(record))

    print("")
