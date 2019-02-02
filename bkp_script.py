from pathlib import PurePath
from shutil import copytree, ignore_patterns

# Path to the volume to drop all of the backups into
bkp_root_path = PurePath(r'/Volumes/Offsite External HD') 

# Path to the list of directories to backup
list_file_path = bkp_root_path / 'bkp_list_of_directories.txt'

# The list of directories to backup
list_dir_to_backup = []

with open(list_file_path) as file:
	# Add the pure path of each line entry in the list_file to the list of directories to backup
	[list_dir_to_backup.append(PurePath(line.rstrip())) for line in file]

for directory_path in list_dir_to_backup:
	# Get just the directory name from the list of directories to backup and define a new directory in the backup location with the same name
	new_backup_directory_path = str(bkp_root_path / directory_path.name)
	
	copytree(str(directory_path), new_backup_directory_path, symlinks=True)#, ignore=ignore_patterns('*.pyc'))
	print('%s copied...' % directory_path)