from wrapper import StabConnector

if __name__ == "__main__":
    stabConnector = StabConnector(ip='192.168.2.223', port=0, data_block=1)

    if stabConnector.enableVisionCheck():
        stabConnector.elementIsValid()

