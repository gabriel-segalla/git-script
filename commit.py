import git
import sys
import subprocess

repo = git.Repo('./')
g = git.cmd.Git('./')

print("Executando Formatação...")
try:     
    subprocess.check_call('npm run format', shell=True)
except:
    print("NÃO CONSEGUIU FORMATAR")
    
print("GIT ADD .")
subprocess.check_call('git add .', shell=True)

#add_all_files = input("Deseja Adicionar todos os arquivos no commit? (Y/n)")
#if(add_all_files.upper() == 'Y'): 
#    subprocess.check_call('git add .', shell=True)
#elif(add_all_files.lower() == 'n'):
#    
#    files = []
#    for file_id ,untracked_file in enumerate(repo.untracked_files, start=1):
#        my_file = {}
#        my_file['id'] = file_id
#        my_file['file']= untracked_file
#        files.append(my_file)
#
#    print("Choose the files to add in commit")
#    for file in files:
#        print('[{}] - {}'.format(file.get('id'),file.get('file')))
#    selected_files = list(map(int, input("Enter a multiple value: ").split())) 
#    for file in files:
#        if file.get('id') in selected_files:
#            g.add(file.get('file'))

print("GIT COMMIT...") 
if('commit.py' in sys.argv):
    sys.argv = sys.argv[1: len(sys.argv)] 
listToStr = ' '.join([str(elem) for elem in sys.argv]) 
message = '[{}] - {}'.format(repo.active_branch.name, listToStr)
index = repo.index
index.commit(message)

print("GIT PUSH...")
g.push()
