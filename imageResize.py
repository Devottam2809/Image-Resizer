import cv2          # importing cv2 module


source_image = "maxresdefault.jpg"
destintion_image = "final_image.jpg"
scale_percent = 50                  # percentage to be reduced

src = cv2.imread(source_image,cv2.IMREAD_UNCHANGED)      # read the imput image

width = int(src.shape[1]*scale_percent/100)         # height of final image
height = int(src.shape[0]*scale_percent/100)        # width of final image

dsize = (width,height)                              # final size tuple

output = cv2.resize(src,dsize)                      # resize source image
cv2.imwrite(destintion_image,output)               # save image

# cv2.waitKey(0)


# cv2.imshow("title",src)           # show the iamge