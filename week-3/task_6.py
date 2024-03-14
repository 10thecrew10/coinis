from typing import List


class Televisor:
    def __init__(self, channel_num: int = 0, channel_name: str = '', channels: List[str] = [], volume: int = 0):
        self._channels = channels
        self._channel_num = channel_num
        self._channel_name = channel_name
        self._volume = volume

    def add_channel(self, name: str):
        self.channels.append(name)

    def delete_channel(self, name: str):
        self.channels.remove(name)

    def increase_volume(self):
        if self.volume == 10:
            print('Max volume')
            return
        self.volume += 1

    def find_name(self, n: int):
        if not (1 <= n <= len(self.channels)):
            print(ValueError('Incorrect channel number'))
            return
        return self.channels[n - 1]

    @property
    def channel_num(self):
        return self._channel_num

    @channel_num.setter
    def channel_num(self, value: int):
        if not (0 <= value <= len(self.channels)):
            print(ValueError('Attribute "channel_num" must be in range [0, len(channels)]'))
            return
        self._channel_num = value

    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value: str):
        if not value:
            print(ValueError('Attribute "channel_name" must contains 1 symbol'))
            return
        self._channel_name = value

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value: List[str]):
        self._channels = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: int):
        if not (0 <= value <= 10):
            print(ValueError('Attribute "volume" must be between 0 and 10'))
            return
        self._volume = value


t = Televisor(0, "Arigato", ['BBC', 'Discovery', 'National Geographic', 'Arigato'], 3)
t.add_channel("First")
t.delete_channel("First")
print(t.channels)
print(t.volume)
t.increase_volume()
print(t.volume)
print(t.find_name(10))
print(t.find_name(2))
