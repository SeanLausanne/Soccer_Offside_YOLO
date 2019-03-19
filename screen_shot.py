import subprocess
import os


path = os.getcwd() + '/screen_shots_PS4/'
def get_shots():
    # try:
    #     for root, dirs, files in os.walk(path):
    #         for name in files:
    #             if name.endswith(".jpg"):
    #                 os.remove(os.path.join(root, name))
    # except FileNotFoundError:
    #     pass


    for j in range(720,840,2):
        subprocess.run(['ffmpeg','-i','FIFA19_PS4.mp4','-ss',str(j),'-vframes','1','-r','1','-ac','1','-ab','2','-s','1200*800','-f','image2',path+str(j)+'.jpg'])

def rename_images():
    i = 0
    imgs = os.listdir(path)
    for filename in imgs:
        i += 1
        os.rename(path + filename, path + 'FIFA' + str(i).zfill(3) + '.jpg')



def main():
    #get_shots()
    rename_images()


if __name__ == '__main__':
    main()
