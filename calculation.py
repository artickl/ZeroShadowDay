#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from datetime import datetime, timedelta, timezone

# -----------------------------
# Configuration
# -----------------------------
LATITUDE = -1.2921       # Nairobi latitude (degrees)
LONGITUDE = 36.8219      # Nairobi longitude (degrees, east positive)
YEAR = 2026
TIMEZONE_OFFSET = 3      # East Africa Time (UTC+3)

# -----------------------------
# Solar math helpers (NOAA)
# -----------------------------
def deg2rad(d):
    return d * math.pi / 180.0

def rad2deg(r):
    return r * 180.0 / math.pi

def solar_declination(day_of_year):
    # Fractional year (radians)
    gamma = 2 * math.pi / 365 * (day_of_year - 1)

    # Declination in radians (NOAA approximation)
    decl = (
        0.006918
        - 0.399912 * math.cos(gamma)
        + 0.070257 * math.sin(gamma)
        - 0.006758 * math.cos(2 * gamma)
        + 0.000907 * math.sin(2 * gamma)
        - 0.002697 * math.cos(3 * gamma)
        + 0.00148  * math.sin(3 * gamma)
    )
    return rad2deg(decl)

def equation_of_time(day_of_year):
    gamma = 2 * math.pi / 365 * (day_of_year - 1)
    eot = (
        229.18 * (
            0.000075
            + 0.001868 * math.cos(gamma)
            - 0.032077 * math.sin(gamma)
            - 0.014615 * math.cos(2 * gamma)
            - 0.040849 * math.sin(2 * gamma)
        )
    )
    return eot  # minutes

def solar_noon(day_of_year):
    eot = equation_of_time(day_of_year)
    solar_noon_minutes = 720 - 4 * LONGITUDE - eot + TIMEZONE_OFFSET * 60
    return solar_noon_minutes

# -----------------------------
# Find zero-shadow dates
# -----------------------------
results = []

for day in range(1, 366):
    decl = solar_declination(day)
    if abs(decl - LATITUDE) < 0.1:  # tolerance in degrees
        results.append(day)

# Deduplicate close days
filtered_days = []
for d in results:
    if not filtered_days or abs(d - filtered_days[-1]) > 3:
        filtered_days.append(d)

# -----------------------------
# Output results
# -----------------------------
print("Zero-shadow events for Nairobi in", YEAR)
print("-----------------------------------")

for day in filtered_days:
    noon_minutes = solar_noon(day)
    hours = int(noon_minutes // 60)
    minutes = int(noon_minutes % 60)

    date = datetime(YEAR, 1, 1, tzinfo=timezone.utc) + timedelta(days=day - 1)
    local_time = datetime(
        YEAR, date.month, date.day, hours, minutes
    )

    print(
        f"{date.strftime('%Y-%m-%d')} at {local_time.strftime('%H:%M')} EAT"
    )