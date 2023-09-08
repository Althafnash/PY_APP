def opener():
    import cv2 as cv 

    Name = input("Your name : ")

    Image_path = input("Enter image path : ")

    img = cv.imread(f"{Image_path}")

    cv.imshow(f"{Name} image window",img)

    cv.waitKey(0)