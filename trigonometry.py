from __future__ import division
import math


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False


def rect_corners_from_center(center, width, hight):
    centerX = center[0]
    centerY = center[1]

    top_left = (int(centerX - width / 2), int(centerY - hight / 2))
    bottom_right = (int(centerX + width / 2), int(centerY + hight / 2))

    return top_left, bottom_right


def point_in_circle(angle, center_circle, radius_circle):
    radian = angle * 0.0174532925
    x = radius_circle * math.cos(radian) + center_circle[0]
    y = radius_circle * -math.sin(radian) + center_circle[1]
    coordinates_blob = (x, y)

    return coordinates_blob
