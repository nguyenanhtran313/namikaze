import re
import os

html_path = r"d:\_AntiGravity\_playground\index.html"
astro_path = r"d:\_AntiGravity\_playground\index_astronaut.html"
looker_path = r"d:\_AntiGravity\_playground\index_looker.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# ================= ASTRONAUT THEME =================
css_astronaut = """<style>
    .reveal {
      font-family: 'Inter', sans-serif;
      font-size: 24px;
      color: #e2e8f0;
      background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
    }

    .reveal h1,
    .reveal h2,
    .reveal h3,
    .reveal h4 {
      font-family: 'Inter', sans-serif;
      text-transform: uppercase;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 24px;
      letter-spacing: -0.015em;
    }

    .reveal h1 {
      font-size: 2.3em;
      text-align: left;
      line-height: 1.1;
      text-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
    }

    .reveal h2 {
      font-size: 1.5em;
      text-align: left;
      border-bottom: 3px solid #00f3ff;
      padding-bottom: 12px;
      display: inline-block;
      margin-bottom: 35px;
      text-shadow: 0 0 10px rgba(0, 243, 255, 0.3);
    }

    .reveal h3 {
      font-size: 1.15em;
      text-align: left;
      color: #cbd5e1;
    }

    .reveal p {
      font-size: 1em;
      line-height: 1.6;
      text-align: left;
      font-weight: 400;
      color: #cbd5e1;
    }

    .reveal ul {
      display: block;
      text-align: left;
      font-weight: 400;
      font-size: 0.95em;
      color: #cbd5e1;
      padding-left: 20px;
    }

    .reveal li {
      margin-bottom: 14px;
    }

    .reveal strong {
      font-weight: 800;
      color: #ffffff;
      text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
    }

    .highlight-green {
      color: #00ffaa;
      font-weight: 800;
      text-shadow: 0 0 8px rgba(0, 255, 170, 0.4);
    }

    .highlight-blue {
      color: #00f3ff;
      font-weight: 800;
      text-shadow: 0 0 8px rgba(0, 243, 255, 0.4);
    }

    .highlight-purple {
      color: #ce5cff;
      font-weight: 800;
      text-shadow: 0 0 8px rgba(206, 92, 255, 0.5);
    }

    .serif-quote {
      font-family: 'Playfair Display', serif;
      font-size: 1.25em;
      font-style: italic;
      color: #94a3b8;
      border-left: 4px solid #ff00ea;
      padding-left: 24px;
      margin: 30px 0;
      text-align: left;
      line-height: 1.4;
      background: rgba(255, 0, 234, 0.05);
      border-radius: 0 10px 10px 0;
      box-shadow: inset 5px 0 15px rgba(255, 0, 234, 0.1);
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 20px;
    }

    /* Card Styling */
    .card {
      background: rgba(15, 23, 42, 0.6);
      padding: 25px;
      border-radius: 12px;
      border-top: 5px solid #475569;
      text-align: left;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 10px rgba(255, 255, 255, 0.05);
      font-size: 0.85em;
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255,255,255,0.05);
      border-left: 1px solid rgba(255,255,255,0.05);
      border-right: 1px solid rgba(255,255,255,0.05);
    }

    .card-claude {
      border-top-color: #00ffaa;
      box-shadow: 0 10px 30px rgba(0, 255, 170, 0.05), inset 0 0 10px rgba(255, 255, 255, 0.05);
    }

    .card-gemini {
      border-top-color: #00f3ff;
      box-shadow: 0 10px 30px rgba(0, 243, 255, 0.05), inset 0 0 10px rgba(255, 255, 255, 0.05);
    }

    .card-anti {
      border-top-color: #ce5cff;
      box-shadow: 0 10px 30px rgba(206, 92, 255, 0.05), inset 0 0 10px rgba(255, 255, 255, 0.05);
    }

    /* Table Styling */
    .reveal table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 0.7em;
      margin-top: 20px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
      border-radius: 10px;
      overflow: hidden;
    }

    .reveal th,
    .reveal td {
      border-bottom: 1px solid rgba(255,255,255,0.05);
      padding: 14px 12px;
      text-align: left;
      line-height: 1.4;
    }

    .reveal th {
      font-weight: 800;
      color: #ffffff;
      background-color: rgba(30, 41, 59, 1);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 2px solid rgba(255,255,255,0.1);
    }
    
    .reveal td {
      background-color: rgba(15, 23, 42, 0.5);
      backdrop-filter: blur(5px);
    }

    /* Navigation Buttons on Cover */
    .nav-menu {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 40px;
      justify-content: flex-start;
    }

    .nav-btn {
      padding: 10px 18px;
      border: 1px solid rgba(0, 243, 255, 0.3);
      background: rgba(15, 23, 42, 0.7);
      color: #00f3ff;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 0.55em;
      text-transform: uppercase;
      letter-spacing: 1px;
      cursor: pointer;
      border-radius: 40px;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      backdrop-filter: blur(8px);
      text-decoration: none !important;
      box-shadow: 0 0 10px rgba(0,255,255,0.1);
    }

    .nav-btn:hover {
      background: #00f3ff;
      color: #000;
      transform: translateY(-3px) scale(1.05);
      box-shadow: 0 0 20px rgba(0, 243, 255, 0.6);
      border-color: #00f3ff;
    }

    .nav-btn:active {
      transform: translateY(0) scale(0.95);
    }

    /* Terminal/Code Example Style */
    .terminal-box {
      background: #0d1117;
      color: #c9d1d9;
      padding: 20px;
      border-radius: 10px;
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.65em;
      line-height: 1.5;
      margin-top: 15px;
      position: relative;
      border: 1px solid rgba(255,255,255,0.1);
      border-top: 30px solid #161b22;
      box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 5px 15px rgba(0,0,0,0.3);
    }

    .terminal-box::before {
      content: "● ● ●";
      position: absolute;
      top: -22px;
      left: 12px;
      color: #ff5f56;
      font-size: 13px;
      letter-spacing: 3px;
      text-shadow: 18px 0 0 #ffbd2e, 36px 0 0 #27c93f;
    }

    .terminal-prompt {
      color: #7ee787;
    }

    .terminal-cmd {
      color: #ff7b72;
    }

    .terminal-output {
      color: #79c0ff;
    }

    .subtitle {
      font-size: 0.65em;
      color: #00f3ff;
      text-transform: uppercase;
      letter-spacing: 3px;
      margin-bottom: 20px;
      display: block;
      text-align: left;
      font-weight: 600;
      text-shadow: 0 0 8px rgba(0, 243, 255, 0.4);
      letter-spacing: 4px;
    }

    .text-sm {
      font-size: 0.75em !important;
      line-height: 1.6;
      color: #cbd5e1;
    }

    .badge {
      display: inline-block;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.75em;
      font-weight: 800;
      color: #000;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-right: 10px;
      box-shadow: 0 0 10px rgba(255,255,255,0.2);
    }

    .bg-green {
      background-color: #00ffaa;
      box-shadow: 0 0 12px rgba(0, 255, 170, 0.6);
    }

    .bg-blue {
      background-color: #00f3ff;
      box-shadow: 0 0 12px rgba(0, 243, 255, 0.6);
    }

    .bg-purple {
      background-color: #ce5cff;
      color: white;
      box-shadow: 0 0 12px rgba(206, 92, 255, 0.6);
    }

    .reveal-viewport {
      background: #090a0f;
    }

    /* Global Home Button */
    .home-btn {
      position: fixed;
      top: 40px;
      right: 50px;
      z-index: 9999;
      font-family: 'Inter', sans-serif;
      font-weight: 800;
      font-size: 14px;
      letter-spacing: 2px;
      color: #00f3ff;
      text-decoration: none;
      text-transform: uppercase;
      opacity: 0;
      pointer-events: none;
      transition: all 0.4s ease;
      padding-bottom: 4px;
      border-bottom: 2px solid transparent;
      text-shadow: 0 0 8px rgba(0, 243, 255, 0.6);
    }

    .home-btn:hover {
      opacity: 1 !important;
      border-bottom-color: #00f3ff;
      transform: translateY(-2px);
    }

    .home-btn:active {
      transform: translateY(0);
    }
  </style>"""

