from cocos import cocosnode

__all__ = ['ProgressTimer']


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


Type = enum('ZERO', 'ONE', 'TWO')


class ProgressTimer():
    def __init__(self):
        self._type = Type.ONE

    @staticmethod
    def create(sprite):
        pass

    def get_type(self):
        return self._type

    def get_percent(self):
        return self._percentage

    def get_sprite(self):
        return self._sprite

    def set_type(self, type):
        pass

    def set_percent(self, percent):
        pass

    def set_sprite(self, sprite):
        pass

    def is_reverse_direction(self):
        return self._reverse_direction

    def set_reverse_direction(self, reverse_direction):
        return self._reverse_direction

    def get_midpoint(self):
        return self._midpoint

    def set_midpoint(self,point):
        pass

    def get_bar_change_rate(self):
        return self._bar_change_rate

    def set_bar_change_rate(self,bar_change_rate):
        pass


if __name__ == '__main__':
    p = ProgressTimer()
    print p.get_type()
