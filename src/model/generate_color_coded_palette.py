#!/usr/bin/env python3

import numpy as np
import colorsys
import random

def generate_complementary_palette(initial_color, num_colors):
    # Convert the initial color from RGB to HSV
    r, g, b = initial_color
    h, s, v = colorsys.rgb_to_hsv(r, g , b)

    palette = []

    # Include the initial color as the first color
    palette.append(((r),(g),(b)))

    # Random chance to generate only shades and tints of the selected color
    if random.random() < 0.3:  # 50% chance to generate only shades and tints
        for i in range(num_colors - 1):
            factor = (i + 1) / num_colors
            new_s = min(max(s * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0), 1)
            new_v = min(max(v * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0.5), 1)
            new_h = (h + random.uniform(-0.05, 0.05)) % 1.0
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
            palette.append((new_r, new_g, new_b))
    else:
        # Calculate the number of colors to generate for each part
        num_initial_colors = (num_colors - 1) // 2
        num_complementary_colors = num_colors - 1 - num_initial_colors

        # Generate shades and tints of the initial color with some random variation
        for i in range(num_initial_colors):
            factor = (i + 1) / (num_initial_colors + 1)
            new_s = min(max(s * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0.5), 1)
            new_v = min(max(v * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0.5), 1)
            new_h = (h + random.uniform(-0.05, 0.05)) % 1.0
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
            palette.append((new_r, new_g, new_b))

        # Calculate the complementary hue with some random variation
        complementary_hue = (h + 0.5 + random.uniform(-0.05, 0.05)) % 1.0

        # Generate shades and tints of the complementary color with some random variation
        for i in range(num_complementary_colors):
            factor = (i + 1) / (num_complementary_colors + 1)
            new_s = min(max(s * (0.5 + factor * 0.5) + random.uniform(-0.2, 0.2), 0.5), 1)
            new_v = min(max(v * (0.5 + factor * 0.5) + random.uniform(-0.2, 0.2), 0.5), 1)
            new_h = (complementary_hue)
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
            palette.append((new_r, new_g, new_b))

    return palette
