from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ds import *
from os import path
import urllib.request
import urllib.error
from sys import platform
import requests
from threading import Timer
from moviepy.editor import *  # convert video to mp3
import pafy  # YouTube download lib
import humanize  # convert file size from bit to Mb


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.urlErrorMessage = QMessageBox()
        self.empty_url = QMessageBox()
        self.download_Completed = QMessageBox()
        self.DownloadFailed = QMessageBox()
        self.check_internet_connection = QMessageBox()
        self.convert_completed = QMessageBox()
        self.convert_empty_mp4_file = QMessageBox()
        self.setupUi(self)
        self.Ui()
        self.Buttons()
        self.number = 0
        self.convert_number = 0
        self.youtube_video_downloaded = 0
        self.location_place = None
        self.data = None
        self.timer = None
        self.___mp3 = None
        self.___mp4 = None
        self.youtube_playlist_downloaded = 0

    def Ui(self):
        self.setFixedSize(790, 442)
        self.qualityBox_2.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.empty_url.setIcon(QMessageBox.Critical)
        self.empty_url.setWindowTitle("Input Error")
        self.empty_url.setText("url is empty please Enter valid Url ")
        self.empty_url.setInformativeText("Click 'OK' And Try Again")
        self.empty_url.setStandardButtons(QMessageBox.Ok)
        self.urlErrorMessage.setWindowTitle('Url Error')
        self.urlErrorMessage.setText('unveiled Url')
        self.urlErrorMessage.setInformativeText("Click 'ok' And Try Again")
        self.urlErrorMessage.setStandardButtons(QMessageBox.Ok)
        self.urlErrorMessage.setIcon(QMessageBox.Critical)
        self.download_Completed.setWindowTitle("Download Completed")
        self.download_Completed.setIcon(QMessageBox.Information)
        self.download_Completed.setText("Download completed thanks")
        self.download_Completed.setInformativeText("Click 'ok' to Download another file")
        self.download_Completed.setStandardButtons(QMessageBox.Ok)
        self.DownloadFailed.setWindowTitle("error")
        self.DownloadFailed.setIcon(QMessageBox.Warning)
        self.DownloadFailed.setText("Download Failed")
        self.DownloadFailed.setInformativeText("Click 'Ok' And Try Again or another url")
        self.DownloadFailed.setStandardButtons(QMessageBox.Ok)
        self.check_internet_connection.setWindowTitle("Internet Connection Problem")
        self.check_internet_connection.setText("Please check you internet Connection")
        self.check_internet_connection.setInformativeText("Click 'Ok' And Try Agin After Fix You internet Connection")
        self.check_internet_connection.setIcon(QMessageBox.Warning)
        self.check_internet_connection.setStandardButtons(QMessageBox.Ok)
        # self.stopMessage.setWindowTitle("download aborted!")
        # self.stopMessage.setIcon(QMessageBox.Information)
        # self.stopMessage.setText("Download Aborted")
        # self.stopMessage.setStandardButtons(QMessageBox.Ok)
        # self.convert_empty_mp4_file.setWindowTitle("unveiled file")
        self.convert_empty_mp4_file.setText("Please select video file")
        self.convert_empty_mp4_file.setInformativeText("Click 'Ok' And Try Agin After Select Video File")
        self.convert_empty_mp4_file.setIcon(QMessageBox.Critical)
        self.convert_empty_mp4_file.setStandardButtons(QMessageBox.Ok)
        self.convert_completed.setWindowTitle("Convert Completed")
        self.convert_completed.setIcon(QMessageBox.Information)
        self.convert_completed.setStandardButtons(QMessageBox.Ok)


    def Buttons(self):
        # location Browser buttons
        ###############################################################
        self.openFileLocationSaver.clicked.connect(self.save_locations_browser)
        self.openSaveLocation.clicked.connect(self.save_location_browser_youtube)
        self.mp3savelcation.clicked.connect(self.save_location_browser_youtube)
        ######################################################
        # search Button
        ##################################################
        self.search.clicked.connect(self.search_quality)
        ###############################################
        # Download Button
        #############################################
        self.downloadButton.clicked.connect(self.url_download)
        self.downloadButton_2.clicked.connect(self.youtube_downloader)
        ##############################################
        # open files Button
        ####################################
        self.openmp4file.clicked.connect(self.open_mp4_file)
        self.openFileBrowser_2.clicked.connect(self.text_download)
        #######################################################
        # convert Button
        ####################################################
        self.downloadButton_4.clicked.connect(self.converter)
        ######################################################

    def progress_bar(self, blocknum, blocksize, totalsize):

        read = blocknum * blocksize
        percent = read * 100 / totalsize
        self.progressBar.setValue(int(percent))
        QApplication.processEvents()

    def save_location_browser_youtube(self):

        if platform == 'linux' or platform == 'darwin':
            self.location_place = QFileDialog.getExistingDirectory(self, caption='save location',
                                                                   directory=os.environ['HOME'])
        elif platform == 'Windows':
            self.location_place = QFileDialog.getExistingDirectory(self, caption='save location',
                                                                   directory=os.environ['Downloads'])
        self.mp3location.setText(self.location_place)
        self.locationPlace.setText(self.location_place)

    def save_locations_browser(self):
        global save_location
        if platform == 'linux' or platform == 'darwin':
            file = QFileDialog.getSaveFileName(self, caption='save file', directory=os.environ['HOME'],
                                               filter='all file (*.*)')
            save_location = str(file)[2:].split(',')[0].replace("'", '')
        elif platform == 'Windows':
            file = QFileDialog.getSaveFileName(self, caption='save file', directory=os.environ['Music'],
                                               filter='all file (*.*)')
            save_location = str(file)[2:].split(',')[0].replace("'", '')
        self.savelocationPlace.setText(save_location)

    # noinspection PyBroadException
    def __internet_testing(self):
        __testing_url = "https://www.google.com/"
        __timeout = 15
        requests.get(__testing_url, timeout=__timeout)

    def url_download(self, state):
        _url = self.urlPlace.text()
        _file_location = self.filePlace.text()
        try:
            self.timer = Timer(5.0, self.__internet_testing())
            if _file_location != "":
                for urls in self.data:
                    self.urlPlace.setText(urls)
                    print(urls)  # for testing propose
                    if urls != "":
                        if save_location == "":
                            if platform == "linux" or platform == "darwin":
                                _home = os.environ['HOME'] + '/Downloads/'
                                if path.exists(_home):
                                    try:
                                        urllib.request.urlretrieve(urls, "{}{}{}".format(_home, self.number,
                                                                                         os.path.basename(urls)),
                                                                   self.progress_bar)
                                    except ValueError:
                                        self.urlErrorMessage.exec_()
                                        return 1
                                    except Exception:
                                        self.DownloadFailed.exec_()
                                        return 1
                                else:
                                    os.mkdir(_home)
                                    try:
                                        urllib.request.urlretrieve(urls, "{}{}{}".format(_home, self.number,
                                                                                         os.path.basename(urls)),
                                                                   self.progress_bar)
                                    except ValueError:
                                        self.urlErrorMessage.exec_()
                                        return 1
                                    except Exception:
                                        self.DownloadFailed.exec_()
                                        return 1

                            elif platform == "Windows":
                                # need test
                                _home = os.path.join(os.environ["Downloads"])
                                if path.exists(_home):
                                    try:
                                        urllib.request.urlretrieve(urls, "{}{}{}".format(_home, self.number,
                                                                                         os.path.basename(urls)),
                                                                   self.progress_bar)
                                    except ValueError:
                                        self.urlErrorMessage.exec_()
                                        return 1
                                    except Exception:
                                        self.DownloadFailed.exec_()
                                        return 1
                                else:
                                    os.mkdir(_home)
                                    try:
                                        urllib.request.urlretrieve(urls, "{}{}{}".format(_home, self.number,
                                                                                         os.path.basename(urls)),
                                                                   self.progress_bar)
                                    except ValueError:
                                        self.urlErrorMessage.exec_()
                                        return 1
                                    except Exception:
                                        self.DownloadFailed.exec_()
                                        return 1

                            else:
                                pass
                        else:
                            try:
                                urllib.request.urlretrieve(urls, "{}{}{}".format(save_location, self.number,
                                                                                 os.path.basename(urls)),
                                                           self.progress_bar)
                            except ValueError:
                                self.urlErrorMessage.exec_()
                                return 1
                            except Exception:
                                self.DownloadFailed.exec_()
                                return 1
                        self.progressBar.setValue(0)
                        self.urlPlace.setText("")
                        self.number += 1
                        self.currentDownladsFile.display(self.number)
                    else:
                        pass
                self.download_Completed.exec_()
            elif _url == "":
                self.empty_url.exec_()
            else:
                if self.savelocationPlace.text() == "":
                    if platform == "linux" or platform == "darwin":
                        _home = os.environ['HOME'] + '/Downloads/'
                        if path.exists(_home):
                            try:
                                urllib.request.urlretrieve(_url, "{}{}{}".format(_home, self.number,
                                                                                 os.path.basename(_url)),
                                                           self.progress_bar)
                            except ValueError:
                                self.urlErrorMessage.exec_()
                                return 1
                            except Exception:
                                self.DownloadFailed.exec_()
                                return 1
                        else:
                            os.mkdir(_home)
                            try:
                                urllib.request.urlretrieve(_url, "{}{}{}".format(_home, self.number,
                                                                                 os.path.basename(_url)),
                                                           self.progress_bar)
                            except ValueError:
                                self.urlErrorMessage.exec_()
                                return 1
                            except Exception:
                                self.DownloadFailed.exec_()
                                return 1

                    elif platform == "Windows":
                        # need test
                        _home = os.path.join(os.environ["Downloads"])
                        if path.exists(_home):
                            try:
                                urllib.request.urlretrieve(_url, "{}{}{}".format(_home, self.number,
                                                                                 os.path.basename(_url)),
                                                           self.progress_bar)
                            except ValueError:
                                self.urlErrorMessage.exec_()
                                return 1
                            except Exception:
                                self.DownloadFailed.exec_()
                                return 1
                        else:
                            os.mkdir(_home)
                            try:
                                urllib.request.urlretrieve(_url, "{}{}{}".format(_home, self.number,
                                                                                 os.path.basename(_url)),
                                                           self.progress_bar)
                            except ValueError:
                                self.urlErrorMessage.exec_()
                                return 1
                            except Exception:
                                self.DownloadFailed.exec_()
                                return 1

                    else:
                        pass
                else:
                    try:
                        urllib.request.urlretrieve(_url, "{}{}{}".format(save_location, self.number,
                                                                         os.path.basename(_url)),
                                                   self.progress_bar)
                    except ValueError:
                        self.urlErrorMessage.exec_()
                        return 1
                    except Exception:
                        self.DownloadFailed.exec_()
                        return 1
                self.download_Completed.exec_()
                self.progressBar.setValue(0)
                self.urlPlace.setText("")
                self.savelocationPlace.setText("")
                self.number += 1
                self.currentDownladsFile.display(self.number)

        except (requests.ConnectionError, requests.Timeout) as exception:
            self.check_internet_connection.exec_()
        QApplication.processEvents()

    def text_download(self):

        if platform == 'linux' or platform == 'darwin':
            open_file = QFileDialog.getOpenFileName(self, caption="Open File", directory=os.environ['HOME'],
                                                    filter='Text files  (*.txt)')
            text = str(open_file)[2:].split(",")[0].replace("'", "")
            self.filePlace.setText(text)
            try:
                read_file = open(text, 'r')
                with read_file:
                    self.data = read_file.read().split('\n')
                # return self.data
            except Exception:
                pass
        elif platform == 'Windows':
            open_file = QFileDialog.getOpenFileName(self, caption="Open File",
                                                    directory=os.environ['Documents'], filter='Text files (*.txt)')
            text = str(open_file)[2:].split(",")[0].replace("'", '')
            self.filePlace.setText(text)
            read_file = open(text, 'r')
            with read_file:
                self.data = read_file.read().split('\n')
        QApplication.processEvents()

    def open_mp4_file(self):
        global file
        if platform == 'linux' or platform == 'darwin':
            mp4_file = QFileDialog.getOpenFileName(self, "open file", os.environ['HOME'], filter='video files (*.mp4)')
            file = str(mp4_file)[2:].split(',')[0].replace("'", '')
        elif platform == 'Windows':
            mp4_file = QFileDialog.getOpenFileName(self, caption="open file", directory=os.environ["Videos"],
                                                   filter='video file (*.mp4)')
            file = str(mp4_file)[2:].split(',')[0].replace("'", '')
        self.mp4filename.setText(file)
        QApplication.processEvents()

    # noinspection PyGlobalUndefined
    def converter(self):
        self.convert_number += 1
        try:
            self.___mp4 = file  # global var file from open_mp4_file method
        except NameError:
            self.convert_empty_mp4_file.exec_()
            return 1
        try:
            self.___mp3 = save_location + ".mp3"
        except NameError:
            if platform == "linux" or platform == 'darwin':
                self.___mp3 = os.path.join(os.environ['HOME'], 'Downloads/file{}.mp3'.format(self.convert_number))
            else:
                self.___mp3 = os.path.join(os.environ['Music'], '/file{}.mp3'.format(self.convert_number))
        __video_clip = VideoFileClip(self.___mp4)
        __audio_clip = __video_clip.audio
        __audio_clip.write_audiofile(self.___mp3)
        __audio_clip.close()
        __video_clip.close()
        self.currentConvertedFile.display(self.convert_number)
        self.convert_completed.setText('Convert {} to mp3 is Completed'.format(os.path.basename(self.___mp4)))
        self.convert_completed.setInformativeText('saved on {}\nClick \'Ok\' To Convert Another file Thanks'
                                                  .format(self.___mp3))
        self.convert_completed.exec_()
        QApplication.processEvents()

    def search_quality(self):
        # TODO : EXCEPTION TEST
        # noinspection PyGlobalUndefined
        # need test to get error  message

        global _video
        if self.youtub_url.text() != "":
            try:
                _video = pafy.new(url=self.youtub_url.text())
                streams = _video.videostreams
                for stream in streams:
                    size = humanize.naturalsize(stream.get_filesize())
                    data = '{} {} {} {}'.format(stream.mediatype, stream.extension, stream.quality, size)
                    self.qualityBox_2.addItem(data)
            except ValueError:
                self.urlErrorMessage.exec_()
        else:
            self.empty_url.exec_()
        QApplication.processEvents()

    def video_progressbar(self, total, recvd, ratio, rate, eta):
        self.progressBar_2.setValue(int(ratio * 100))
        QApplication.processEvents()

    def youtube_downloader(self):
        # TODO :EXCEPTION TEST FOR DOWNLOAD VAR (state Ok)
        if self.youtub_url.text() != "":
            self.youtube_video_downloaded += 1
            if self.location_place is not None:
                _file = _video.videostreams
                quality = self.qualityBox_2.currentIndex()
                download = _file[quality].download(filepath=self.location_place, callback=self.video_progressbar)
            else:
                _file = _video.videostreams
                quality = self.qualityBox_2.currentIndex()
                if platform == 'linux' or platform == 'darwin':
                    if os.path.exists(os.environ['HOME'] + '/Downloads/'):
                        download = _file[quality].download(filepath=os.environ['HOME'] + '/Downloads/',
                                                           callback=self.video_progressbar)
                    else:
                        os.mkdir(os.environ['HOME'] + '/Downloads/')
                        download = _file[quality].download(filepath=os.environ['HOME'] + '/Downloads/',
                                                           callback=self.video_progressbar)
                else:
                    # need test
                    download = _file[quality].download(filepath=os.environ['Videos'],
                                                       callback=self.video_progressbar)
            self.currentDownladFile_2.display(self.youtube_video_downloaded)
            self.youtub_url.setText('')
            self.qualityBox_2.clear()

        else:
            self.empty_url.exec_()
        QApplication.processEvents()


# TODO: FIX PROGRAMME NOT RESPONDING
def main():
    apps = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    main()
