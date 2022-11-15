import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PIL import Image
		
#========================================================================================================
# Setup:


ROTATION_ANGLE = -90    # in degrees


#========================================================================================================


class Img_rot(QWidget):


    def __init__(self, rotation_angle):
        super().__init__()
        self.work(rotation_angle)
        input('Press Enter to exit:')
        sys.exit()
        

    def work(self, rotation_angle):
        try:
            source_images_folder = str(QFileDialog.getExistingDirectory(self, "Select source images folder:"))
            print(source_images_folder)
            result_images_folder = str(QFileDialog.getExistingDirectory(self, "Select result images folder:"))
            print(result_images_folder)
            img_file_names = [f for f in os.listdir(source_images_folder) if os.path.isfile(os.path.join(source_images_folder, f)) and (os.path.splitext(f)[1].upper() == '.JPG' or os.path.splitext(f)[1].upper() == '.JPEG')]
            for img_file_name in img_file_names:
                print(img_file_name)
                img = Image.open(os.path.join(source_images_folder, img_file_name))
                img = img.rotate(rotation_angle, resample=0, expand=1)
                img.save(os.path.join(result_images_folder, img_file_name), "JPEG")
        except Exception as e:
            print('work Exception: ' + str(e))        


#========================================================================================================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    img_rot = Img_rot(ROTATION_ANGLE)
    sys.exit(app.exec_())




