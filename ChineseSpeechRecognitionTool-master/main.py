import tensorflow as tf
from flask import Flask, render_template

from LanguageModel2 import ModelLanguage
from SpeechModel251 import ModelSpeech

datapath = 'F:\\语音数据集'
modelpath = 'F:\\Pycharm\\Workspace\\recoder\\model_speech\\'

# sess = tf.Session()
# ms = ModelSpeech(datapath)
# ms.LoadModel(modelpath + 'speech_model251_e_0_step_12000.model')
# r = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00241I0052.wav')
# r_test = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\test.wav')
# r = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\test.wav')
# ml = ModelLanguage('model_language')
# ml.LoadModel()


def func_show(r):
    # r = ms.RecognizeSpeech_FromFile('E:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00241I0052.wav')
    print('*[提示] 语音识别结果：\n', r)
    str_pinyin = r
    r = ml.SpeechToText(str_pinyin)
    print('语音转文字结果：\n', r)
    return r


def func_test(r_test):
    # r_test = ms.RecognizeSpeech_FromFile('E:\\语音数据集\\test.wav')
    print('*[提示] 语音识别结果：\n', r_test)
    str_pinyin = r_test
    r_test = ml.SpeechToText(str_pinyin)
    print('语音转文字结果：\n', r_test)
    return r_test


app = Flask(__name__)


@app.route('/')
def index():
    # rs = func()
    return render_template('show_recoder.html')  # , result=rs)


@app.route('/result/')
def show_result():
    rs = func_show(r)
    return render_template('show_result.html', result=rs)


@app.route('/test/')
def show_test():
    with g.as_default():
        r_test = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\test.wav')
        str_pinyin = r_test
        r_test = ml.SpeechToText(str_pinyin)
        print("testtesttest")
    # rs = func_test(r_test)
    return render_template('show_test.html', result=r_test)
    # return 'ge'


if __name__ == '__main__':
    g = tf.Graph()
    with g.as_default():
        ms = ModelSpeech(datapath)
        ms.LoadModel(modelpath + 'speech_model251_e_0_step_12000.model')
        # r = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\data_thchs30\\test\\D4_750.wav')
        r = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\ST-CMDS-20170001_1-OS\\20170001P00136I0088.wav')
        r_test = ms.RecognizeSpeech_FromFile('F:\\语音数据集\\test.wav')
        ml = ModelLanguage('model_language')
        ml.LoadModel()
    app.run(debug=True);