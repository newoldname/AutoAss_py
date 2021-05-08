import cv2

video_path = "a.mp4"
msfile = open("mstime.txt", "r")
msarr = msfile.readlines()
vc = cv2.VideoCapture(video_path)  # 读取视频
a = "photo\\"
count = 0
for i in range(len(msarr)):
    mstr = msarr[i]
    ms = int(mstr.strip())
    vc.set(cv2.CAP_PROP_POS_MSEC, ms + 800)  # 设置读取位置，1000毫秒
    rval, frame = vc.read()  # 读取当前帧，rval用于判断读取是否成功
    if rval:
        cover_path = a + str(ms) + ".jpg"
        print(cover_path)
        cv2.imwrite(cover_path, frame)  # 将当前帧作为图片保存到 cover_path
    else:
        print("读取失败")

#
