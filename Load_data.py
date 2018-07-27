def load_data(data_dir):
    directories = [d for d in os.listdir(data_dir) 
                   if os.path.isdir(os.path.join(data_dir, d))]
    labels = []
    images = []
    for d in directories:
        label_dir = os.path.join(data_dir, d)
        file_names = [os.path.join(label_dir, f) 
                      for f in os.listdir(label_dir) if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels
ROOT_PATH = "E:/Traffice signs"
train_data_dir = os.path.join(ROOT_PATH, "Belgium/Training/")
test_data_dir = os.path.join(ROOT_PATH, "Belgium/Testing/")

