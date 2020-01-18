import os
import fnmatch
import ffmpeg
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--src", dest="src", action="store", help="source dir", default="./")
parser.add_option("-d", "--dest", dest="dest", action="store", help="destination dir", default="./audio")
parser.add_option("-v", "--video-type", dest="videoType", action="store", help="input video type", default="mp4")
parser.add_option("-a", "--audio-type", dest="audioType", action="store", help="output audio type", default="wav")


def filter_file(path, file_ext):
    flist = os.listdir(path)
    all_file = []
    for filename in flist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            all_file.extend(filter_file(filepath, file_ext))
        elif fnmatch.fnmatch(filepath, '*.' + file_ext):
            all_file.append(filepath)
        else:
            pass
    return all_file


if __name__ == '__main__':
    (options, args) = parser.parse_args()
    src = options.src
    dest = options.dest
    videoType = options.videoType
    audioType = options.audioType
    all_file = filter_file(src, videoType)
    if not os.path.exists(dest):
        os.mkdir(dest)
    for f in all_file:
        vFilename = os.path.split(f)[-1]
        aFilename = vFilename.split('.')[0] + '.' + audioType
        vFullFilename = os.path.join(src, vFilename)
        aFullFilename = os.path.join(dest, aFilename)
        if os.path.exists(aFullFilename):
            continue
        else:
            try:
                print("Start converting {0}".format(vFilename))
                (ffmpeg.input(vFullFilename)
                 .output(aFullFilename, **{'vn': None, 'f': audioType})
                 .run())
                print("Finish conversion of {0}".format(aFilename))
            except Exception as e:
                print('Exception: {}'.format(e))
