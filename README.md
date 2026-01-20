# Zero Shadow Day Calculator

**Zero Shadow Day** is a solar phenomenon that occurs when the Sun passes directly overhead at local solar noon.
At that moment, vertical objects cast little to no shadow.

In Hawaii, this event is known as **Lahaina Noon**, but it is also called **Día sin sombra** in Mexico, **Zero Shadow Day**
or **Day Without a Shadow** in other parts of the world. The phenomenon is not unique to Hawaii.
It can occur **anywhere on Earth located between the Tropic of Cancer (23.44° N) and the Tropic of Capricorn (23.44° S)**.
Most locations within this range experience it **twice each year**, while locations exactly on the tropics experience it once.

The event happens when the Sun’s **declination matches the latitude** of a location. Because the Sun’s declination changes
continuously throughout the year, the exact date and time depend on both **geographic location** and **year**.

This Python script calculates the **exact date and local solar noon time (down to the minute)** when the zero-shadow event
occurs for a given location. It uses standard solar position equations to track the Sun’s declination and determines when
it aligns with the specified latitude, making it possible to compute the event for **any place in the tropical zone worldwide**.

## Usage

1. Edit the configuration section of the script to set your location and year:

```python
LATITUDE = -1.2921       # Latitude in degrees (positive north, negative south)
LONGITUDE = 36.8219      # Longitude in degrees (positive east, negative west)
YEAR = 2026              # Year for calculation
TIMEZONE_OFFSET = 3      # Local time offset from UTC
```

2. Run the script

```python
python zero_shadow_day.py
```

3. The script will output the date(s) and local solar noon time(s) when vertical objects cast no shadow.

## Example Output (for Nairobi, Kenya, 2026)

```bash
$ python3 zero_shadow_day.py

Zero-shadow events for Nairobi in 2026
-----------------------------------
2026-03-19 at 12:36 EAT
2026-09-25 at 12:19 EAT
```

These correspond to the two annual occurrences of the Sun being directly overhead in Nairobi.

## Notes

1. Solar noon times account for longitude and the equation of time, but may differ slightly from clock noon.
2. The zero-shadow event lasts only a few minutes around solar noon.
3. For highest precision (seconds), astronomical ephemeris software or tools like Stellarium can be used.
