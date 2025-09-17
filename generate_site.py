import os
from jinja2 import Environment, FileSystemLoader
import markdown

# Jinja2 setup
env = Environment(loader=FileSystemLoader('templates'))

pages = [
    {"template": "index.html", "output": "dist/index.html"},
    {"template": "publications.html", "output": "dist/publications.html"},
    {"template": "patents.html", "output": "dist/patents.html"},
    {"template": "awards.html", "output": "dist/awards.html"},
    {"template": "personal.html", "output": "dist/personal.html"},
    {"template": "activities.html", "output": "dist/activities.html"},
    # Remove any .md links from this list
]

output_dir = 'dist'
os.makedirs(output_dir, exist_ok=True)

for page in pages:
    template = env.get_template(page['template'])
    output = template.render()
    with open(page['output'], 'w', encoding='utf-8') as f:
        f.write(output)

# Copy static folder
import shutil
shutil.copytree('static', os.path.join(output_dir, 'static'), dirs_exist_ok=True)
shutil.copytree('images', os.path.join(output_dir, 'images'), dirs_exist_ok=True)
print("✅ Website generated in 'dist/' folder!")
