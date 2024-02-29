import os
import girder_client
from ctk_cli import CLIArgumentParser

def main(args2):
    base_dir_id = args2.inputFolder.split('/')[-2]

    gc = girder_client.GirderClient(apiUrl=args2.girderApiUrl)
    gc.setToken(args2.girderToken)
    files = list(gc.listItem(base_dir_id))

    for file in files:
        print(file)

    cwd = os.getcwd()
    print(cwd)
    os.chdir(cwd)

    print(args2.inputImageFile)
    print(args2.Model)
    print(args2.outputFolder)
    print(args2.inputFolder)
    print(args2.resize)
    print(args2.batchsize)
    print(args2.patchsize)

    cmd = f"python3 ../kidneyhistologicprimitives/make_output_unet_cmd.py {args2.inputImageFile} \
        --model {args2.Model}\
        --outdir {args2.outputFolder}\
        --basepath {args2.inputFolder}\
        --resize {args2.resize} \
        --batchsize {args2.batchsize} \
        --patchsize {args2.patchsize} \
        --force"
    
    os.system(cmd)    


if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())
