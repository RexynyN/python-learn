# from skimage.metrics import structural_similarity
# import cv2

# #Works well with images of different dimensions
# def orb_sim(img1, img2):
#   # SIFT is no longer available in cv2 so using ORB
#   orb = cv2.ORB_create()

#   # detect keypoints and descriptors
#   kp_a, desc_a = orb.detectAndCompute(img1, None)
#   kp_b, desc_b = orb.detectAndCompute(img2, None)

#   # define the bruteforce matcher object
#   bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
#   #perform matches. 
#   matches = bf.match(desc_a, desc_b)
#   #Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
#   similar_regions = [i for i in matches if i.distance < 50]  
#   if len(matches) == 0:
#     return 0
#   return len(similar_regions) / len(matches)


# #Needs images to be same dimensions
# def structural_sim(img1, img2):
#   sim, diff = structural_similarity(img1, img2, full=True)
#   return sim

# img00 = cv2.imread('igor.jpg', 0)
# img01 = cv2.imread('igor4.png', 0)


# # img1 = cv2.imread('images/BSE.jpg', 0)  # 714 x 901 pixels
# # img2 = cv2.imread('images/BSE_noisy.jpg', 0)  # 714 x 901 pixels
# # img3 = cv2.imread('images/BSE_smoothed.jpg', 0)  # 203 x 256 pixels
# # img4 = cv2.imread('images/different_img.jpg', 0)  # 203 x 256 pixels

# orb_similarity = orb_sim(img00, img01)  #1.0 means identical. Lower = not similar

# print("Similarity using ORB is: ", orb_similarity)

import cv2

class CompareImage(object):
    def __init__(self, image_1_path, image_2_path):
        self.minimum_commutative_image_diff = 1
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path

    def compare_image(self):
        image_1 = cv2.imread(self.image_1_path, 0)
        image_2 = cv2.imread(self.image_2_path, 0)
        commutative_image_diff = self.get_image_difference(image_1, image_2)

        if commutative_image_diff < self.minimum_commutative_image_diff:
            print ("Matched")
            return commutative_image_diff

        return -1 # random failure value

    @staticmethod
    def get_image_difference(image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
        img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff


if __name__ == '__main__':
    compare_image = CompareImage('notebooks/bingus.jpg', 'notebooks/floppa.jpg')
    image_difference = compare_image.compare_image()
    print(image_difference)
    print(CompareImage.get_image_difference('notebooks/bingus.jpg', 'notebooks/floppa.jpg'))