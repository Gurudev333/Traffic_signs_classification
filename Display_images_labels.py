def display_label_images(images, label):
    limit = 24  
    plt.figure(figsize=(15, 5))
    i = 1
    start = labels_train.index(label)
    end = start + labels_train.count(label)
    for image in images[start:end][:limit]:
        plt.subplot(3, 8, i)
        plt.axis('off')
        i += 1
        plt.imshow(image)
    plt.show()

