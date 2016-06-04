#! /usr/bin/env python

import codecs
import re, os, sys, math, locale,time
import MP3Info
import id3reader

pauseOnError = 'false'
pauseOnUnicode = 'false'
found = 0
tagError = 0
lengthError = 0
unicodeError = 0
filePathError = 0
corruptError = 0
windowsError5 = 0
windowsError = 0
tc = 0

def GetTrackInfo(filePath):
    
    global pauseOnError
    global pauseOnUnicode
    global found
    global tagError
    global lengthError
    global unicodeError
    global filePathError
    global corruptError
    global windowsError5
    global windowsError

    length = 0
    title = ""
    artist = ""
    album = ""
    genre = ""
    
    # Construct a reader from a file or filename.
    id3r = id3reader.Reader(filePath)
    try:
        op = 'retrieving length';
        f = codecs.open(filePath, 'rb')
        i = MP3Info.MP3Info(f)
        # length = i.mpeg.total_time
        length = i.mpeg.length
        op = 'retrieving title';
        title = id3r.getValue(u'title')
        op = 'retrieving artist';
        artist = id3r.getValue(u'performer')
        op = 'retrieving album';
        album = id3r.getValue(u'album')
        op = 'retrieving genre';
        genre = id3r.getValue(u'genre')
    
    except UnicodeEncodeError:
        unicodeError = unicodeError + 1
        try:
            print "Error with Unicode in %s while %s" % (filePath, op);
            if pauseOnUnicode == 'true':
                raw_input("Press ENTER to continue...")
        except UnicodeEncodeError:
            print " unprintable filename";
            if pauseOnUnicode == 'true':
                raw_input("Press ENTER to continue...")
    except:
        try:
            if op == 'retrieving length':
                lengthError = lengthError + 1
            print "Unhandled Exception in %s while %s" % (filePath, op);
            if pauseOnError == 'true':
                raw_input("Press ENTER to continue...")
        except UnicodeEncodeError:
            unicodeError = unicodeError + 1
            print " unprintable filename";
            if pauseOnError == 'true':
                raw_input("Press ENTER to continue...")

    return length, title, artist, album, genre

