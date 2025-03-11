from math import cos, radians, sin, sqrt, tan


ROBOT_CENTRE_TO_APRILTAG = 17.125
APRILTAG_CENTRE_TO_POLE = 6.47
APRIL_TAG_INFO = [
    {"id": 6, "x": 13.474446, "y": 3.3063179999999996, "rotation": 300},
    {"id": 7, "x": 13.890498, "y": 4.0259, "rotation": 0},
    {"id": 8, "x": 13.474446, "y": 4.745482, "rotation": 60},
    {"id": 9, "x": 12.643358, "y": 4.745482, "rotation": 120},
    {"id": 10, "x": 12.227305999999999, "y": 4.0259, "rotation": 180},
    {"id": 11, "x": 12.643358, "y": 3.3063179999999996, "rotation": 240},
    {"id": 17, "x": 4.073905999999999, "y": 3.3063179999999996, "rotation": 240},
    {"id": 18, "x": 3.6576, "y": 4.0259, "rotation": 180},
    {"id": 19, "x": 4.073905999999999, "y": 4.745482, "rotation": 120},
    {"id": 20, "x": 4.904739999999999, "y": 4.745482, "rotation": 60},
    {"id": 21, "x": 5.321046, "y": 4.0259, "rotation": 0},
    {"id": 22, "x": 4.904739999999999, "y": 3.3063179999999996, "rotation": 300},
]


def get_left_pair(a, b, x, y, rotation):
    length = get_left_right_length(a, b)
    return (
        x + length * get_x_portion_left(a, b, rotation) / 39.37,
        y + length * get_y_portion_left(a, b, rotation) / 39.37,
    )


def get_right_pair(a, b, x, y, rotation):
    length = get_left_right_length(a, b)
    return (
        x + length * get_x_portion_right(a, b, rotation) / 39.37,
        y + length * get_y_portion_right(a, b, rotation) / 39.37,
    )


def get_middle_pair(a, x, y, rotation):
    return (
        x + a * get_x_portion(rotation) / 39.37,
        y + a * get_y_portion(rotation) / 39.37,
    )


def get_left_right_length(a, b):
    return sqrt((a**2) + (b**2))


def get_x_portion(angle, adjust=0):
    return cos(radians(angle) + adjust)


def get_y_portion(angle, adjust=0):
    return sin(radians(angle) + adjust)


def get_x_portion_left(a, b, angle):
    return get_x_portion(angle, tan(b / a) * -1)


def get_y_portion_left(a, b, angle):
    return get_y_portion(angle, tan(b / a) * -1)


def get_x_portion_right(a, b, angle):
    return get_x_portion(angle, tan(b / a))


def get_y_portion_right(a, b, angle):
    return get_y_portion(angle, tan(b / a))


def print_map_line(id, x, y, rotation):
    print(f"map.put( {id}, new Pose2d({x}, {y}, Rotation2d.fromDegrees({rotation})) );")


print("Left:")
for info in APRIL_TAG_INFO:

    (x, y) = get_left_pair(
        ROBOT_CENTRE_TO_APRILTAG,
        APRILTAG_CENTRE_TO_POLE,
        info["x"],
        info["y"],
        info["rotation"],
    )
    print_map_line(info["id"], x, y, info["rotation"])

print("Right:")
for info in APRIL_TAG_INFO:

    (x, y) = get_right_pair(
        ROBOT_CENTRE_TO_APRILTAG,
        APRILTAG_CENTRE_TO_POLE,
        info["x"],
        info["y"],
        info["rotation"],
    )
    print_map_line(info["id"], x, y, info["rotation"])

print("Centre:")
for info in APRIL_TAG_INFO:

    (x, y) = get_middle_pair(
        ROBOT_CENTRE_TO_APRILTAG,
        info["x"],
        info["y"],
        info["rotation"],
    )
    print_map_line(info["id"], x, y, info["rotation"])
