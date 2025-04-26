class Television:
    """
    Class variables
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self) -> None:
        """
        Method to set default instance variables for the creation of television object
        """
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL


    def power(self) -> None:
        """
        Method to control tv power off and power on
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self) -> None:
        """
        Method to mute and un-mute tv
        """
        if self.__muted:
            self.__muted = False
        else:
            self.__muted = True


    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status:
                if self.__channel > Television.MIN_CHANNEL:
                    self.__channel -= 1
                else:
                    self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """
        Method to increase tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            #else:
            #    self.__volume = Television.MIN_VOLUME



    def volume_down(self) -> None:
        """
        Method to decrease tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            #else:
            #    self.__volume = Television.MAX_VOLUME



    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__status:
            if self.__muted:
                return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
            else:
                return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

