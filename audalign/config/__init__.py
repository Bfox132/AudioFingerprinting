import typing
from abc import ABC


class BaseConfig(ABC):
    used_parameters = set()
    set_parameters = set()
    extra_parameters = {}
    freq_threshold = 44100
    multiprocessing = True
    num_processors = None
    start_end = None
    plot = False
    max_lags: typing.Optional[float] = None
    filter_matches: typing.Optional[int] = None
    sample_rate = 44100
    match_len_filter: typing.Optional[int] = None

    CONFIDENCE = "confidence"
    MATCH_TIME = "match_time"
    OFFSET_SAMPLES = "offset_frames"
    OFFSET_SECS = "offset_seconds"
    LOCALITY = "locality_frames"
    LOCALITY_SECS = "locality_seconds"

    rankings_no_locality_top_match_tups: tuple = ()
    rankings_locality_top_match_tups: tuple = ()
    rankings_minus: tuple = ()
    rankings_second_is_close_add: int = 1
    rankings_get_top_num_match: typing.Optional[str] = None
    rankings_num_matches_tups: typing.Optional[tuple] = None

    def __init__(self, set_parameters: dict = {}, extra_parameters: dict = {}):
        for param, value in set_parameters.items():
            if param in self.used_parameters:
                self.set_parameters[param] = value
                self.__dict__[param] = value
            else:
                self.extra_parameters[param] = value
