#!/usr/bin/env python

import os
import sys
import subprocess
import time


class Watcher:
    _process = None
    _history = {}

    def __init__(self, command, *targets):
        self.command = command
        self.targets = targets

    def start(self):
        self.spawn_process()

    def initialize(self):
        for source in self.targets:
            last_modified = os.path.getmtime(source)
            self._history[source] = last_modified

    def update(self):
        for source in self.targets:
            if os.path.getmtime(source) != self._history[source]:
                self.spawn_process()

    def spawn_process(self):
        if self._process is not None and self._process.poll():
            self.kill_process()

        kwargs = {"shell": True, "start_new_session": True}
        self.initialize()
        self._process = subprocess.Popen([self.command], **kwargs)

    def kill_process(self):
        if self._process is None:
            return
        self._process.terminate()
        self._process.wait()
        self._process = None


def main_loop():
    watcher = Watcher(sys.argv[1], *sys.argv[2:])
    watcher.start()
    try:
        while 1:
            try:
                watcher.update()
            except Exception as e:
                print(e)
                return 1
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        watcher.kill_process()
        return 0


def check_args():
    if len(sys.argv) < 3:
        if len(sys.argv) < 2:
            print("No command file!")
        print("No targets given!")
        sys.exit(1)

    fail = False
    for each in sys.argv[2:]:
        if not os.path.exists(each):
            fail = True
            print("Target <%s> doesn't exist!" % each)
    if fail:
        sys.exit(1)


if __name__ == '__main__':
    check_args()
    try:
        sys.exit(main_loop())
    except Exception as e:
        print(e)
        sys.exit(1)
