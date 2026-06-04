import uuid
import time


class VisitorTracker:

    def __init__(self):

        self.visitors = {}

    def get_or_create(
        self,
        track_id
    ):

        if track_id not in self.visitors:

            self.visitors[track_id] = {

                "visitor_id":
                f"VIS_{uuid.uuid4().hex[:8]}",

                "entered":
                False,

                "last_zone":
                None,

                "zone_start":
                time.time(),

                "reentered":
                False
            }

        return self.visitors[track_id]