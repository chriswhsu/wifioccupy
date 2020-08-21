import paramiko
import logging as lgg
import time

lgg.basicConfig(level=lgg.INFO, format='%(asctime)s %(levelname)s %(message)s')

# This retrieves a Python logging instance (or creates it)
log = lgg.getLogger(__name__)


class Connection:
    host = "192.168.1.200"
    port = 22
    username = "root"
    password = "wifi"

    def make_connection(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, self.port, self.username, self.password)
        return client


class ChannelChanger:
    cm = Connection()
    client = cm.make_connection()

    CHAN_DICT_24 = {1: 2412,
                    2: 2417,
                    3: 2422,
                    4: 2427,
                    5: 2432,
                    6: 2437,
                    7: 2442,
                    8: 2447,
                    9: 2452,
                    10: 2457,
                    11: 2462
                    }

    CHAN_DICT_50 = {36: 5180,
                    40: 5200,
                    44: 5220,
                    48: 5240,
                    52: 5260,
                    56: 5280,
                    60: 5300,
                    64: 5320,
                    100: 5500,
                    104: 5520,
                    108: 5540,
                    112: 5560,
                    116: 5580,
                    120: 5600,
                    124: 5620,
                    128: 5640,
                    132: 5660,
                    136: 5680,
                    140: 5700,
                    144: 5720,
                    149: 5745,
                    153: 5765,
                    157: 5785,
                    161: 5805,
                    165: 5825}

    def get_50freq(self, channel):
        return self.CHAN_DICT_50[channel]

    def get_24freq(self, channel):
        return self.CHAN_DICT_24[channel]

    def change50_channel(self, channel):
        radio = 1
        beacons = 10
        frequency = self.get_50freq(channel)
        log.info("Changing 5GHz Radio to Channel {0}".format(channel))
        self.change_channel(radio, beacons, frequency)

    def change24_channel(self, channel):
        radio = 0
        beacons = 10
        frequency = self.get_24freq(channel)
        self.change_channel(radio, beacons, frequency)

    def change_channel(self, radio, beacons, frequency):
        try:
            command = "hostapd_cli -iwlan{0} chan_switch {1} {2}".format(radio, beacons, frequency)
            log.info(command)
            stdin, stdout, stderr = self.client.exec_command(command)
            lines = stdout.readlines()
            log.info(lines)
        except Exception as e:
            log.warning('Failure diuring change_channel: {0}'.format(e))

    def rotate50_channels(self, wait):
        while True:
            self.change50_channel(36)
            time.sleep(wait)
            self.change50_channel(149)
            time.sleep(wait)
            self.change50_channel(157)
            time.sleep(wait)
            self.change50_channel(165)
            time.sleep(wait)

    def rotate24_channels(self, wait):
        while True:
            self.change24_channel(1)
            time.sleep(wait)
            self.change24_channel(3)
            time.sleep(wait)
            self.change24_channel(6)
            time.sleep(wait)
            self.change24_channel(11)
            time.sleep(wait)


cc = ChannelChanger()
cc.rotate50_channels(1)