def WriteLibraryFolder(f, curPath, rootPath):
    trackCount = 0;
    global pauseOnError
    global pauseOnUnicode
    global found
    global tagError
    global lengthError
    global unicodeError
    global filePathError
    global corruptError
    global windowsError5
    global windowsError
    global tc

    dirs = []
    try:
        os.chdir(curPath)
        op = 'reading directory';
        for fileName in os.listdir(u'.'):
            op = 'reading fullname';
            fullName = os.path.normpath(os.path.join(curPath, fileName))
            fullName = fullName.replace(u'\\', '/')

            if os.path.isdir(fullName):
                dirs.append(fullName)

            else:
                if fullName.lower().endswith(u'.mp3'):
                    found = found + 1
                    # Strip the root and the extension
                    shortName = fullName.replace(rootPath + 'Music/', '')
                    shortName = shortName.replace('.mp3', '')
                    shortName = shortName.replace('.Mp3', '')
                    shortName = shortName.replace('.mP3', '')
                    shortName = shortName.replace('.MP3', '')
                    shortName = shortName.replace('/', '\\')
                    shortName = clean(shortName)

                    # Fetch the length of the track in seconds.
                    length, title, artist, album, genre = GetTrackInfo(fullName)

                    # Replace quotes
                    op = 'retrieving tags';
                    if (title):
                        title = clean(title)
                    if (artist):
                        artist = clean(artist)
                    if (album):
                        album = clean(album)
                    if (genre):
                        genre = clean(genre) 

                    if length > 0:
                        try:
                            print 'Found %s (%s secs)' % (shortName, length)
                            op = 'adding to playlist'
                            #f.write('   Song("%s", %s, "%s", "%s", "%s", "%s");\n' % (shortName, length, title, artist, album, genre));
                            #f.write('  {\n')
                            #f.write('      ["Album"] = "%s",\n' % album);
                            #f.write('      ["Name"] = "%s",\n' % shortName);
                            #f.write('      ["Genre"] = "%s",\n' % genre);
                            #f.write('      ["Length"] = %s,\n' % length);
                            #f.write('      ["Artist"] = "%s",\n' % artist);
                            #f.write('      ["Title"] = "%s",\n' % title);
                            #f.write('  }, -- [%s]\n' % (tc + 1));
                            f.write('   Soundtrack.Library.AddTrack("%s", %s, "%s", "%s", "%s");\n' % (shortName, length, title, artist, album));

                            trackCount = trackCount + 1
                            tc = tc + 1
                        except UnicodeEncodeError:
                            unicodeError = unicodeError + 1
                            try:
                                print "Error with Unicode in %s (%s) while %s" % (fullName, shortName, op);
                                if pauseOnUnicode == 'true':
                                    raw_input("Press ENTER to continue...")
                            except UnicodeEncodeError:
                                print "unprintable filename while ", (op);
                                if pauseOnUnicode == 'true':
                                    raw_input("Press ENTER to continue...")
                        except IOError:
                            if len(fullName) > 255:
                                filePathError = filePathError + 1
                                print "File error in %s (%s) while %s, The filepath is too long." % (fullName, shortName, op);
                                if pauseOnError == 'true':
                                    raw_input("Press ENTER to continue...")
                            else:
                                corruptError = corruptError + 1
                                print "Unknown Error in %s while %s" % (fullName, op);
                                if pauseOnError == 'true':
                                    raw_input("Press ENTER to continue...")

                        except UnicodeDecodeError:
                            unicodeError = unicodeError + 1
                            try:
                                print "Error with Unicode in %s (%s) while %s" % (fullName, shortName, op);
                                if pauseOnUnicode == 'true':    
                                    raw_input("Press ENTER to continue...")
                            except UnicodeEncodeError:
                                print "unprintable filename while ", (op);
                                if pauseOnUnicode == 'true':
                                    raw_input("Press ENTER to continue...")
    except UnicodeEncodeError:
        unicodeError = unicodeError + 1
        try:
            print "Error with Unicode in %s while %s" % (curPath, op);
            if pauseOnUnicode == 'true':
                raw_input("Press ENTER to continue...")
        except UnicodeEncodeError:
            print " unprintable directory name";
            if pauseOnUnicode == 'true':
                raw_input("Press ENTER to continue...")
    except UnicodeDecodeError:
        unicodeError = unicodeError + 1
        try:
            print "Error with Unicode in %s (%s) while %s" % (curPath, shortName, op);
            if pauseOnUnicode == 'true':
                raw_input("Press ENTER to continue...")
        except UnicodeEncodeError:
            print "unprintable filename while ", (op);
            if pauseOnUnicode == 'true':
                raw_input("Press ENTER to continue...")
    except IOError:
        if len(curPath) > 255:
            filePathError = filePathError + 1
            print "Directory error in %s while %s, The filepath is too long." % (curPath, op);
            if pauseOnError == 'true':
                raw_input("Press ENTER to continue...")
        else:
            corruptError = corruptError + 1
            print "Unknown Error in %s" % curPath;
            if pauseOnError == 'true':
                raw_input("Press ENTER to continue...")
    except WindowsError, (errno, strerror):
        if errno == 5:
            windowsError5 = windowsError5 + 1
            if pauseOnError == 'true':
                print curPath;
                print strerror;
                raw_input("Press ENTER to continue...")
        else:
            windowsError = windowsError + 1
            if pauseOnError == 'true':
                print errno
                print strerror;
                raw_input("Press ENTER to continue...")
            
            
    for dirName in dirs:
        trackCount = WriteLibraryFolder(f, dirName, rootPath) + trackCount
    
    return trackCount
