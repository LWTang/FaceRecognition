import cv2, dlib, numpy, os


test_img_path = 'tlw.jpg'
predictor_path = 'shape_predictor_68_face_landmarks.dat'
face_rc_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
face_folder_path = 'E:\pyproject\candidate_faces'

detector = dlib.get_frontal_face_detector()
feature_point = dlib.shape_predictor(predictor_path)
feature_model = dlib.face_recognition_model_v1(face_rc_model_path)

descriptors = numpy.load('vectors.npy')
print(type(descriptors))

test_img = cv2.imread(test_img_path)
dets = detector(test_img, 1)
print(type(dets))
for k, d in enumerate(dets):
    shape = feature_point(test_img, d)
    test_feature = feature_model.compute_face_descriptor(test_img, shape)
    test_feature = numpy.array(test_feature)

dist = []
count = 0
name_list = os.listdir(face_folder_path)
for i in descriptors:
    dist_ = numpy.linalg.norm(i-test_feature)
    print('%s : %f' % (name_list[count], dist_))
    dist.append(dist_)
    count += 1

min_dist = numpy.argmin(dist)
print('%s' % name_list[min_dist][:-4])

