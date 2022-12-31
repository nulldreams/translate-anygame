img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Bilaterial filter and adaptive histogram thresholding to get background into mostly one patch
img = cv2.bilateralFilter(img, 9, 29, 29)
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 0)

# Add padding to join any background around edges into the same patch 
pad = 2
img_pad = cv2.copyMakeBorder(thresh, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value = 1)

# Label patches and remove padding
ret, markers = cv2.connectedComponents(img_pad)
markers = markers[pad:-pad,pad:-pad]

# Count pixels in each patch
counts = [(markers==i).sum() for i in range(markers.max()+1)]

# Keep patches based on pixel counts
maxCount = 200 # removes large background patches
minCount = 40  # removes specs and centres of numbering
keep = [c<maxCount and c>minCount for c in counts]
output = markers.copy()
for i,k in enumerate(keep):
    output[markers==i] = k