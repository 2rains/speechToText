from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
 
root = Tk()
root.title('filedialog study')
 
def open():
    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
 
    Label(root, text=root.filename).pack() # 파일경로 view
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=my_image).pack() #사진 view
 
 
my_btn = Button(root, text='파일열기', command=open).pack()
 
root.mainloop()




import speech_recognition as sr
sr.__version__
'3.8.1'

r = sr.Recognizer()  # 음성인식 recognizer 인스턴스 생성

harvard = sr.AudioFile('hello.wav')
with harvard as source:
    audio = r.record(source)

type(audio)  # audio data로 타입 변경시킴

r.recognize_google(audio)  # 음성 인식하여 text로 return

with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)
    audio3 = r.record(source, offset=4, duration=3)  # offset, 오디오 시작위치 지정

print(r.recognize_google(audio, language='ko'))

