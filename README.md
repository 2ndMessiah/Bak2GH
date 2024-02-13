# 一个自用Linux备份脚本

依托git repo当备份目的地，当然你也可以用github。

考虑到.git可能会越变越大，所以本脚本只保留最新的一个commit。

注意几点：

1. 备份的repo放在/home/$backup_dir
    1. 和脚本中的backup_dir这个变量对应起来，结尾不加”/”。
    2. 要先把backup_dir这个git repo的相关信息配置好，包括user\email\login credentials
2. repo默认的分支应该叫master。其实可以判断一下，放在todo里吧。
3. 根据自己的要求修改脚本中的input_dir,也就是需要备份的文件夹。
4. outputfile变量指的是备份出来的tarball。
    1. 为了规避github的100MB文件大小限制，用split拆分resulted tarball 为 90MB左右再上传。

