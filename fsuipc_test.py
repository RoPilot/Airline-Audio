from fsuipc import FSUIPC


with FSUIPC() as fsuipc:
    prepared = fsuipc.prepare_data([
        (0x560, "s"),
        (0x568, "l"),
        (0x2B4, "l")
    ], True)

    while True:
        latitude, longitude, altitude = prepared.read()

        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Altitude: {altitude}")

        input("Press ENTER to read again")