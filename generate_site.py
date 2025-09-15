import os
from jinja2 import Environment, FileSystemLoader
import markdown

# Jinja2 setup
env = Environment(loader=FileSystemLoader('templates'))

pages = [
    {'template': 'index.html', 'output': 'index.html'},
    {'template': 'publications.html', 'output': 'publications.html', 'content_file': 'content/publications.md'},
    {'template': 'patents.html', 'output': 'patents.html', 'content_file': 'content/patents.md'},
    {'template': 'awards.html', 'output': 'awards.html', 'content_file': 'content/awards.md'},
]

output_dir = 'dist'
os.makedirs(output_dir, exist_ok=True)

for page in pages:
    template = env.get_template(page['template'])
    content_html = ''
    if 'content_file' in page:
        with open(page['content_file'], 'r', encoding='utf-8') as f:
            content_html = markdown.markdown(f.read())
    rendered = template.render(content=content_html)
    with open(os.path.join(output_dir, page['output']), 'w', encoding='utf-8') as f:
        f.write(rendered)

# Copy static folder
import shutil
shutil.copytree('static', os.path.join(output_dir, 'static'), dirs_exist_ok=True)
shutil.copytree('images', os.path.join(output_dir, 'images'), dirs_exist_ok=True)
print("✅ Website generated in 'dist/' folder!")