def clean(x):
    global pauseOnError
    global pauseOnUnicode
    global unicodeError
    try:
        op = 'cleaning'
        x = x.replace('\\', '\\\\')
        x = x.replace('"', '\\"')
        x = x.replace("'", "\\'")
        x = x.replace(u'\xb4' , u'\\195\\116')
        x = x.replace(u'\xc0' , u'\\195\\128')
        x = x.replace(u'\xc1' , u'\\195\\129')
        x = x.replace(u'\xc2' , u'\\195\\130')
        x = x.replace(u'\xc3' , u'\\195\\131')
        x = x.replace(u'\xc4' , u'\\195\\132')
        x = x.replace(u'\xc5' , u'\\195\\133')
        x = x.replace(u'\xc6' , u'\\195\\134')
        x = x.replace(u'\xc7' , u'\\195\\135')
        x = x.replace(u'\xc8' , u'\\195\\136')
        x = x.replace(u'\xc9' , u'\\195\\137')
        x = x.replace(u'\xca' , u'\\195\\138')
        x = x.replace(u'\xcb' , u'\\195\\139')
        x = x.replace(u'\xcc' , u'\\195\\140')
        x = x.replace(u'\xcd' , u'\\195\\141')
        x = x.replace(u'\xce' , u'\\195\\142')
        x = x.replace(u'\xcf' , u'\\195\\143')
        x = x.replace(u'\xd0' , u'\\195\\144')
        x = x.replace(u'\xd1' , u'\\195\\145')
        x = x.replace(u'\xd2' , u'\\195\\146')
        x = x.replace(u'\xd3' , u'\\195\\147')
        x = x.replace(u'\xd4' , u'\\195\\148')
        x = x.replace(u'\xd5' , u'\\195\\149')
        x = x.replace(u'\xd6' , u'\\195\\150')
        x = x.replace(u'\xd7' , u'\\195\\151')
        x = x.replace(u'\xd8' , u'\\195\\152')
        x = x.replace(u'\xd9' , u'\\195\\153')
        x = x.replace(u'\xda' , u'\\195\\154')
        x = x.replace(u'\xdb' , u'\\195\\155')
        x = x.replace(u'\xdc' , u'\\195\\156')
        x = x.replace(u'\xdd' , u'\\195\\157')
        x = x.replace(u'\xde' , u'\\195\\158')
        x = x.replace(u'\xdf' , u'\\195\\159')
        x = x.replace(u'\xe0' , u'\\195\\160')
        x = x.replace(u'\xe1' , u'\\195\\161')
        x = x.replace(u'\xe2' , u'\\195\\162')
        x = x.replace(u'\xe3' , u'\\195\\163')
        x = x.replace(u'\xe4' , u'\\195\\164')
        x = x.replace(u'\xe5' , u'\\195\\165')
        x = x.replace(u'\xe6' , u'\\195\\166')
        x = x.replace(u'\xe7' , u'\\195\\167')
        x = x.replace(u'\xe8' , u'\\195\\168')
        x = x.replace(u'\xe9' , u'\\195\\169')
        x = x.replace(u'\xea' , u'\\195\\170')
        x = x.replace(u'\xeb' , u'\\195\\171')
        x = x.replace(u'\xec' , u'\\195\\172')
        x = x.replace(u'\xed' , u'\\195\\173')
        x = x.replace(u'\xee' , u'\\195\\174')
        x = x.replace(u'\xef' , u'\\195\\175')
        x = x.replace(u'\xf0' , u'\\195\\176')
        x = x.replace(u'\xf1' , u'\\195\\177')
        x = x.replace(u'\xf2' , u'\\195\\178')
        x = x.replace(u'\xf3' , u'\\195\\179')
        x = x.replace(u'\xf4' , u'\\195\\180')
        x = x.replace(u'\xf5' , u'\\195\\181')
        x = x.replace(u'\xf6' , u'\\195\\182')
        x = x.replace(u'\xf7' , u'\\195\\183')
        x = x.replace(u'\xf8' , u'\\195\\184')
        x = x.replace(u'\xf9' , u'\\195\\185')
        x = x.replace(u'\xfa' , u'\\195\\186')
        x = x.replace(u'\xfb' , u'\\195\\187')
        x = x.replace(u'\xfc' , u'\\195\\188')
        x = x.replace(u'\xfd' , u'\\195\\189')
        x = x.replace(u'\xfe' , u'\\195\\190')
        x = x.replace(u'\xff' , u'\\195\\191')
    except UnicodeEncodeError:
        try:
            if pauseOnUnicode == 'true':
                print "Error with Unicode in %s while %s" % (x, op);
                raw_input("Press ENTER to continue...")
        except UnicodeEncodeError:
            if pauseOnUnicode == 'true':
                print "unprintable tag while ", (op);
                raw_input("Press ENTER to continue...")
    except UnicodeDecodeError:
        try:
            if pauseOnUnicode == 'true':
                print "Error with Unicode in %s while %s" % (x, op);
                raw_input("Press ENTER to continue...")
        except UnicodeEncodeError:
            if pauseOnUnicode == 'true':
                print "unprintable tag while ", (op);
                raw_input("Press ENTER to continue...")
    return x

