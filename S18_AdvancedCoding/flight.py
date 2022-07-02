"""
GLA -> LHR -> CAN
"""

from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        # self.segments[0].departure = val
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return ' -> '.join(stops)


flight = Flight([Segment('GLA', 'LHR')])
# flight.segments[0].departure = 'EDI'
flight.departure_point = 'EDI'
print(flight)
