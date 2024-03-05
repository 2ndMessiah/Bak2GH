import subprocess

# 定义需要压缩的目录和输出文件的名称
input_dir = "/mnt/mmcblk2p4"
output_file = "/mnt/mmcblk2p4/bak/root.tar.gz"
backup_dir = "/mnt/mmcblk2p4/bak/313bak" #backup repo name
excepList="/mnt/mmcblk2p4/bak/exception.txt"

# 清理.git/objects
cleanup_command = f"cd {backup_dir} && git pull"
cleanup_process = subprocess.Popen(cleanup_command, shell=True)
cleanup_process.wait()

# 确保命令成功执行
if cleanup_process.returncode != 0:
    print(f"cleanup message: \n {cleanup_process.returncode}")
    # exit(1)




# 使用tar命令创建压缩文件
tar_command = f"tar -czf {output_file} -X {excepList} {input_dir}"
tar_process = subprocess.Popen(tar_command, shell=True)
tar_process.wait()

# 确保tar命令成功执行
if tar_process.returncode != 0:
    print(f"tar command failed with exit code {tar_process.returncode}")
    exit(1)

# 使用split命令将压缩文件分割成小于100MB的分卷
# 这里的100MB是通过计算得出的，1MB = 1024*1024 bytes
split_command = f"split -b 95000000 {output_file} {output_file}.part"
split_process = subprocess.Popen(split_command, shell=True)
split_process.wait()

# 确保split命令成功执行
if split_process.returncode != 0:
    print(f"split command failed with exit code {split_process.returncode}")
    exit(1)

# 清空备份目录
rm_command = f"rm -rf {backup_dir}/* && rm {output_file}"
rm_process = subprocess.Popen(rm_command, shell=True)
rm_process.wait()

# 确保rm命令成功执行
if rm_process.returncode != 0:
    print(f"rm command failed with exit code {rm_process.returncode}")
    exit(1)

# 移动分割后的文件到备份目录
mv_command = f"mv {output_file}.part* {backup_dir} && crontab -l > {backup_dir}/crontab.bak"
mv_process = subprocess.Popen(mv_command, shell=True)
mv_process.wait()

# 确保mv命令成功执行
if mv_process.returncode != 0:
    print(f"mv command failed with exit code {mv_process.returncode}")
    exit(1)

print("Compression, split, clear directory, and move completed successfully.")


gitcmd0=f"git checkout --orphan backtemp && \
        git add -A && \
        git commit -am 'bak' && \
        git branch -D master && \
        git branch -m master && \
        git push -f origin master && \
        rm -rf {backup_dir}/.git/objects/* && \
        rm {backup_dir}/*"
git_process = subprocess.Popen(gitcmd0,shell=True,cwd=backup_dir)
git_process.wait()

if mv_process.returncode != 0:
    print(f"git command failed with exit code {git_process.returncode}")
    exit(1)