def main(argv, stdout, environ):
    pathname = os.path.dirname(sys.argv[0])
    workingPath = os.path.abspath(pathname) 
    workingPath = workingPath.replace('\\', '/')
    workingPath = workingPath.replace('/Music Manager', '')
    print '' + workingPath
    
    mp3Path = workingPath + 'Music/'
    scriptFilePath = workingPath + 'Music/MyTracks.lua'
    global pauseOnError
    global pauseOnUnicode
    global found
    global tagError
    global lengthError
    global unicodeError
    global filePathError
    global corruptError
    global windowsError5
    global windowsError
    global tc

    if not os.path.isdir(mp3Path):
        print 'ERROR : Cannot find the folder ' + mp3Path
        print 'Soundtrack needs to have your music under Interface/AddOns/SoundtrackMusic'
        raw_input("Press ENTER to continue...")

    trackCount = 0;
    
    #if raw_input("Pause on Unicode errors? (y/n)\n") == 'y':
    #   pauseOnUnicode = 'true'
    #else:
    #   pauseOnUnicode = 'false'
        
    #if raw_input("Pause on other errors? (y/n)\n") == 'y':
    #   pauseOnError = 'true'
    #else:
    #   pauseOnError = 'false'

    #text = f.read()
    #f = open(scriptFilePath, 'w')
    f = codecs.open(scriptFilePath, "w", "utf-8")
    f.write(u'-- This file is automatically generated\n')
    f.write(u'-- Please do not edit it.\n')
    f.write(u'SMP3_PL_VERSION = "')
    f.write(time.ctime())
    f.write(u'"\n')
    f.write(u'function Soundtrack_LoadMyTracks()\n')
    f.write(u'   if Soundtrack.Settings.MyTracksVersion == nil or Soundtrack.Settings.MyTracksVersion ~= SMP3_PL_VERSION then\n')
    f.write(u'   Soundtrack.Settings.MyTracksVersion = SMP3_PL_VERSION\n')
    f.write(u'   Soundtrack.Settings.MyTracksVersionSame = false\n')
    f.write(u'   else\n')
    f.write(u'   Soundtrack.Settings.MyTracksVersionSame = true\n')
    f.write(u'   end\n')
    
    print 'Scanning ' + mp3Path

    trackCount = WriteLibraryFolder(f, mp3Path, workingPath) + trackCount


    f.write(u'end\n')
    f.close()

    print ' '
    print 'Finished writing MyTracks.lua.'
    print 'Found %s track(s).' % trackCount
    print 'The tracks should now be available within the game!'
    print ' '
    print 'Some interesting facts about your mp3s:'
    print '%i mp3s were found' % found
    if tagError > 0:
        print '%i of them had errors while retrieving tags' % tagError
    if lengthError > 0:
        print '%i of them had errors while retrieving length' % lengthError
    if unicodeError > 0:
        print '%i of them had errors with Unicode characters' % unicodeError
    if filePathError > 0:
        print '%i of them had errors with the filepath length' % filePathError
    if corruptError > 0:
        print '%i of them may be corrupt in some way' % corruptError
    if windowsError5 > 0:
        print 'There were also %i errors from inaccessible directories' % windowsError5
    if windowsError > 0:
        print 'There were also %i other errors' % windowsError
    print ' '
    raw_input("Press ENTER to continue...")


if __name__ == "__main__":
  main(sys.argv, sys.stdout, os.environ)

