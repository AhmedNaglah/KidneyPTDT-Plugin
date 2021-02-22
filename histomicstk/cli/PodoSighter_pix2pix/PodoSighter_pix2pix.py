import os
from histomicstk.cli.utils import CLIArgumentParser

def main(args2):         
    
    cmd = "python3 ../PodoSighter_pix2pix_folder/Complete_Pix2pix_Prediction.py -A0 '{}' -A1 '{}' -A2 '{}' -A3 '{}' -A4 '{}' -A5 '{}' -A6 {} -A7 {} -A8 {} -A9 '{}' -A10 '{}'".format(args2.inputFolder, args2.inputImageFile,args2.inputAnnotationFile1, args2.TrainedGeneratorModel ,args2.TrainedDiscriminatorModel,args2.outputAnnotationFile1, args2.PASnucleiThreshold,args2.gauss_filt_size, args2.Disc_size ,args2.species,args2.stain)

    os.system(cmd)    

if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())