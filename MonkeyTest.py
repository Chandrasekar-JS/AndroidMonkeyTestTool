from __future__ import print_function
from subprocess import Popen, PIPE


class MonkeyTest(object):

    """ This class is to build and run the monkey command """

    # class constants with static part of monkey command
    cmd = 'adb shell monkey -p '
    verbose_level = ' -v -v -v '

    def __init__(self, package_name, number_of_events):
        self.package_name = package_name
        self.events_number = str(number_of_events)
        self.monkey_command = None
        self.monkey_events = None
        self.event_file = None

    def build_monkey_command(self):
        """returns the adb command """
        self.monkey_command = self.cmd + self.package_name + self.verbose_level + self.events_number
        return self.monkey_command

    def run_monkey_test(self):
        """ adb command, runs the monkey command and saves the monkey events to text file"""
        self.build_monkey_command()
        process = Popen(self.monkey_command, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()
        self.monkey_events = stdout
        if True:
            self.event_file = open('Event_log.txt', 'w')
            self.event_file.write(self.monkey_events)
            self.event_file.close()
        else:
            print ('error:', stderr)

Monkey_test = MonkeyTest('com.yourPackageName.android', 'replaceWithNumber')
Monkey_test.run_monkey_test()
