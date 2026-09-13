Set-Content -Path "export_data.py" -Value @"
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'furniture_project.settings')
django.setup()

from django.core.management import call_command

with open('datadump.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'store', 'auth.user', indent=4, stdout=f)

print('Done exporting to UTF-8!')
"@