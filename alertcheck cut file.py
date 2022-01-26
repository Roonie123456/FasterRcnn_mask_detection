if (distance_from_line <= 0):

    # crossed+=1
    posii = int(image_np.shape[1] / 2)
    cv2.putText(image_np, "ALERT dsads", (posii, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
    # sound = os.path.join()
    playsound("utils\a.wav")
    cv2.rectangle(image_np, (posii - 20, 20), (posii + 85, 60), (255, 0, 0), thickness=3, lineType=8, shift=0)
    # to write into xl-sheet
    return 1
else:
    return 0