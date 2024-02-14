# A Linux Backup Script for Personal Use

Utilizing a Git repository as the backup destination is recommended, and you may consider using GitHub as well.

Considering the potential growth of the `.git` folder, this script will only retain the latest commit.

Please pay attention to the following points:

1. The backup repository should be located at `/home/$backup_dir`.
    1. Ensure that the `backup_dir` variable in the script corresponds to the actual directory, without appending a "/" at the end.
    2. Prior to running the script, configure the necessary information for the `backup_dir` Git repository, including user, email, and login credentials.
2. The default branch for the repository should be named "master". 
3. Modify the `input_dir` variable in the script according to your requirements, indicating the folder that needs to be backed up.
4. The `outputfile` variable refers to the resulting tarball backup file.
    1. To overcome GitHub's 100MB file size restriction, the resulting tarball will be split into chunks of approximately 90MB each before uploading.
5. If your system's got a very terrible network so that git push fails, try: git config --global http.postBuffer 524288000

