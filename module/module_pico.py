import os
import subprocess

# Define path
file_path = os.path.abspath(__file__)
speech_wave = file_path.replace(
            'module/module_pico.py', 'beep/speech.wav')
beep_wave = file_path.replace(
            'module/module_pico.py', 'beep/stop.wav')
# Speak content
def speak(content):

    ###############
    #
    # use this module to speak param
    #
    # param >> content: speak this content
    #
    # return >> None
    #
    ###############


    subprocess.call('aplay -q --quiet {}'.format(beep_wave), shell=True)

    print("[*] SPEAK : {0}".format(content),flush=True)
    content = content.replace("ri-one","reon").replace("Ri-one","reon")
    subprocess.call('amixer sset Master 65% -q --quiet', shell=True)  # 大声
    subprocess.call(['pico2wave', '-w={}'.format(speech_wave), content])
    subprocess.call('aplay -q --quiet {}'.format(speech_wave), shell=True)
    #subprocess.call('amixer sset Master 30% -q --quiet', shell=True)  # 声の大きさを戻す

if __name__ == '__main__':
    speak("the bear cub was named winnipeg. it inspired the stories of winnie-the-pooh")
