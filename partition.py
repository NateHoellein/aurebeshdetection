import os
import shutil
from sklearn.model_selection import train_test_split

images = [os.path.join('images', x) for x in os.listdir('images')]
labels = [os.path.join('labels', x) for x in os.listdir('labels')]

print(len(images))
print(len(labels))

if ('images/test' in images or 'images/train' in images or 'images/validate' in
    images or 'images/.DS_Store' in images):
    print('diretories in list to sort')
    images.remove('images/test')
    images.remove('images/train')
    images.remove('images/validate')
    images.remove('images/.DS_Store')

if ('labels/test' in labels or 'labels/train' in labels or 'labels/validate' in
    labels or 'labels/.DS_Store' in labels):
    print('diretories in list to sort')
    labels.remove('labels/test')
    labels.remove('labels/train')
    labels.remove('labels/validate')
    labels.remove('labels/.DS_Store')

if ('images/test' in images or 'images/train' in images or 'images/validate' in
    images or 'images/.DS_Store' in images):
    print('diretories in images list')
    assert False

if ('labels/test' in labels or 'labels/train' in labels or 'labels/validate' in
    labels or 'labels/.DS_Store' in labels):
    print('diretories in labels list')
    assert False

images.sort()
labels.sort()

train_images, validate_images, train_labels, validate_labels = train_test_split(images,
                                                                                 labels,
                                                                                 test_size = 0.2,
                                                                                 random_state = 1)

validate_images, test_images, validate_labels, test_labels = train_test_split(validate_images,
                                                                                 validate_labels,
                                                                                 test_size = 0.5,
                                                                                 random_state = 1)

print("train shape: {0}".format(len(train_images)))
print("test shape: {0}".format(len(test_images)))
print("validate shape: {0}".format(len(validate_images)))
print("train lables shape: {0}".format(len(train_labels)))
print("test labels  shape: {0}".format(len(test_labels)))
print("validate labels shape: {0}".format(len(validate_labels)))

#for b in (background for background in backgrounds
#          if os.path.isfile(background)):

def move_files_to_folder(list_of_files, destination_folder):
    for f in (myfile for myfile in list_of_files
              if os.path.isfile(myfile)):
        try:
            print("Moving {0} to {1}".format(f, destination_folder))
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False

move_files_to_folder(train_images, 'images/train')
move_files_to_folder(validate_images, 'images/validate/')
move_files_to_folder(test_images, 'images/test/')
move_files_to_folder(train_labels, 'labels/train/')
move_files_to_folder(validate_labels, 'labels/validate/')
move_files_to_folder(test_labels, 'labels/test/')
