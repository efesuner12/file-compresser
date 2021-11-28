import tarfile
from tqdm import tqdm # pip3 install tqdm

def compress(tar_file, members):
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()

def decompress(tar_file, path, members=None):
    tar = tarfile.open(tar_file, mode="r:gz")

    if members is None:
        members = tar.getmembers()
    # with progress bar
    # set the progress bar
    progress = tqdm(members)

    for member in progress:
        tar.extract(member, path=path)
        # set the progress description of the progress bar
        progress.set_description(f"Extracting {member.name}")
    # or use this
    # tar.extractall(members=members, path=path)
    # close the file
    tar.close()

if __name__ == "__main__":
    compress("compressed.tar.gz", ["test.txt", "folder"])
    #decompress("compressed.tar.gz", "extracted")
