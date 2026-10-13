# -*- coding: utf-8 -*-
"""
Football Tactics Hub - Compiler & Asset Orchestrator
Data-Driven Modern Compiler:
1. Single Source of Truth: data/tactics_data.json
2. Automatic UMD synchronization: data/tactics_data.js (Browser, Node.js, WeChat Mini Program)
3. Dual-Mode Output:
   - Lightweight Web Mode (Default): football_tactics_hub.html & index.html (~70KB)
   - Standalone Bundle Mode (--standalone): football_tactics_hub_standalone.html with Base64 inlining
"""

import os
import sys
import json
import base64
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
data_json_path = os.path.join(base_dir, "data", "tactics_data.json")
data_js_path = os.path.join(base_dir, "data", "tactics_data.js")
gif_dir = os.path.join(base_dir, "tactics_animations_gif")

def load_data():
    if not os.path.exists(data_json_path):
        raise FileNotFoundError(f"Missing data source: {data_json_path}")
    with open(data_json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def sync_js_from_json(data):
    js_content = f"""/**
 * Football Tactics Hub - Core Tactics Data Store
 * Cross-platform data source for Standalone Web, Mobile Viewports, and WeChat Mini Programs.
 */
(function(global) {{
  const tacticsData = {json.dumps(data, ensure_ascii=False, indent=2)};

  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = tacticsData;
  }}
  if (typeof window !== 'undefined') {{
    window.TACTICS_DATA = tacticsData;
  }} else {{
    global.TACTICS_DATA = tacticsData;
  }}
}})(typeof window !== 'undefined' ? window : this);
"""
    with open(data_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Synced {data_js_path} successfully.")

def get_base64_gif(relative_path):
    full_path = os.path.join(base_dir, relative_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            return "data:image/gif;base64," + base64.b64encode(f.read()).decode("ascii")
    return relative_path

def build_standalone(data):
    """Generate standalone offline single-file HTML with Base64 assets embedded"""
    print("Building Standalone Single-File Bundle with Base64 assets...")
    data_copy = json.loads(json.dumps(data))
    
    # Invert GIF paths to Base64
    for doc in data_copy.get("doctrines", []):
        if "gif" in doc:
            doc["gif"] = get_base64_gif(doc["gif"])
            
    for cat_id, w_list in data_copy.get("weapons", {}).items():
        for w in w_list:
            if "gif" in w:
                w["gif"] = get_base64_gif(w["gif"])
                
    if "combo" in data_copy and "gif" in data_copy["combo"]:
        data_copy["combo"]["gif"] = get_base64_gif(data_copy["combo"]["gif"])
        
    for f_id, form in data_copy.get("formations", {}).items():
        if "animGif" in form:
            form["animGif"] = get_base64_gif(form["animGif"])
            
    # Read template HTML
    template_path = os.path.join(base_dir, "football_tactics_hub.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    # Replace external script with inlined TACTICS_DATA
    script_tag = '<script src="data/tactics_data.js"></script>'
    inlined_script = f'<script>window.TACTICS_DATA = {json.dumps(data_copy, ensure_ascii=False)};</script>'
    standalone_html = html.replace(script_tag, inlined_script)
    
    out_standalone = os.path.join(base_dir, "football_tactics_hub_standalone.html")
    with open(out_standalone, "w", encoding="utf-8") as f:
        f.write(standalone_html)
    print(f"Generated standalone bundle: {out_standalone} ({len(standalone_html)/(1024*1024):.2f} MB)")

def main():
    standalone = "--standalone" in sys.argv
    data = load_data()
    sync_js_from_json(data)
    
    hub_html_path = os.path.join(base_dir, "football_tactics_hub.html")
    index_html_path = os.path.join(base_dir, "index.html")
    
    if os.path.exists(hub_html_path):
        size_kb = os.path.getsize(hub_html_path) / 1024
        print(f"Lightweight Hub Web: {hub_html_path} ({size_kb:.1f} KB)")
        shutil.copy2(hub_html_path, index_html_path)
        print(f"Mirrored to: {index_html_path}")
        
    if standalone:
        build_standalone(data)

if __name__ == "__main__":
    main()
