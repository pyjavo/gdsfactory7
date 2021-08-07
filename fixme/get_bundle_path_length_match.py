"""
Some manhattan routes have disconnected waveguides

Now we raise a warning

ideally we also enable:

- sbend routing
- 180 deg routing

"""

import gdsfactory


if __name__ == "__main__":
    c = gdsfactory.Component()
    # c1 = c << gdsfactory.c.straight_array(spacing=200)
    c1 = c << gdsfactory.c.array(pitch=50)
    c2 = c << gdsfactory.c.array(pitch=5)

    c2.movex(200)
    c1.y = 0
    c2.y = 0

    routes = gdsfactory.routing.get_bundle_path_length_match(
        c1.get_ports_list(orientation=0),
        c2.get_ports_list(orientation=180),
        end_straight_offset=0,
        start_straight=0,
        separation=50,
        # modify_segment_i=-3,
        # waveguide="nitride",
    )

    for route in routes:
        c.add(route.references)

    c.show()
