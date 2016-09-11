from __future__ import print_function
from subprocess import Popen, PIPE
import wx


class MonkeyTest(wx.Frame):
    """ This class is to build and run the monkey command """

    # class constants with static part of monkey command
    cmd = 'adb shell monkey -p '
    verbose_level = ' -v -v -v '

    def __init__(self, parent, id):
        self.package_name = None
        self.events_number = None
        self.monkey_command = None
        self.monkey_events = None
        self.event_file = None

        # wx panel design
        wx.Frame.__init__(self, parent, id, 'Android Monkey Test', size=(400, 400))
        monkey_test_panel = wx.Panel(self)

        # UX for User inputs
        self.basic_label = wx.StaticText(monkey_test_panel, -1, "Package Name:")
        self.basic_text = wx.TextCtrl(monkey_test_panel, -1, "Enter your app package name", size=(175, -1))
        self.basic_text.SetInsertionPoint(0)
        self.num_of_events_label = wx.StaticText(monkey_test_panel, -1, "Number of events:")
        self.num_of_events = wx.TextCtrl(monkey_test_panel, -1, "200", size=(175, -1))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([self.basic_label, self.basic_text, self.num_of_events_label, self.num_of_events])
        monkey_test_panel.SetSizer(sizer)

        # button action
        run_monkey_button = wx.Button(monkey_test_panel, label='Run', pos=(300, 300), size=(40, 40))
        self.Bind(wx.EVT_BUTTON, self.runtest, run_monkey_button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

    def build_monkey_command(self):
        """returns the adb command """
        self.monkey_command = self.cmd + self.package_name + self.verbose_level + self.events_number
        return self.monkey_command

    def run_monkey_test(self):
        """ adb command, runs the monkey command and saves the monkey events to text file"""
        self.build_monkey_command()
        print(self.monkey_command)
        process = Popen(self.monkey_command, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()
        self.monkey_events = stdout
        if True:
            self.event_file = open('Event_log.txt', 'w')
            self.event_file.write(self.monkey_events)
            self.event_file.close()
        else:
            print('error:', stderr)

    def runtest(self, event):
        self.package_name = str(self.basic_text.GetValue())
        self.events_number = str(self.num_of_events.GetValue())
        self.run_monkey_test()

    def closewindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MonkeyTest(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
