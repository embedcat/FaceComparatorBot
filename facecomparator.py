import dlib
from skimage import io
import const
from scipy.spatial import distance


class FaceCompare:
    sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()

    def get_face_descriptor(self, file):
        img = io.imread(str(file))
        detections = self.detector(img, 1)
        if len(detections) > 0:
            d = detections[0]
            shape = self.sp(img, d)
            dlib.save_face_chip(img, shape, str(file)[:-4] + const.file_with_face_suffix)
            return self.facerec.compute_face_descriptor(img, shape)

    def compare(self, file1, file2):
        result = {'distance': None,
                  'error': None,
                  'file1': None,
                  'file2': None}

        fd1 = self.get_face_descriptor(file1)
        fd2 = self.get_face_descriptor(file2)
#        print(" >In compare()", "Calc distance")
        result.update(error=1 if fd1 is None else 2 if fd2 is None else None)
        if fd1 and fd2:
            dist = distance.euclidean(fd1, fd2)
            result.update(distance=dist,
                          file1=str(file1)[:-4] + const.file_with_face_suffix,
                          file2=str(file2)[:-4] + const.file_with_face_suffix)
        return result
