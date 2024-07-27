#!/usr/bin/env python3

import numpy as np
import colorsys
import random

def generate_complementary_palette(initial_color, num_colors):
    # Convert the initial color from RGB to HSV
    r, g, b = initial_color
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    
    palette = []
    
    # Generate shades and tints of the initial color with some random variation
    for i in range(num_colors // 2):
        factor = i / (num_colors // 2)
        new_s = min(max(s * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0), 1)
        new_v = min(max(v * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0), 1)
        new_h = (h + random.uniform(-0.05, 0.05)) % 1.0
        new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
        palette.append((new_r, new_g, new_b))
    
    # Calculate the complementary hue with some random variation
    complementary_hue = (h + 0.5 + random.uniform(-0.05, 0.05)) % 1.0
    
    # Generate shades and tints of the complementary color with some random variation
    for i in range((num_colors + 1) // 2):  # Ensure we generate enough colors
        factor = i / ((num_colors + 1) // 2)
        new_s = min(max(s * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0), 1)
        new_v = min(max(v * (0.5 + factor * 0.5) + random.uniform(-0.1, 0.1), 0), 1)
        new_h = (complementary_hue + random.uniform(-0.05, 0.05)) % 1.0
        new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
        palette.append((new_r, new_g, new_b))
    
    return palette[:num_colors]