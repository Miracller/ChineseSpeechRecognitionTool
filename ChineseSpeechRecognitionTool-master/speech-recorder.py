import wave
from pyaudio import PyAudio,paInt16
from SpeechModel251 import ModelSpeech
from LanguageModel2 import ModelLanguage

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=10
def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*6:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('02.wav',my_buf)
    stream.close()

chunk=1024
def play():
    wf=wave.open(r"02.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data=wf.readframes(chunk)
        if data=="":break
        stream.write(data)
    stream.close()
    p.terminate()


if __name__ == '__main__':
    my_record()
    print('Over!')
    # play()

    ms = ModelSpeech('F:\\Pycharm\\Workspace\\ChineseSpeechRecognitionTool-master')
    ms.LoadModel('model_speech\\' + 'speech_model251_e_0_step_12000.model')
    r = ms.RecognizeSpeech_FromFile('F:\\Pycharm\\Workspace\\ChineseSpeechRecognitionTool-master\\02.wav')
    print('*[提示] 语音识别结果：\n', r)

    ml = ModelLanguage('model_language')
    ml.LoadModel()

    str_pinyin = r
    r = ml.SpeechToText(str_pinyin)
    print('语音转文字结果：\n', r)