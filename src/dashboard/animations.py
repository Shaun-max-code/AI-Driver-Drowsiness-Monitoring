"""
Dashboard Animations
"""


def lerp(current, target, alpha=0.15):
    """
    Smooth transition.

    current -> target
    """

    return current + (target - current) * alpha