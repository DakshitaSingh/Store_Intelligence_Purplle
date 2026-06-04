from layout_config import STORE_LAYOUTS


def get_zone(
    store_id,
    x,
    frame_width
):

    zones = STORE_LAYOUTS[
        store_id
    ]["zones"]

    ratio = x / frame_width

    for zone, bounds in zones.items():

        if (
            bounds[0]
            <= ratio <
            bounds[1]
        ):
            return zone

    return "UNKNOWN"