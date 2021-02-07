
import subprocess
import os
import re
import unicodedata

USER_NAMESPACE="YOUR_USERNAME_HERE"

def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')



'''
git init
git add .
git commit -m "Auto Publish"
git push –-set-upstream git@gitlab.example.com:namespace/nonexistent-project.git master
'''

if os.path.exists(os.path.join(os.getcwd(),'.git')):
    print("ERROR: Git repo already exits")
    exit(0)
current_folder_name=os.path.basename(os.getcwd())
current_folder_name=slugify(current_folder_name)


subprocess.run('git init -b main')
subprocess.run('git add .')
subprocess.run('git commit -m "Auto Publish"')
cmd='git push --set-upstream git@gitlab.com:'+USER_NAMESPACE+'/'+current_folder_name+'.git main'
subprocess.run(cmd)
print("SUCCESS!")



