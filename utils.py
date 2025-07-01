# utils.py
import csv
import os
from datetime import datetime

def check_direction(obj_id, current_x, history, counted_ids):
    direction = None
    updated = False

    if obj_id in history:
        prev_x = history[obj_id]
        delta = current_x - prev_x
        if abs(delta) > 20:  # Minimum movement threshold
            direction = "right" if delta > 0 else "left"
            if obj_id not in counted_ids:
                counted_ids.add(obj_id)
                updated = True
    history[obj_id] = current_x
    return direction, updated

def update_log(count):
    filename = "track_log.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Overwrite with the latest count
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "count"])
        writer.writerow([now, count])
