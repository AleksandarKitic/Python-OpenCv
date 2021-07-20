import cv2
import tkinter as tk
import time


# OPENING CAMERA
class openCamera:
    def openCamera1(self):
        cam = cv2.VideoCapture(0)
        img_counter = 0

        if not cam.isOpened():
            print('Can not open the camera!')
            exit()

        while True:
            # CAPTURE FRAME BY FRAME
            ret, frame = cam.read()

            # OUR OPERATION FOR FRAME COME HERE
            color_cam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # IF FRAME IS READ CORRECTLY RET IS TRUE
            if not ret:
                print('Can not streaming the frame. Exiting..')
                break

            if cv2.waitKey(1) == ord('q'):
                # Q pressed
                break

            if cv2.waitKey(1) == ord('a'):
                # A pressed
                img_name = "UserImg_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                a = mainProgram()
                return a.mainProgram1()

            # DISPLAY THE RESULT OF FRAME
            cv2.imshow('frame', color_cam)

        cam.release()
        cv2.destroyAllWindows()


# SOFTWARE FOR REGISTRATION
class mainProgram:
    def mainProgram1(self):
        root = tk.Tk()
        root.title('Unlock Door')
        root.geometry('600x400')

        tk.Label(root, text='Full Name:').grid(row=0)
        tk.Label(root, text='Email:').grid(row=1)
        tk.Label(root, text='ID:').grid(row=2)

        fullName = tk.Entry(root)
        email = tk.Entry(root)
        id = tk.Entry(root)

        fullName.grid(row=0, column=1)
        email.grid(row=1, column=1)
        id.grid(row=2, column=1)

        def sendUserInfo():
            print('Processing..')
            time.sleep(5)
            name = fullName.get()
            email1 = email.get()
            userId = id.get()

            print('Processing is DONE!')
            print('-' * 30)
            print(f'Your name: {name}')
            print(f'Your email: {email1}')
            print(f'Your personal ID: {userId}')
            img = cv2.imread('UserImg_0.png')
            cv2.imshow('User1', img)

        tk.Button(root, text='Submit', fg='red', command=sendUserInfo).grid(row=4, column=1, sticky=tk.W, pady=4)

        root.mainloop()


a = openCamera()
a.openCamera1()