# ================= LOOKER THEME =================
css_looker = """<style>
    .reveal {
      font-family: 'Inter', 'Google Sans', sans-serif;
      font-size: 24px;
      color: #202124;
      background-color: #f8f9fa;
    }

    .reveal h1,
    .reveal h2,
    .reveal h3,
    .reveal h4 {
      font-family: 'Inter', 'Google Sans', sans-serif;
      font-weight: 600;
      color: #202124;
      margin-bottom: 24px;
      letter-spacing: -0.01em;
    }

    .reveal h1 {
      font-size: 2.3em;
      text-align: left;
      line-height: 1.2;
      color: #1a73e8;
    }

    .reveal h2 {
      font-size: 1.5em;
      text-align: left;
      border-bottom: 2px solid #e8eaed;
      padding-bottom: 12px;
      display: inline-block;
      margin-bottom: 35px;
      color: #202124;
    }

    .reveal h3 {
      font-size: 1.15em;
      text-align: left;
      color: #3c4043;
      font-weight: 600;
    }

    .reveal p {
      font-size: 1em;
      line-height: 1.6;
      text-align: left;
      font-weight: 400;
      color: #3c4043;
    }

    .reveal ul {
      display: block;
      text-align: left;
      font-weight: 400;
      font-size: 0.95em;
      color: #3c4043;
      padding-left: 20px;
    }

    .reveal li {
      margin-bottom: 14px;
    }

    .reveal strong {
      font-weight: 600;
      color: #202124;
    }

    .highlight-green {
      color: #137333;
      font-weight: 600;
    }

    .highlight-blue {
      color: #1a73e8;
      font-weight: 600;
    }

    .highlight-purple {
      color: #9334e6;
      font-weight: 600;
    }

    .serif-quote {
      font-family: 'Inter', sans-serif;
      font-size: 1.1em;
      font-style: normal;
      color: #1a73e8;
      background: #e8f0fe;
      border-left: 4px solid #1a73e8;
      padding: 16px 24px;
      margin: 30px 0;
      text-align: left;
      line-height: 1.5;
      border-radius: 0 8px 8px 0;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 30px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 20px;
    }

    /* Card Styling */
    .card {
      background: #ffffff;
      padding: 24px;
      border-radius: 8px;
      border: 1px solid #dadce0;
      border-top: 4px solid #dadce0;
      text-align: left;
      box-shadow: 0 1px 3px rgba(60,64,67,0.1), 0 1px 2px rgba(60,64,67,0.06);
      font-size: 0.85em;
      transition: box-shadow 0.2s, transform 0.2s;
    }
    
    .card:hover {
      box-shadow: 0 4px 6px rgba(60,64,67,0.1), 0 2px 4px rgba(60,64,67,0.06);
      transform: translateY(-2px);
    }

    .card-claude {
      border-top-color: #34A853;
    }

    .card-gemini {
      border-top-color: #1A73E8;
    }

    .card-anti {
      border-top-color: #A142F4;
    }

    /* Table Styling */
    .reveal table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 0.7em;
      margin-top: 20px;
      box-shadow: 0 1px 2px rgba(60,64,67,0.1);
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #dadce0;
    }

    .reveal th,
    .reveal td {
      border-bottom: 1px solid #dadce0;
      padding: 16px;
      text-align: left;
      line-height: 1.4;
      background: #fff;
    }

    .reveal th {
      font-weight: 600;
      color: #5f6368;
      background-color: #f1f3f4;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-size: 0.9em;
    }
    
    .reveal tr:last-child td {
      border-bottom: none;
    }

    /* Navigation Buttons on Cover */
    .nav-menu {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 40px;
      justify-content: flex-start;
    }

    .nav-btn {
      padding: 10px 20px;
      border: 1px solid #dadce0;
      background: #ffffff;
      color: #1a73e8;
      font-family: 'Inter', sans-serif;
      font-weight: 500;
      font-size: 0.6em;
      text-transform: none;
      letter-spacing: 0;
      cursor: pointer;
      border-radius: 20px;
      transition: all 0.2s ease;
      text-decoration: none !important;
      box-shadow: 0 1px 2px rgba(60,64,67,0.06);
    }

    .nav-btn:hover {
      background: #f8fbfd;
      color: #174ea6;
      border-color: #d2e3fc;
      transform: translateY(-1px);
      box-shadow: 0 1px 3px rgba(60,64,67,0.1);
    }

    .nav-btn:active {
      background: #e8f0fe;
      transform: translateY(0);
    }

    /* Terminal/Code Example Style */
    .terminal-box {
      background: #f8f9fa;
      color: #202124;
      padding: 16px;
      border-radius: 6px;
      font-family: 'Roboto Mono', 'Courier New', monospace;
      font-size: 0.65em;
      line-height: 1.5;
      margin-top: 15px;
      border: 1px solid #dadce0;
      box-shadow: none;
      border-top: 1px solid #dadce0;
    }
    
    .terminal-box::before {
      display: none;
    }

    .terminal-prompt {
      color: #137333;
    }

    .terminal-cmd {
      color: #1a73e8;
      font-weight: 600;
    }

    .terminal-output {
      color: #5f6368;
    }

    .subtitle {
      font-size: 0.65em;
      color: #5f6368;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 20px;
      display: block;
      text-align: left;
      font-weight: 600;
    }

    .text-sm {
      font-size: 0.75em !important;
      line-height: 1.6;
      color: #3c4043;
    }

    .badge {
      display: inline-block;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.75em;
      font-weight: 600;
      color: white;
      letter-spacing: 0;
      margin-right: 10px;
    }

    .bg-green {
      background-color: #137333;
    }

    .bg-blue {
      background-color: #1a73e8;
    }

    .bg-purple {
      background-color: #9334e6;
    }

    .reveal-viewport {
      background: #f8f9fa;
    }

    /* Global Home Button */
    .home-btn {
      position: fixed;
      top: 40px;
      right: 50px;
      z-index: 9999;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 14px;
      letter-spacing: 1px;
      color: #1a73e8;
      text-decoration: none;
      text-transform: none;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s ease;
      padding: 8px 16px;
      border-radius: 20px;
      background: #ffffff;
      border: 1px solid #dadce0;
      box-shadow: 0 1px 2px rgba(60,64,67,0.1);
    }

    .home-btn:hover {
      opacity: 1 !important;
      background: #f8fbfd;
      border-color: #d2e3fc;
      transform: translateY(-2px);
    }

    .home-btn:active {
      background: #e8f0fe;
    }
  </style>"""

astro_html = re.sub(r"<style>.*?</style>", css_astronaut, html_content, flags=re.DOTALL)
looker_html = re.sub(r"<style>.*?</style>", css_looker, html_content, flags=re.DOTALL)

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(astro_html)

with open(looker_path, "w", encoding="utf-8") as f:
    f.write(looker_html)
