import os

with open(r"d:\_AntiGravity\_playground\index_astronaut.html", "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    ('color: #444;', 'color: #94a3b8;'),
    ('color: #555;', 'color: #94a3b8;'),
    ('color: #999;', 'color: #64748b;'),
    ('color: #888;', 'color: #94a3b8;'),
    ('color:#777', 'color:#94a3b8'),
    ('color: #777;', 'color: #94a3b8;'),
    ('border-top: 1px solid #ddd;', 'border-top: 1px solid rgba(255,255,255,0.1);'),
    ('background: #fafafa; padding: 25px; border-radius: 8px; border: 1px solid #ddd;', 'background: rgba(15, 23, 42, 0.6); padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(12px); box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.05);'),
    ('border-left-color: #1565c0;', 'border-left-color: #00f3ff;'),
    ('border: 2px solid #6a1b9a;', 'border: 2px solid #ce5cff; box-shadow: 0 0 15px rgba(206, 92, 255, 0.3);'),
    ('border-top-color: #000;', 'border-top-color: #ffffff; box-shadow: 0 10px 30px rgba(255, 255, 255, 0.05), inset 0 0 10px rgba(255, 255, 255, 0.05);'),
    ('border-top-color: #f00;', 'border-top-color: #ff0055; box-shadow: 0 10px 30px rgba(255, 0, 85, 0.1), inset 0 0 10px rgba(255, 255, 255, 0.05);')
]

for old_str, new_str in replacements:
    html = html.replace(old_str, new_str)

with open(r"d:\_AntiGravity\_playground\index_astronaut.html", "w", encoding="utf-8") as f:
    f.write(html)
